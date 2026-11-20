import sqlite3
import requests
from datetime import datetime
import time

def create_table():
    #assign connection to the variable conn
    conn = sqlite3.connect("iss_positions.db")
    #assign cursor to the variable cursor
    cursor = conn.cursor()
    #write SQL query
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS iss_positions(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           Date_time TEXT,
           LATITUDE REAL,
           LONGITUDE REAL
           )
        """,
        )
    #save and close
    conn.commit()
    conn.close()

def extract_iss_data():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    timestamp = data["timestamp"]
    date_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    return date_time, latitude, longitude

def save_data(date_time, latitude, longitude):
     #assign connection to the variable conn
     conn = sqlite3.connect("iss_positions.db")
     #assign cursor to the variable cursor
     cursor = conn.cursor()
     #write SQL query
     cursor.execute(
         """
         INSERT INTO iss_positions (date_time, latitude, longitude) VALUES (?, ?, ?)
         """,
         (date_time, latitude, longitude),
         )
     #save and close
     conn.commit()
     conn.close()
     print("data successfully saved to database!") 

if __name__ == "__main__":
    create_table()
    print("ISS Tracking Pipeline started. Press Ctrl+C to stop.")
    
    while True:
        try:
            # Estrazione e salvataggio in loop
            date_time, latitude, longitude = extract_iss_data()
            save_data(date_time, latitude, longitude)
            
            # Attendi 60 secondi prima della prossima richiesta
            time.sleep(60)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(10)