#sqlite3 interface code using python
import sqlite3
connection = sqlite3.connect("sample.db")
cursor = connection.cursor()
prompt = "sqlite3>"

while True:
	print(prompt, end = " ")
	query = input("")
	if query.lower() == '.quit':
		exit()
	elif query.lower() == '.tables':
		tableList = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
		for tables in tableList:
			print(tables[0], end = " ")

		query = " " 
		'''Even though it is enclosed in try block, it is printing the error.'''

	else:
		while query[-1] != ";":
			query = query + input("     -->")

	try:
		cursor.execute(query) #executes query 

		connection.commit() #commits with database.
		#to print the result
		output = cursor.fetchall()
		for data in output:
			print("")
			for item in data:
				print(item, end = "|")
		print(" ")
	except Exception as e:
		print(e)
		pass
