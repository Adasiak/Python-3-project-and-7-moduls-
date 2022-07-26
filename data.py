import csv
from lib import *
import mysql.connector

clearConsole()

with mysql.connector.connect(username='sql11508308', password='eg7lBrNj1q', host="sql11.freemysqlhosting.net", database='sql11508308') as connection:
    cursor = connection.cursor()


    with open("cities.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            try:
                previous_position = int(row["2021"])
            except:
                previous_position = 0

            sql = f"""INSERT INTO 
            city(name,country,position,previous_position)
            VALUES("{row["City"]}","{row["Country"]}", {int(row["2022"])},{previous_position} )
            """
            cursor.execute(sql)

        connection.commit()
