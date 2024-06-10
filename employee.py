from flask import *
from database import *
import uuid
employee=Blueprint('employee',__name__)



@employee.route('/employeehome')
def employeehome():
	return render_template('employeehome.html')

@employee.route('/employee_view_trainee',methods=['get','post'])
def employee_view_trainee():
    data={}
    q="select * from trainee"
    res=select(q)
    data['tr']=res
    return render_template('employee_view_trainee.html',data=data)



@employee.route('/employee_send_material',methods=['get','post'])
def employee_send_material():
    data={}
    q="select * from material inner join trainee using(trainee_id)"
    res=select(q)
    data['mat']=res

    q="select * from trainee"
    res=select(q)
    data['tr']=res

    if 'submit' in request.form:
        trainee=request.form['trainee']
        i=request.files['material']
        img='static/'+str(uuid.uuid4())+i.filename
        i.save(img)
        q="insert into material values(null,'%s','%s',curdate())"%(trainee,img)
        insert(q)
        return redirect(url_for('employee.employee_send_material'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
      
            

    else:
        action=None

    if action=="delete":
        q="delete from material where material_id='%s'"%(id)
        delete(q)
        return redirect(url_for('trainee.trainee_send_material'))


    return render_template("employee_send_material.html",data=data)


@employee.route('/employee_view_appraisal',methods=['get','post'])
def employee_view_appraisal():
    data={}
    q="select * from appreciate inner join employee using(employee_id) inner join trainee using(trainee_id) "
    res=select(q)
    data['tr']=res
    return render_template("employee_view_appraisal.html",data=data)


@employee.route('/employee_view_dailyreport',methods=['get','post'])
def employee_view_dailyreport():
    data={}
    q="select * from report inner join trainee using(trainee_id)"
    res=select(q)
    data['tr']=res
    return render_template("employee_view_dailyreport.html",data=data)



