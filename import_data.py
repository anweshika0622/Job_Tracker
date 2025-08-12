import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../job_tracker.db')
df = pd.read_csv('../data/jobs_sample.csv')
df.to_sql('jobs', engine, if_exists='replace', index=False)
print("Data imported.")
