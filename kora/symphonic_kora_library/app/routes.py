from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .config import create_connection
from .models import create_tables

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # A secret password to keep our playground safe

# Start playing by setting up the big toy box
conn = create_connection()
create_tables(conn)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            return "Login failed!"

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = create_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        cursor.execute("INSERT INTO playlists (user_id, name, description) VALUES (%s, %s, %s)", (session['user_id'], name, description))
        conn.commit()

    cursor.execute("SELECT * FROM playlists WHERE user_id = %s", (session['user_id'],))
    playlists = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('dashboard.html', playlists=playlists)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
