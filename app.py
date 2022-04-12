from flask import Flask, render_template,flash, redirect, url_for, session
from forms import Register, Login

app = Flask(__name__)

app.config["SECRET_KEY"] = "537a1b62d2a95fc74624e1db5c24ca78"

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/register')
def registerpage():
    form = Register()
    return render_template('register.html', form = form)


@app.route('/login')
def loginpage():
    form = Login()
    return render_template('login.html', form = form)

@app.route('/blog')
def blogpage():
    return render_template('blog.html')

@app.route('/store')
def storepage():
    return render_template('shop.html')

@app.route('/accountp')
def accountpage():
    return render_template('account.html')

@app.route('/accounts')
def accountpage2():
    return render_template('account2.html')


if __name__ == '__main__':
    app.run(debug=True)
