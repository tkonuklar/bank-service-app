from project import db

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), unique=True)
   pin= db.Column(db.Integer, nullable=False)
   balance = db.Column(db.Integer, default=0)

   def __repr__(self):
      return f"User(id={self.id}, name='{self.name}' , pin='{self.pin}', balance='{self.balance}')"
