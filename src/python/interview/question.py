# Third-party libraries.
import psycopg

# Internal libraries.
import interview_config


class Question:

    def foo(self) -> str:
        a = 1
        b = 2
        c = a + b
        return str(c)

    def database_connection(self):
        with psycopg.connect(interview_config.database_dsn) as conn:
            cur = conn.cursor()
            cur.execute("SELECT 1")
            rows = cur.fetchone()[0]
            return rows
