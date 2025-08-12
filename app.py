import streamlit as st
import pandas as pd
import sqlite3

st.title("🎯 Job Tracker & Interview Readiness System")

conn = sqlite3.connect('../job_tracker.db')
df_jobs = pd.read_sql("SELECT * FROM jobs", conn)
df_qa = pd.read_sql("SELECT * FROM interview_qa", conn)

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Job Tracker", "Interview Q&A"])

if page == "Job Tracker":
    st.subheader("🗃️ All Jobs")
    st.dataframe(df_jobs)

    st.subheader("📅 Upcoming Deadlines")
    df_jobs['deadline'] = pd.to_datetime(df_jobs['deadline'])
    upcoming = df_jobs[df_jobs['deadline'] <= pd.Timestamp.now() + pd.Timedelta(days=7)]
    st.table(upcoming[['company', 'position', 'deadline']])

elif page == "Interview Q&A":
    st.subheader("❓ Interview Question Vault")
    st.dataframe(df_qa)
