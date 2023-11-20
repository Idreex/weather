from market import db
    
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=50), nullable=False, unique=True)
    description = db.Column(db.String(length=100), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    
    def __repr__(self):
        return f'Items {self.name}'
    

    
class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),index=False,unique=True,nullable=False)
    email = db.Column(db.String(80),index=True,unique=True,nullable=False)
    created = db.Column(db.DateTime,index=False,unique=False,nullable=False)
    password_hash = db.Column(db.String(60),nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    
    def __repr__(self):
        return f'Users {self.username}'
