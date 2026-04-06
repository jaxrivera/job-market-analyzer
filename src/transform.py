import pandas as pd

def clean_data(jobs):
    df = pd.DataFrame(jobs)

    df = df[[
        "title",
        "company_name",
        "candidate_required_location",
        "publication_date",
        "salary",
        "description"
    ]]

    df["avg_salary"] = df["salary"].str.extract(r'(\d+)')
    df["avg_salary"] = pd.to_numeric(df["avg_salary"], errors="coerce")

    return df
