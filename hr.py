from flask import *
from database import *
hr=Blueprint('hr',__name__)

@hr.route('/hrhome')
def hrhome():
	return render_template('hrhome.html')


@hr.route('/hr_manage_vaccancy',methods=['get','post'])
def hr_manage_vaccancy():
    data={}
    q="select * from vaccancy inner join department using(department_id)"
    res=select(q)
    data['vaccancy']=res
    q="select * from department"
    res=select(q)
    data['dept']=res
    
    if 'submit' in request.form:
        dept=request.form['dept']
        vaccancy=request.form['vaccancy']
        detials=request.form['details']
        q="insert into vaccancy values(null,'%s','%s','%s',curdate())"%(dept,vaccancy,detials)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('hr.hr_manage_vaccancy'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="update":
        q="select * from vaccancy where vaccancy_id='%s'"%(id)
        res=select(q)
        data['up']=res


    if 'update' in request.form:
        dept=request.form['dept']
        vaccancy=request.form['vaccancy']
        detials=request.form['details']
        q="update vaccancy set vaccancy='%s',details='%s' where vaccancy_id='%s'"%(vaccancy,detials,id)
        update(q)
        flash("UPDATED SUCCESSFULLY")
        return redirect(url_for('hr.hr_manage_vaccancy'))

    if action=="delete":
        q="delete from vaccancy where vaccancy_id='%s'"%(id)
        delete(q)
        flash("DELETED SUCCESSFULLY")
        return redirect(url_for('hr.hr_manage_vaccancy'))

    return render_template("hr_manage_vaccany.html",data=data)



# @hr.route('/hr_view_trainee',methods=['get','post'])
# def hr_view_trainee():
#     data={}
#     q="select * from vaccancy"
#     res=select(q)
#     data['dept']=res
#     return render_template('hr_view_trainee.html',data=data)



@hr.route('/hr_send_promotion',methods=['get','post'])
def hr_send_promotion():
    data={}
    q="select * from promotion"
    res=select(q)
    data['promo']=res
    
    if 'submit' in request.form:
        
        promotion=request.form['promo']
        q="insert into promotion values(null,'%s')"%(promotion)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('hr.hr_send_promotion'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="delete":
        q="delete from promotion where promotion_id='%s'"%(id)
        delete(q)
       	flash("deleted successfully")
        return redirect(url_for('hr.hr_send_promotion'))

    return render_template('hr_send_promotion.html',data=data)


@hr.route('/hr_trainee_appraisal',methods=['get','post'])
def hr_trainee_appraisal():
    data={}
    q="select * from appreciate inner join employee using(employee_id) inner join trainee using(trainee_id)"
    res=select(q)
    data['app']=res

    q="select * from trainee"
    res=select(q)
    data['tr']=res
    
    q="select * from employee"
    res=select(q)
    data['emp']=res


    if 'submit' in request.form:
        
        tr=request.form['trainee']
        emp=request.form['employee']
        details=request.form['details']
        q="insert into appreciate values(null,'%s','%s','%s')"%(tr,emp,details)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('hr.hr_trainee_appraisal'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="delete":
        q="delete from appreciate where appreciate_id='%s'"%(id)
        delete(q)
       	flash("deleted successfully")
        return redirect(url_for('hr.hr_trainee_appraisal'))

    return render_template('hr_trainee_appraisal.html',data=data)


@hr.route('/hr_manage_trainee',methods=['get','post'])
def hr_manage_trainee():
    data={}
    q="select * from trainee"
    res=select(q)
    data['tr']=res
    
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        quali=request.form['qualification']
        uname=request.form['uname']
        pword=request.form['passw']
        q="insert into login values(null,'%s','%s','trainee')"%(uname,pword)
        id=insert(q)
        q="insert into trainee values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email,quali)
        insert(q)
        flash('inserted successfully')
        return redirect(url_for('hr.hr_manage_trainee'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
            

    else:
        action=None

    if action=="update":
        q="select * from trainee where trainee_id='%s'"%(id)
        res=select(q)
        data['up']=res


    if 'update' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        quali=request.form['qualification']
        
        q="update trainee set fname='%s',lname='%s',place='%s',phone='%s',email='%s',qualification='%s' where trainee_id='%s'"%(fname,lname,place,phone,email,quali,id)
        update(q)
        flash("UPDATED SUCCESSFULLY")
        return redirect(url_for('hr.hr_manage_trainee'))

    if action=="delete":
        q="delete from trainee where trainee_id='%s'"%(id)
        delete(q)
        flash("DELETED SUCCESSFULLY")
        return redirect(url_for('hr.admin_manage_employee'))

        
    return render_template('hr_manage_trainee.html',data=data)


@hr.route('/hr_send_notification',methods=['get','post'])
def hr_send_notification():
    data={}
    q="select * from notification"
    res=select(q)
    data['noti']=res

    if 'submit' in request.form:
        noti=request.form['notification']
        q="insert into notification values(null,'%s')"%(noti)
        insert(q)
        return redirect(url_for('hr.hr_send_notification'))


    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
      
    else:
        action=None

    if action=="delete":
        q="delete from notification where notification_id='%s'"%(id)
        delete(q)
        return redirect(url_for('hr.hr_send_notification'))

    return render_template("hr_send_notification.html",data=data)


@hr.route('/hr_view_queries',methods=['get','post'])
def hr_view_queries():
    data={}
    q="select * from query"
    res=select(q)
    data['query']=res

    
    return render_template("hr_view_query.html",data=data)



@hr.route('/hr_view_feedback',methods=['get','post'])
def hr_view_feedback():
    data={}
    q="SELECT * FROM feedback INNER JOIN CLIENT ON feedback.user_id=client.client_id"
    res=select(q)
    data['feed']=res
    return render_template("hr_view_feedback.html",data=data)

