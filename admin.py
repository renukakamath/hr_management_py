from flask import *
from database import *
admin=Blueprint('admin',__name__)



@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')



@admin.route('/admin_manage_client',methods=['get','post'])
def admin_manage_client():
    data={}
    q="select * from client"
    res=select(q)
    data['client']=res
    
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pword=request.form['passw']
        q="insert into login values(null,'%s','%s','client')"%(uname,pword)
        id=insert(q)
        q="insert into client values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('admin.admin_manage_client'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="update":
        q="select * from client where client_id='%s'"%(id)
        res=select(q)
        data['up']=res


    if 'update' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
		
        q="update client set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where client_id='%s'"%(fname,lname,place,phone,email,id)
        update(q)
        flash("UPDATED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_client'))

    if action=="delete":
        q="delete from staff where staff_id='%s'"%(id)
        delete(q)
        flash("DELETED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_client'))

        
    return render_template('admin_manage_client.html',data=data)



@admin.route('/admin_manage_employee',methods=['get','post'])
def admin_manage_employee():
    data={}
    q="select * from employee"
    res=select(q)
    data['emp']=res
    
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        quali=request.form['qualification']
        uname=request.form['uname']
        pword=request.form['passw']
        q="insert into login values(null,'%s','%s','employee')"%(uname,pword)
        id=insert(q)
        q="insert into employee values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email,quali)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('admin.admin_manage_employee'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="update":
        q="select * from employee where employee_id='%s'"%(id)
        res=select(q)
        data['up']=res


    if 'update' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        quali=request.form['qualification']
		
        q="update employee set fname='%s',lname='%s',place='%s',phone='%s',email='%s',qualification='%s' where employee_id='%s'"%(fname,lname,place,phone,email,quali,id)
        update(q)
        flash("UPDATED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_employee'))

    if action=="delete":
        q="delete from employee where employee_id='%s'"%(id)
        delete(q)
        flash("DELETED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_employee'))

        
    return render_template('admin_manage_employee.html',data=data)
    



@admin.route('/admin_manage_department',methods=['get','post'])
def admin_manage_department():
    data={}
    q="select * from department"
    res=select(q)
    data['dept']=res
    
    if 'submit' in request.form:
        dept=request.form['department']
        q="insert into department values(null,'%s')"%(dept)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('admin.admin_manage_department'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="update":
        q="select * from department where department_id='%s'"%(id)
        res=select(q)
        data['up']=res


    if 'update' in request.form:
        dept=request.form['department'] 
        q="update department set department='%s' where department_id='%s'"%(dept,id)
        update(q)
        flash("UPDATED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_department'))

    if action=="delete":
        q="delete from department where department_id='%s'"%(id)
        delete(q)
        flash("DELETED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_department'))

        
    return render_template('admin_manage_department.html',data=data)

       
@admin.route('/admin_view_vaccancy',methods=['get','post'])
def admin_manage_vaccancy():
    data={}
    q="select * from vaccancy"
    res=select(q)
    data['vaccancy']=res
    return render_template("admin_view_vaccancy.html",data=data)



@admin.route('/admin_view_promotion',methods=['get','post'])
def admin_view_promotion():
    data={}
    q="select * from promotion"
    res=select(q)
    data['promo']=res
    return render_template("admin_view_promotion.html",data=data)


@admin.route('/admin_view_trainee_appraisal',methods=['get','post'])
def admin_view_trainee_appraisal():
    data={}
    q="select * from appreciate inner join employee using(employee_id) inner join trainee using(trainee_id)"
    res=select(q)
    data['tr']=res
    return render_template("admin_view_trainee_appraisal.html",data=data)


@admin.route('/admin_send_notification',methods=['get','post'])
def admin_send_notification():
    data={}
    q="select * from notification"
    res=select(q)
    data['noti']=res

    if 'submit' in request.form:
        noti=request.form['notification']
        typ=request.form['type']
        q="insert into notification values(null,'%s','%s')"%(typ,noti)
        insert(q)
        return redirect(url_for('admin.admin_send_notification'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
      
            

    else:
        action=None

    if action=="delete":
        q="delete from notification where notification_id='%s'"%(id)
        delete(q)
        return redirect(url_for('admin.admin_send_notification'))


    return render_template("admin_send_notification.html",data=data)


@admin.route('/admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
    data={}
    q="SELECT * FROM feedback INNER JOIN CLIENT ON feedback.user_id=client.client_id"
    res=select(q)
    data['feed']=res
    return render_template("admin_view_feedback.html",data=data)


@admin.route('/admin_manage_hr',methods=['get','post'])
def admin_manage_hr():
    data={}
    q="select * from hr inner join login using(login_id)"
    res=select(q)
    data['emp']=res
    
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        # desi=request.form['desi']
        quali=request.form['qualification']
        uname=request.form['uname']
        pword=request.form['passw']
        q="insert into login values(null,'%s','%s','hr')"%(uname,pword)
        id=insert(q)
        q="insert into hr values(null,'%s','%s','%s','%s','%s','%s','HR','%s')"%(id,fname,lname,place,phone,email,quali)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('admin.admin_manage_hr'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        lid=request.args['lid']
            

    else:
        action=None

    if action=="update":
        q="select * from hr where hr_id='%s'"%(id)
        res=select(q)
        data['up']=res


    if 'update' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        # desi=request.form['desi']
        quali=request.form['qualification']
        
        q="update hr set fname='%s',lname='%s',place='%s',phone='%s',email='%s',qualification='%s' where hr_id='%s'"%(fname,lname,place,phone,email,quali,id)
        update(q)
        flash("UPDATED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_hr'))

    if action=="delete":
        q="delete from hr where hr_id='%s'"%(id)
        delete(q)
        q="delete from login where login_id='%s'"%(lid)
        delete(q)
        flash("DELETED SUCCESSFULLY")
        return redirect(url_for('admin.admin_manage_hr'))

        
    return render_template('admin_manage_hr.html',data=data)



    



