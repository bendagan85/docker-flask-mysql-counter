from flask import Flask, render_template
import os
import pymysql

app = Flask(__name__)

# Read DB config from environment variables (Docker Compose will supply them)
db_host = os.getenv("DB_HOST", "db")
db_port = int(os.getenv("DB_PORT", 3306))
db_name = os.getenv("DB_NAME", "mydb")
db_user = os.getenv("DB_USER", "myuser")
db_password = os.getenv("DB_PASSWORD", "mypassword")

# Create a MySQL connection
db_conn = pymysql.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name,
    autocommit=False
)

@app.route('/')
def index():
    with db_conn.cursor() as cursor:
        # Insert first value or increase existing counter
        cursor.execute("""
            INSERT INTO page_counter (id, count)
            VALUES (1, 1)
            ON DUPLICATE KEY UPDATE count = count + 1;
        """)

        # Read updated value
        cursor.execute("SELECT count FROM page_counter WHERE id = 1;")
        row = cursor.fetchone()
        page_count = row[0]

    db_conn.commit()
    return render_template('index.html', page_count=page_count)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

