from src.extract import fetch_jobs
from src.transform import clean_data
from src.load import load_data

def run_pipeline():
    jobs = fetch_jobs()
    df = clean_data(jobs)
    load_data(df)
    print("Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()
