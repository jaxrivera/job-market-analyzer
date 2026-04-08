# 📊 Job Market Analyzer

An end-to-end data analysis project that extracts, processes, and visualizes job market data to uncover hiring trends, geographic demand, and top companies.

---

## 🚀 Overview

The Job Market Analyzer is a Python-based ETL and analytics pipeline designed to simulate real-world data workflows. It ingests job listing data, transforms it into structured formats, and presents insights through an interactive dashboard.

This project demonstrates core data engineering concepts including data ingestion, transformation, storage, and visualization.

---

## 🧠 Features

- Data extraction from job listing sources  
- Data cleaning and transformation using Pandas  
- Structured storage using SQLite and SQLAlchemy  
- Interactive BI dashboard built with Streamlit  
- Visualizations for:
  - Job distribution by location  
  - Top hiring companies  
  - Raw data exploration  

---

## 🏗️ Project Structure

```
job-market-analyzer/
│
├── src/                # ETL pipeline scripts
│   └── pipeline.py
│
├── dashboard/          # Streamlit dashboard
│   └── app.py
│
├── jobs.db             # SQLite database (generated)
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- SQLite  
- SQLAlchemy  
- Streamlit  
- Matplotlib  

---

## 🔄 Data Pipeline

1. **Extract**  
   Fetch job listing data from an API or dataset  

2. **Transform**  
   Clean and structure data using Pandas  
   - Handle missing values  
   - Normalize fields  
   - Prepare for analysis  

3. **Load**  
   Store processed data into SQLite using SQLAlchemy  

4. **Visualize**  
   Display insights through a Streamlit dashboard  

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jaxrivera/job-market-analyzer.git
cd job-market-analyzer
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run ETL pipeline

```bash
python src/pipeline.py
```

### 5. Launch dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📊 Example Insights

- Distribution of remote vs location-based jobs  
- Top companies hiring across regions  
- Trends in job posting frequency  

---

## ⚠️ Challenges & Learnings

- Handling missing and inconsistent data formats  
- Designing a clean ETL workflow structure  
- Integrating SQLAlchemy with Pandas pipelines  
- Building a lightweight BI dashboard with Streamlit  

---

## 🚀 Future Improvements

- Add real-time data ingestion  
- Integrate cloud storage (AWS S3)  
- Upgrade database to PostgreSQL or Snowflake  
- Add advanced analytics (salary trends, skill extraction)  
- Deploy dashboard for public access  

---

## 💼 Why This Project Matters

This project demonstrates:
- End-to-end data pipeline design  
- Data transformation and modeling  
- Database integration  
- BI dashboard development  

It reflects real-world workflows used in data engineering and analytics roles.

---

## 📬 Contact

**Jonatan A. Rivera**  
GitHub: https://github.com/jaxrivera  

