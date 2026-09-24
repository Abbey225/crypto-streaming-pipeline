import time
import requests
import psycopg2
from datetime import datetime

def fetch_live_prices():
    # Fetch real-time crypto prices from a public API
    url = "https://coingecko.com"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"❌ Error fetching streaming data: {e}")
        return None

def write_to_warehouse():
    # Connect to the target analytical warehouse
    conn = psycopg2.connect(
        host="localhost", database="crypto_warehouse", user="data_engineer", password="password123"
    )
    cursor = conn.cursor()

    # Create the time-series analytical table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_crypto_prices (
            ticker VARCHAR(10),
            price_usd NUMERIC(18, 4),
            volume_24h NUMERIC(18, 2),
            extracted_at TIMESTAMP
        );
    """)
    conn.commit()

    print("🛰️ Starting live micro-batch stream (Press Ctrl+C to stop)...")
    
    # Simulate a streaming micro-batch listener loop
    for i in range(5):  
        data = fetch_live_prices()
        if data:
            timestamp = datetime.now()
            
            # SSIS Equivalent: Split and parse the incoming JSON stream records
            for asset in ['bitcoin', 'ethereum']:
                ticker = 'BTC' if asset == 'bitcoin' else 'ETH'
                price = data[asset]['usd']
                volume = data[asset]['usd_24h_vol']
                
                cursor.execute(
                    "INSERT INTO fact_crypto_prices (ticker, price_usd, volume_24h, extracted_at) VALUES (%s, %s, %s, %s);",
                    (ticker, price, volume, timestamp)
                )
            conn.commit()
            print(f"✅ Ingested live streaming updates at {timestamp.strftime('%H:%M:%S')}")
        
        time.sleep(10) # Wait 10 seconds before fetching the next streaming event

    cursor.close()
    conn.close()

if __name__ == "__main__":
    write_to_warehouse()
