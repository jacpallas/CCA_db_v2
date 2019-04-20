import pymysql


def verf():
	#windows
	'''
	mydb = pymysql.connect(
  host="localhost",user="root",
  passwd="cocojj12",db="access_db")
	'''
	

	#mac
	
	
	mydb = pymysql.connect(
	  host="localhost",port=8889,user="root",
	  passwd="root",db="access_db")
	
	
	miCursor=mydb.cursor()

	return mydb, miCursor

	
verf()


