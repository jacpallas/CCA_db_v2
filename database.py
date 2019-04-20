import pymysql

query_manual=[]

def crear():

	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="ods_db")

	miCursor=mydb.cursor() #Creando el cursor o puntero

	miCursor.execute('''CREATE TABLE HOJA1
	 (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	 FECHA VARCHAR UNIQUE, 
	 MANUAL INTEGER,
	 OBSERVATORIO INTEGER,
	 CONSULTA INTEGER, 
	 ACTUALIZACION INTEGER,
	 OTROS INTEGER)''')
	  #Esto Crea una tabla con las siguiente columnas

	mydb.commit() 
	mydb.close() 

def anadir(fecha,manual,observatorio,consulta,actualizacion,otros):

	total=(fecha,manual,observatorio,consulta,actualizacion,otros)

	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="ods_db")

	miCursor=mydb.cursor()

	
	insertar=('''INSERT INTO HOJA1 (fecha,manual,
		observatorio,consulta,actualizacion,otros)
		VALUES(%s,%s,%s,%s,%s,%s)''')
			#Esto introduce nuevos datos en la tabla determinada
			# y columnas especificadas
	miCursor.execute(insertar,total)
	
	mydb.commit() 
	mydb.close() 



def promedio():

	global lista
	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="ods_db")

	miCursor=mydb.cursor()


	miCursor.execute('''SELECT ROUND(AVG(MANUAL),2), 
		ROUND(AVG (OBSERVATORIO),2), 
		ROUND(AVG(CONSULTA),2),ROUND(AVG(ACTUALIZACION),2), 
	 	ROUND(AVG(OTROS),2) FROM HOJA1''')
		
	lista=miCursor.fetchall()
	

	mydb.commit() 
	mydb.close() 

def datalist():
	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="ods_db")

	miCursor=mydb.cursor()

	miCursor.execute('''SELECT FECHA , MANUAL,
	 OBSERVATORIO, CONSULTA,ACTUALIZACION ,
	 OTROS FROM HOJA1 ORDER BY FECHA DESC''')
	global lista_completa
	lista_completa=miCursor.fetchall()


	mydb.commit() 
	mydb.close() 


def query(query_box,query_market):
	
	#windows
	'''
	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="ods_db")
  '''
  
	#mac
	
	mydb = pymysql.connect(
	  host="localhost",port=8889,user="root",
	  passwd="root",db="ods_db")
	
	
	miCursor=mydb.cursor()


	#global query_manual_new
	
	query_manual_new=[]
	

	for i in query_box:
		query_manual=[]
		query_manual_new.append(query_manual)
		
		
		for n in query_market:

			miCursor.execute('''SELECT * FROM {}
			 WHERE ID_MARKET={}'''.format(i,n))
					
			seleccion=miCursor.fetchall()

			query_manual.extend(seleccion)
	return query_manual_new
	print (query_manual_new)

	mydb.commit() 
	mydb.close() 
	


def qu():
	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="ods_db")

	miCursor=mydb.cursor()


	miCursor.execute('''SELECT TEXTO FROM REQ01
			 WHERE ID_MARKET="2"''')
					
	seleccion=miCursor.fetchall()

	for i in seleccion:
		print(i)		

	mydb.commit() 
	mydb.close() 


print(query(["al"],["1"]))

