from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3
from werkzeug.exceptions import InternalServerError
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = 's3cr3t_k3y_123'

# Initialize database
def init_db():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, 
                  username TEXT, 
                  password TEXT,
                  balance INTEGER,
                  is_admin INTEGER)''')
    
    # Insert sample data
    try:
        c.execute("INSERT INTO users VALUES (1000, 'user1', 'weakpass123', 5000000, 0)")
        c.execute("INSERT INTO users VALUES (1001, 'admin', 'super_secure_pass', 999999999, 1)")
    except sqlite3.IntegrityError:
        pass
        
    conn.commit()
    conn.close()

# Vulnerable login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        
        try:
            # Vulnerable SQL query
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            c.execute(query)
            user = c.fetchone()
            
            if user:
                return redirect(url_for('account', user_id=user[0]))
            else:
                # Information disclosure in error message
                raise Exception(f"Login failed for user: {username}")
                
        except Exception as e:
            # Detailed error exposure
            return f"Error: {str(e)}", 500
        finally:
            conn.close()
    
    return render_template('login.html')

# Vulnerable account page
@app.route('/account/<int:user_id>')
def account(user_id):
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    
    # IDOR vulnerability - no ownership check
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    
    if not user:
        return "Account not found", 404
        
    conn.close()
    
    # Admin flag is in the account page
    flag = "CTF_FLAG{1nf0_d1scL0sur3_&_IDOR}" if user[4] == 1 else None
    
    return render_template('account.html', 
                         user=user,
                         flag=flag)

@app.route('/')
def index():
    return redirect(url_for('login'))




@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Create static folder if not exists
    if not os.path.exists('static'):
        os.makedirs('static')
    
    init_db()
    app.run(debug=True)