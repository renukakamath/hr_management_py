from flask import *
from database import *
trainee=Blueprint('trainee',__name__)



@trainee.route('/traineehome')
def traineehome():
	return render_template('traineehome.html')


@trainee.route('/trainee_send_dailyreport',methods=['get','post'])
def trainee_send_dailyreport():
    data={}
    q="select * from report"
    res=select(q)
    data['report']=res

    if 'submit' in request.form:
        noti=request.form['report']
        q="insert into report values(null,'%s','%s')"%(session['trainee_id'],noti)
        insert(q)
        return redirect(url_for('trainee.trainee_send_dailyreport'))


    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
      
    else:
        action=None

    if action=="delete":
        q="delete from report where report_id='%s'"%(id)
        delete(q)
        return redirect(url_for('trainee.trainee_send_dailyreport'))

    return render_template("trainee_send_dailyreport.html",data=data)




@trainee.route('/trainee_send_query',methods=['get','post'])
def trainee_send_query():
    data={}
    q="select * from query"
    res=select(q)
    data['query']=res

    if 'submit' in request.form:
        noti=request.form['query']
        q="insert into query values(null,'%s','%s',curdate(),'pending')"%(session['trainee_id'],noti)
        insert(q)
        return redirect(url_for('trainee.trainee_send_query'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
      
            

    else:
        action=None

    if action=="delete":
        q="delete from query where query_id='%s'"%(id)
        delete(q)
        return redirect(url_for('trainee.trainee_send_query'))


    return render_template("trainee_send_query.html",data=data)





@trainee.route('/trainee_view_notification',methods=['get','post'])
def trainee_view_notification():
    data={}
    q="SELECT * FROM notification "
    res=select(q)
    data['feed']=res
    return render_template("trainee_view_notification.html",data=data)




@trainee.route('/trainee_send_feedback',methods=['get','post'])
def trainee_send_feedback():
    data={}
    q="select * from feedback"
    res=select(q)
    data['feedback']=res

    if 'submit' in request.form:
        noti=request.form['feedback']
        q="insert into feedback values(null,'%s','%s',curdate())"%(session['trainee_id'],noti)
        insert(q)
        return redirect(url_for('trainee.trainee_send_feedback'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
      
            

    else:
        action=None

    if action=="delete":
        q="delete from feedback where feedback_id='%s'"%(id)
        delete(q)
        return redirect(url_for('trainee.trainee_send_feedback'))


    return render_template("trainee_send_feedback.html",data=data)



@trainee.route('/trainee_download_material',methods=['get','post'])
def trainee_download_material():
    data={}
    q="SELECT * FROM material where trainee_id='%s'"%(session['trainee_id'])
    res=select(q)
    data['material']=res

    
    return render_template("trainee_download_material.html",data=data)
