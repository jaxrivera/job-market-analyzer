import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("Job Market Analyzer")

try:
    engine = create_engine("sqlite:///jobs.db")
    df = pd.read_sql("SELECT * FROM jobs", engine)

    if df.empty:
        st.warning("No data found. Run pipeline first.")
    else:
        st.subheader("Top Locations")
        st.bar_chart(df["candidate_required_location"].value_counts().head(10))

        st.subheader("Salary Distribution")
        st.line_chart(df["avg_salary"])

except Exception as e:
    st.error(f"Error: {e}")
