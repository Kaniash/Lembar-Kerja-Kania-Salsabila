from flask import Flask, render_template

app = Flask(__name__)

app_name = "My Flask App"  # Variabel global

@app.route("/")
def home():
    return f"Welcome to {app_name}!"  # Menggabungkan kedua fungsi / menjadi satu

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

@app.route('/user/<name>')  # Variabel name diambil dari URL
def user(name):
    return f"Hello, {name}!"


@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)

@app.route('/data')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)

@app.route('/users')
def users():
    user_list = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users.html', users=user_list)

@app.route('/nilai/<int:score>')
def nilai(score):
    return render_template('nilai.html', score=score)

@app.route('/mahasiswa')
def mahasiswa():
    daftar_mahasiswa = [
        {"nama": "Ali", "nilai": 92},
        {"nama": "Budi", "nilai": 80},
        {"nama": "Citra", "nilai": 65},
        {"nama": "Dewi", "nilai": 55},
    ]
    return render_template('mahasiswa.html', mahasiswa=daftar_mahasiswa)

if __name__ == "__main__":
    app.run(debug=False)
