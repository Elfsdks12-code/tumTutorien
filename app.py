from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('tutors.db')
    conn.row_factory = sqlite3.Row 
    return conn
@app.route('/')
def index():
    conn = get_db_connection()
    tutors = conn.execute('SELECT * FROM tutoriums').fetchall()
    conn.close()
    return render_template('index.html', tutors = tutors)

if __name__ == '__main__':
    app.run(debug=True, port=5002)