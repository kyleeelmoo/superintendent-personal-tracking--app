from app import db
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class WorkOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    status = db.Column(db.String(100))

class TenantRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenant_name = db.Column(db.String(150))
    request = db.Column(db.String(500))

class PartInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(150))
    quantity = db.Column(db.Integer)

class PartRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(150))
    requested_by = db.Column(db.String(150))

class CleaningTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)
