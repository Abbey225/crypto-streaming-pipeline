# Real-Time Crypto Data Streaming Pipeline

## 📌 Project Overview
This project establishes a real-time data ingestion pipeline that captures streaming asset valuations via a public REST API, normalizes data payloads using Python, and appends micro-batches into an analytical database.

## 🏗️ Architecture Design
* **Data Source:** Live REST API (CoinGecko)
* **Ingestion Engine:** Python Requests & Time-Series Micro-batching Loop
* **Target Warehouse:** PostgreSQL (Analytical Engine)
* **Infrastructure:** Docker Containerization

## 💡 SSIS Translation: Why I Built It This Way
Coming from an **SSIS (SQL Server Integration Services)** background, this project replaces the traditional **SSIS Data Flow Task (JSON Source -> OLE DB Destination)** with a code-first, memory-efficient Python streaming architecture. Instead of running heavy on-premise package execution engines, this light script containerizes perfectly for modern cloud scale.
