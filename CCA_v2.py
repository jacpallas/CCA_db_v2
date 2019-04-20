from flask import Flask, render_template, request, url_for, redirect, session, flash
from passlib.hash import sha256_crypt
from db_login import verf
from database import query, query_manual
from functools import wraps
from forms import ContactForm
from flask_mail import Message, Mail

import os

mail=Mail()

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jacpallaswebmaster@gmail.com'
app.config["MAIL_PASSWORD"] = 'Marin36900'

mail.init_app(app)


def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Debes loguearte primero')
			return redirect(url_for('index'))
	return wrap

@app.route('/logout/')
@login_required
def logout():
	session.clear()
	flash(' Has salido')
	return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')



@app.route("/login", methods=["POST", "GET"])
def login():

	#try:
	mydb, miCursor=verf()
	data=""

	if request.method=="POST":
		
		#ojo. La tabla se llama data_users. Cambiar para que funcione en win.Para mac es data.
		data=miCursor.execute("SELECT * FROM data_users WHERE user_n=(%s)",
		(request.form["user"]))


		if data!=0:


			data=sha256_crypt.hash(miCursor.fetchone()[1])

			miCursor.execute("SELECT * FROM data_users WHERE user_n=(%s)",
		(request.form["user"]))
			user_login=miCursor.fetchone()[2]

			
			mydb.close() 

			#comparamos la clave encriptada de la bbdd-->(data) 
			#con la clave introducida en el formulario
			#Este medodo devuelve True or False			
			if sha256_crypt.verify(request.form["key"], data):

				session['logged_in']=True
				session['username']=user_login

				flash("Estás logueado")

				resultado=("YES")
				return redirect(url_for('home'))

			else:
				flash("User name or password incorrect. Please try again.")
				
				return render_template("index.html")

		else:
			flash("User name or password invalid. Try again.")
			
			return render_template("index.html")	

	'''except Exception:
		
		mydb.close() 
		resultado="Ha ocurrido un error en la base de datos"
		return render_template("index.html",data=data,resultado=resultado)'''
	

@app.route('/home')
@login_required
def home():
	return render_template('home.html')


@app.route('/tree/')
@login_required
def tree():
	return render_template('tree.html')



@app.route('/checkbox/',methods=["POST"])
@login_required
def checkbox():

	check_req=request.form.getlist('req')
	check_market=request.form.getlist('market')
	check_req_chem=request.form.getlist('req_chem')
	
	if check_req==[] and check_req_chem==[]:
		
		flash(' At least one requirement must be selected.')
		return redirect(url_for('db'))

	elif  check_market==[]:
		flash(' At least one market must be selected.')
		return redirect(url_for('db'))

	else:
		#check_req.extend(check_req_chem)
		
		boxMsg_chem=query(check_req_chem,check_market)
		boxMsg_fisic=query(check_req,check_market)
		

		#from database import query_manual_new
		

		return render_template('db.html',boxMsg_chem=boxMsg_chem,boxMsg_fisic=boxMsg_fisic,
		 check_req=check_req,check_market=check_market, check_req_chem=check_req_chem)


@app.route('/glossary/')
@login_required
def glossary():

	return render_template('glossary.html')

@app.route('/db/')
def db():
	section=request.path
	return render_template('db.html')


@app.route('/contact1', methods=['GET', 'POST'])
@login_required
def contact1():

	form = ContactForm()
 
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact1.html', form=form)
		else:
			msg = Message(form.subject.data, sender='jacpallaswebmaster@gmail.com', recipients=['jacoborodriguezpallas@gmail.com'])
			msg.body = """
			From: %s <%s>
			Subject: %s

%s
			""" % (form.name.data, form.email.data,form.subject.data ,form.message.data)
			mail.send(msg)

			return render_template('contact1.html', success=True)
	elif request.method == 'GET':
		return render_template('contact1.html', form=form)


	'''if request.method == 'POST':

		name_mail=request.form['inputName']
		mail_mail=request.form['inputEmail']
		subject_mail=request.form['inputSubject']
		msg_mail=request.form['inputMsg']
		msg = Message(subject_mail, sender="jacpallaswebmaster@gmail.com", recipients=['jacoborodriguezpallas@gmail.com'])
		msg.body = "From: %s <%s> %s %s" %(name_mail, mail_mail,subject_mail ,msg_mail)
				
		mail.send(msg)

		return 'Form posted.'

		return render_template('contact.html', n=name_mail, m=mail_mail, s=subject_mail,ms=msg_mail)

	elif request.method == 'GET':
		return render_template('contact.html')

	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form=form)

		else:
			name_mail=request.form('inputName')
			mail_mail=request.form('inputEmail')
			subject_mail=request.form('inputSubject')
			msg = Message(subject_mail, sender="jacpallaswebmaster@gmail.com", recipients=['jacoborodriguezpallas@gmail.com'])
			msg.body = "From: %s <%s> %s %s" %(name_mail, mail_mail,subject_mail ,request.form('inputMsg'))
			
			mail.send(msg)

			return 'Form posted.'
	elif request.method == 'GET':
		return render_template('contact.html', form=form)'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001', debug=True)


