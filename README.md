# ISS Position Tracker Pipeline

A lightweight Python ETL (Extract, Transform, Load) pipeline that fetches real-time coordinates of the International Space Station (ISS) from a public API, parses and formats the telemetry data, and stores it locally in an SQLite database.

## 🚀 Tech Stack
- **Python 3.x**
- **Requests** (API HTTP requests)
- **SQLite3** (Relational database storage)
- **Datetime** (Timestamp conversion)

## 📊 Pipeline Architecture
1. **Extract:** Queries the open-notify API (`http://api.open-notify.org/iss-now.json`) to retrieve current geolocation data and Unix timestamps.
2. **Transform:** Converts JSON payloads into clean numeric floats and formats UTC timestamps into human-readable strings (`YYYY-MM-DD HH:MM:SS`).
3. **Load:** Persists the structured records securely into an SQLite database (`positions.db`) using parameterized SQL queries.

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/tuo-username/pipeline_iss_tracker.git](https://github.com/tuo-username/pipeline_iss_tracker.git)
   cd pipeline_iss_tracker