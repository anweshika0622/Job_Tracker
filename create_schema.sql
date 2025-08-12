CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    position TEXT,
    status TEXT,
    applied_date TEXT,
    deadline TEXT,
    resume_version TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS resumes (
    version_name TEXT PRIMARY KEY,
    file_path TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS interview_qa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    question TEXT,
    answer TEXT,
    topic TEXT
);
