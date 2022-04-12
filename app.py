
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template,flash, redirect, url_for, session
from forms import Register, Login
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import pymysql.cursors
import pymysql

app = Flask(__name__)

'''app.config['MYSQL_HOST'] = 'JustV.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'JustV'
app.config['MYSQL_PASSWORD'] = 'Password852'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)'''
app.config['SQLALCHEMY_DATABASE_URI']='mysql://JustV:Password852@JustV.mysql.pythonanywhere-services.com/JustV$default'

app.config["SECRET_KEY"] = "537a1b62d2a95fc74624e1db5c24ca78"
db= SQLAlchemy(app)


#Model
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

#Model
class Store(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    item=db.Column(db.String(200), nullable=False)
    description=db.Column(db.String(200), nullable=False, unique=True)
    price=db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

#Model
class Blog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    comment=db.Column(db.String(120), nullable=False, unique=True)
    username=db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

#Model
class Images(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    link=db.Column(db.String(200), nullable=False)
    username=db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/', methods=["GET","POST"])
def home():
    image= Images.query
    return render_template('main.html', image=image)

@app.route('/register', methods=["GET","POST"])
def registerpage():
    form = Register()
    name = None
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            name = form.username.data
            form.username.data = ''
            form.email.data = ''
            flash(name)
    our_users= Users.query
    return render_template('register.html', form = form, name=name, our_users=our_users)


@app.route('/login', methods=["GET","POST"])
def loginpage():
    form = Login()

    return render_template('login.html', form = form)

@app.route('/blog', methods=["GET","POST"])
def blogpage():
    blog = Blog.query
    return render_template('blog.html', blog=blog)

@app.route('/store', methods=["GET","POST"])
def storepage():
    store = Store.query
    return render_template('shop.html', store=store)

@app.route('/accountp', methods=["GET","POST"])
def accountpage():
    return render_template('account.html')

@app.route('/accounts', methods=["GET","POST"])
def accountpage2():
    return render_template('account2.html')


if __name__ == '__main__':
    app.run(debug=True)
