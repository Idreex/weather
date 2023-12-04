from market import db, app
from market import bcrypt
from flask import render_template, url_for,redirect, request, flash
from market.model import Item, User
from market.form import Registrationform, Loginform, PurchaseForm
from flask_login import login_user, login_required, current_user,logout_user

class Transaction(Exception):
    pass


@app.route('/', methods=['GET','POST'])
@app.route('/home')
@login_required
def home():
    
    return render_template('home.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out', 'info')
    return redirect(url_for('login'))



@app.route('/market', methods=['GET','POST'])
@login_required
def market():

    form = PurchaseForm()
    items = Item.query.all()

    item_name = request.form.get('purchase')
    if request.method == 'POST':
        bought_item = Item.query.filter_by(name=item_name).first()
        if bought_item:
            bought_item.owner = current_user.id 
            if current_user.can_purchase(bought_item):
                bought_item.buy(current_user)
            flash('Thanks for your patronage', category='success')
            return redirect(url_for('market'))

    if request.method == 'GET':
        items = Item.query.all()
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items = items, form = form, owned_items = owned_items)

@app.route('/login', methods=['GET','POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
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
        gen_pass_hash = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
        user = User(username=form.username.data,
                            email_address=form.email_address.data,
                            password_hash= gen_pass_hash)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', category='success')
        login_user(user)
        flash('logged in successfully', category='info')
        return redirect(url_for('market'))
    
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a {form.username.data}: {str(err_msg)}',category='danger')
    return render_template('register.html', form = form)

