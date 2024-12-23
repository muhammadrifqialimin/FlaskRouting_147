from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Logika autentikasi sederhana (ganti dengan logika yang sesuai)
    if username == 'rifqi' and password == '1234':
        return f'welcome, {username}!.'
    else:
        return "Login Gagal! Coba lagi."

if __name__ == '__main__':
    app.run(debug=True)