from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def init_db():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, 'tutors.db')
    schema_path = os.path.join(base_dir, 'schema.sql')
    
    with sqlite3.connect(db_path) as conn:
        with open(schema_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())

init_db()

def get_db_connection():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, 'tutors.db')
    conn = sqlite3.connect(db_path)
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
