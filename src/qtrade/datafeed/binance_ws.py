import asyncio
import json
import aiohttp
from loguru import logger

BINANCE_WS = "wss://stream.binance.com:9443/stream"

class BinanceWS:
    """
    Binance WebSocket client for combined streams.
    Subscribes to trades + depth updates for given symbols.
    Handles reconnection with exponential backoff.
    """

    def __init__(self, symbols: list[str], depth: int = 10, url: str = BINANCE_WS):
        self.symbols = [s.upper() for s in symbols]
        self.depth = depth
        self.url = url
        self._stop = asyncio.Event()

    def _build_params(self) -> list[str]:
        params = []
        for s in self.symbols:
            s_low = s.lower()
            # subscribe to trades + orderbook depth
            params += [f"{s_low}@trade", f"{s_low}@depth{self.depth}@100ms"]
        return params

    async def stop(self):
        """Stop the websocket gracefully"""
        self._stop.set()

    async def run(self, on_message):
        """
        Run the WS loop. Calls `on_message(stream, data)` for each event.
        """
        backoff = 1
        while not self._stop.is_set():
            try:
                params = self._build_params()
                payload = {"method": "SUBSCRIBE", "params": params, "id": 1}

                async with aiohttp.ClientSession() as session:
                    async with session.ws_connect(self.url, heartbeat=30) as ws:
                        await ws.send_json(payload)
                        logger.info("Subscribed to Binance WS: {}", params)
                        backoff = 1  # reset backoff on success

                        async for msg in ws:
                            if self._stop.is_set():
                                break
                            if msg.type == aiohttp.WSMsgType.TEXT:
                                data = json.loads(msg.data)
                                if "stream" in data and "data" in data:
                                    # pass event to callback
                                    await on_message(data["stream"], data["data"])
                            elif msg.type == aiohttp.WSMsgType.ERROR:
                                raise RuntimeError("WebSocket message error")

            except Exception as e:
                logger.warning("WS error: {}. Reconnecting in {}s...", e, backoff)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30)  # exponential backoff, max 30s
