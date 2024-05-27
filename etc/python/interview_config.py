# For Production-targeted use, this should be templated, and populated at deployment time.
database = {
    "host": "localhost",
    "dbname": "interview_db",
    "user": "interview_user",
    "password": "interview_pass"
}

# Use this when making connections.
database_dsn = \
    f"host={database['host']} " \
    f"dbname={database['dbname']} " \
    f"user={database['user']} " \
    f"password={database['password']}"
