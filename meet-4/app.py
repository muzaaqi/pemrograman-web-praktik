from flask import Flask, render_template, session, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'HSAIJWEHRIUHIUFGF92165009DIUFGIFSFG989234R440837047IDSAFF892'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form:
        email = request.form['inpEmail']
        passwd = request.form['inpPass']
        
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM users WHERE email = %s AND password = %s''', (email, passwd))
        
        data = cur.fetchone()
        
        if data:
            session['is_logged_in'] = True
            session['username'] = data[1]
            
            return redirect(url_for('home'))
        
        else:
            return render_template('login.html', error='Invalid email or password')
    
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'inpUsername' in request.form and 'inpEmail' in request.form and 'inpPass' in request.form:
        username = request.form['inpUsername']
        email = request.form['inpEmail']
        passwd = request.form['inpPass']
        
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO users (username, email, password) VALUES (%s, %s, %s)''', (username, email, passwd))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/home')
def home():
    if 'is_logged_in' in session:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM users''')
        
        data = cur.fetchall()
        
        return render_template('home.html', users=data)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('is_logged_in', None)
    session.pop('username', None)
    
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)