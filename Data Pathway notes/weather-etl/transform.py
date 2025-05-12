import pandas as pd

def transform_data(raw_data):
    records = []
    for entry in raw_data:
        record = {
            "city": entry["name"],
            "timestamp": pd.to_datetime(entry["dt"], unit='s'),
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "pressure": entry["main"]["pressure"],
            "weather": entry["weather"][0]["description"]
        }
        records.append(record)
    df = pd.DataFrame(records)
    return df.drop_duplicates().reset_index(drop=True)
