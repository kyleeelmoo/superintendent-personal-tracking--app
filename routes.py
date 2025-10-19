from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import User, WorkOrder, TenantRequest, PartInventory, PartRequest, CleaningTask
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=request.form['username'], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/work_orders')
@login_required
def work_orders():
    orders = WorkOrder.query.all()
    return render_template('work_orders.html', orders=orders)

@app.route('/tenant_requests')
@login_required
def tenant_requests():
    requests = TenantRequest.query.all()
    return render_template('tenant_requests.html', requests=requests)

@app.route('/parts_inventory')
@login_required
def parts_inventory():
    parts = PartInventory.query.all()
    return render_template('parts_inventory.html', parts=parts)

@app.route('/parts_requests')
@login_required
def parts_requests():
    requests = PartRequest.query.all()
    return render_template('parts_requests.html', requests=requests)

@app.route('/cleaning_tasks')
@login_required
def cleaning_tasks():
    tasks = CleaningTask.query.all()
    return render_template('cleaning_tasks.html', tasks=tasks)
