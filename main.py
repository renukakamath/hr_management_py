from flask import Flask
from public import public
from admin import admin
from hr import hr
from employee import employee
from trainee import trainee



app=Flask(__name__)
app.secret_key='hellooo'
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(hr,url_prefix='/hr')
app.register_blueprint(employee,url_prefix='/employee')
app.register_blueprint(trainee,url_prefix='/trainee')





app.run(debug=True,port=5407)