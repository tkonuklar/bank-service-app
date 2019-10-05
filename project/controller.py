from flask import jsonify
from project import app
from project.models import User

@app.route('/')
def hello():
   return "<h1>Hello World!</h1>"

# user = {'name':'Tugce','pin':12345,'balance':1000}
# users= [{'name':'John Doe','pin':12345,'balance':1000},{'name':'Jane Doe','pin':12346,'balance':2000}]

@app.route('/users')
def getUsers():
   first_user = User.query.first()
   return jsonify(first_user.pin)
