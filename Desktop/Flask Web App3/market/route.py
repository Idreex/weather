from market import db, app
from market import bcrypt
from flask import render_template, url_for,redirect, request, flash
from market.model import Item, User
from market.form import Registrationform,Loginform
from flask_login import login_user

@app.route('/', methods=['GET','POST'])
@app.route('/home')
def home():
    
    return render_template('home.html')


@app.route('/market', methods=['GET','POST'])
def market():
       
    items = Item.query.all()
        
    return render_template('market.html', item = items)


@app.route('/login', methods=['GET','POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        # gen_pass_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash(f'Success! You are logged in as: {user.username}', category='success')
            return redirect(url_for('market'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form = form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        # try:
        gen_pass_hash = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
        user_to_create = User(username=form.username.data,
                            email_address=form.email_address.data,
                            password_hash= gen_pass_hash)
        db.session.add(user_to_create)
        db.session.commit()
        flash('Account created successfully', category='success')
        return redirect(url_for('market'))
    # except Exception:
        flash('Username or Password failed', category='danger')
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a {form.username.data}: {str(err_msg)}',category='danger')
    return render_template('register.html', form = form)


# items = Item(id = 1, name='Samsung', price=2134, barcode='012345436', description='about2 Samsung')
# db.session.add(items)
# db.session.commit()  
