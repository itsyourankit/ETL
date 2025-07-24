"""
Python Extract Transform Load Example (MySQL Version)
"""

import requests
import pandas as pd
from sqlalchemy import create_engine

def extract() -> dict:
    """Extracts data from universities API"""
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()
    return data

def transform(data: dict) -> pd.DataFrame:
    """Filters for California universities and transforms the data"""
    df = pd.DataFrame(data)
    print(f"Total universities from API: {len(df)}")

    # Filter for California
    df = df[df["name"].str.contains("California", case=False, na=False)]
    print(f"Universities in California: {len(df)}")

    # Convert lists to comma-separated strings
    df['domains'] = df['domains'].apply(lambda x: ','.join(x))
    df['web_pages'] = df['web_pages'].apply(lambda x: ','.join(x))
    df = df.reset_index(drop=True)

    return df[["domains", "country", "web_pages", "name"]]

def load(df: pd.DataFrame) -> None:
    """Loads data into a MySQL database"""
    try:
        # Replace with your own credentials
        user = "root"
        password = "5445"
        host = "localhost"
        port = 3306
        database = "university_db"

        # Create MySQL engine
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

        # Write to MySQL table
        df.to_sql('cal_uni', con=engine, if_exists='replace', index=False)

        print(f"✅ Successfully loaded {len(df)} records into 'cal_uni' table.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")

# Main execution
if __name__ == "__main__":
    data = extract()
    df = transform(data)
    load(df)
