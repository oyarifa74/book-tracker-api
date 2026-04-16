from app import create_app
import time
import psycopg2
import os

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(os.getenv('DATABASE_URL'))
            conn.close()
            print("✅ Database is ready!")
            break
        except psycopg2.OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(2)

app = create_app()

if __name__ == '__main__':
    wait_for_db()
    app.run(host='0.0.0.0', port=5000, debug=True)