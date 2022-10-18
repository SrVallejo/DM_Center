import settings
import psycopg2

def connect():
    conn = psycopg2.connect(database=settings.DATABASE,
                            user=settings.USER,
                            password=settings.PASSWORD,
                            host=settings.HOST,
                            port=settings.PORT)

    cur = conn.cursor()
    return cur, conn