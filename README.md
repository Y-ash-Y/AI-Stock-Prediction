# 🏦 Ai_Stock_Prediction — Quant Research & Trading Platform

## 📌 Overview
This project is a **quant-desk-grade research & trading platform** that mimics the workflow inside top HFT / prop firms (Optiver, Jane Street, Tower Research, Quadeye).  
It provides a full stack from **tick-level ingestion → feature engineering → strategy research → backtesting → execution → risk → dashboard**.

The goal: build institutional-level infra, not a retail bot.

---

## 🧩 Features

### 🔹 Data Layer
- Tick + order book (L2) ingestion from **Binance (crypto)** and **NSE/BSE (Zerodha)**.
- Storage in **ClickHouse** (fast columnar DB) with **CSV fallback**.
- Historical backfill + real-time streaming.

### 🔹 Feature Engineering
- **Microstructure signals**: Order Flow Imbalance (OFI), trade sign autocorrelation, queue dynamics.
- **Volatility models**: realized vol, HAR-RV, GARCH (planned).
- **Factor models**: PCA, cointegration features.

### 🔹 Strategies
- **Market Making**: quoting around mid-price (Avellaneda–Stoikov base).
- **Stat Arb**: cointegration, Kalman-filter pairs trading.
- **Execution Algos**: TWAP, VWAP, POV.
- **ML/RL Alpha (planned)**: short-horizon prediction, reinforcement learning execution.

### 🔹 Backtesting
- **Event-driven simulator** with tick/L2 data.
- Latency + slippage + queue-priority modeling.
- Multi-strategy, portfolio-level PnL aggregation.

### 🔹 Risk Management
- Hard limits: gross exposure, max position.
- Soft limits: inventory control, stop-loss.
- Kill-switch (drops all orders on disconnect).

### 🔹 Reporting
- Risk & performance metrics: Sharpe, Sortino, drawdown, expected shortfall.
- PnL attribution by strategy, symbol, time-of-day.
- Execution quality: slippage vs VWAP/TWAP benchmarks.

### 🔹 Dashboard & API
- **Streamlit dashboard**: live signals, order book, PnL, risk.
- **FastAPI service**: REST endpoints for signals, positions, risk.
- **Quant Copilot (planned)**: AI assistant explaining strategy performance.

---

## 📂 Project Structure
    Ai_Stock_Prediction/
    ├── configs/ # system, market, strategy configs
    ├── data/ # raw ticks/BBO, processed features, saved models
    ├── docs/ # math notes & strategy writeups
    ├── notebooks/ # Jupyter exploration notebooks
    ├── reports/ # backtest reports & plots
    ├── src/qtrade/ # main source code
    │ ├── core/ # config + utils
    │ ├── datafeed/ # Binance/Zerodha feeds
    │ ├── storage/ # ClickHouse/CSV sinks
    │ ├── features/ # signal engineering
    │ ├── strategies/ # market making, stat arb
    │ ├── backtest/ # event-driven simulator
    │ ├── execution/ # risk + routing
    │ ├── evaluation/ # metrics & attribution
    │ ├── api/ # FastAPI service
    │ ├── dashboard/ # Streamlit UI
    │ └── scripts/ # CLI commands
    └── tests/ # pytest unit tests

---

## 🚀 Quickstart

### 1. Clone & Setup
```bash
git clone https://github.com/<your-username>/Ai_Stock_Prediction.git
cd Ai_Stock_Prediction
python -m venv .venv
source .venv/bin/activate    # (Linux/Mac)
.\.venv\Scripts\Activate.ps1 # (Windows PowerShell)
pip install -e .

