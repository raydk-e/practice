logs = [
    "2026-05-31 12:00:01, INFO, System initialized ",
    "2026-05-31 12:05:23, WARN, High memory usage detected",
    "2026-05-31 12:10:45, INFO, Cron job completed successfully",
    "2026-05-31 12:15:12, ERROR,  Database connection failed   "
]
for log in logs:
    item = log.split(',')
    print(item)
