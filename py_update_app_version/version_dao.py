#!/usr/bin/python3
#_*_ coding:utf-8_*_
'''
Create by 2018.11.13
@author:Marco.Chi
'''
import cx_Oracle

class Connect():

	def __init__(self):
		print("self")

	def getVersion():
		username = "dlm_iconn"
		userpwd = "dlm_iconn"
		host="172.16.1.85"
		port=1521
		dbname="iconnd"

		dsn=cx_Oracle.makedsn(host, port, dbname)
		connection=cx_Oracle.connect(username, userpwd, dsn) 
		cursor = connection.cursor() 
		sql = "select configuration_value v from SYSTEM_CONFIGURATION where CONFIGURATION_KEY = 'APP_ANDROID_LOWEST_VERSION' ";
		cursor.execute(sql)
		result = cursor.fetchone()
		print(result)
		cursor.close()
		connection.close()
		return result;

	def updateVersion(newVersion):
		print("v_v:" + newVersion);
		if newVersion.strip() != '':
			username = "dlm_iconn"
			userpwd = "dlm_iconn"
			host="172.16.1.85"
			port=1521
			dbname="iconnd"

			dsn=cx_Oracle.makedsn(host, port, dbname)
			connection=cx_Oracle.connect(username, userpwd, dsn) 
			cursor = connection.cursor() 
			sql = "update SYSTEM_CONFIGURATION set configuration_value = '"+newVersion+ "' where CONFIGURATION_KEY = 'APP_ANDROID_LOWEST_VERSION' ";
			print (sql)
			try:
				cursor.execute(sql)
				connection.commit()
			except Exception as err:
				print(err)
				connection.rollback()
			cursor.close()
			connection.close()