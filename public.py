from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('publichome.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['uname']
		password=request.form['pword']
		
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			lid=session['lid']
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))


			elif res[0]['usertype']=='hr':
				q="select * from hr where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['hr_id']=res[0]['hr_id']	
				return redirect(url_for('hr.hrhome'))


			elif res[0]['usertype']=='employee':
				q="select * from employee where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['employee_id']=res[0]['employee_id']
				return redirect(url_for('employee.employeehome'))

			elif res[0]['usertype']=='client':
				q="select * from client where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['client_id']=res[0]['client_id']
				return redirect(url_for('client_id.clienthome'))

			elif res[0]['usertype']=='trainee':
				q="select * from trainee where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['trainee_id']=res[0]['trainee_id']
				return redirect(url_for('trainee.traineehome'))

		return redirect(url_for('public.login'))

	return render_template('login.html')

