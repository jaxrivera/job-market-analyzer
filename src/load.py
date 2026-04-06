from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine("sqlite:///jobs.db")
    df.to_sql("jobs", engine, if_exists="replace", index=False)
