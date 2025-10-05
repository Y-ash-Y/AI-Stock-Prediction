import asyncio
from qtrade.datafeed.binance_ws import BinanceWS

async def main():
    async def on_message(stream, data):
        print(stream, data)   # just print raw events

    ws = BinanceWS(symbols=["BTCUSDT"], depth=5)
    await ws.run(on_message)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped.")
