from market import db, app
from flask import render_template, url_for,redirect
from market.model import Item, User
from market.form import Registration


@app.route('/', methods= ['POST','GET'])
@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/market', methods=['GET'])
def market():
       
    items = Item.query.all()
        
    return render_template('market.html', item = items)


@app.route('/login', methods=['GET'])
def login():
    
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, 
                    password_hash = form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('market'))

    return render_template('register.html', form = form)


# items = Item(id = 1, name='Samsung', price=2134, barcode='012345436', description='about2 Samsung')
# db.session.add(items)
# db.session.commit()  
