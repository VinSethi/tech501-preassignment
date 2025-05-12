from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    cities = ["London", "New York", "Tokyo", "Mumbai", "Sydney"]

    print("🔍 Extracting data...")
    raw = extract_data(cities)
    print(f"✅ Extracted data for {len(raw)} cities.")

    print("🧹 Transforming data...")
    clean = transform_data(raw)
    print(f"✅ Transformed data: {clean.shape[0]} rows.")

    print("📦 Loading data into MySQL...")
    load_data(clean)
    print("✅ ETL process completed!")

if __name__ == "__main__":
    run_etl()
