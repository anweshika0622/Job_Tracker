-- Jobs due in next 7 days
SELECT * FROM jobs
WHERE julianday(deadline) - julianday('now') BETWEEN 0 AND 7
ORDER BY deadline ASC;

-- Count of applications per status
SELECT status, COUNT(*) FROM jobs GROUP BY status;
