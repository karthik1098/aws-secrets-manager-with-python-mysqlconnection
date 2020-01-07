import mysql.connector
import config


try:

    connection = mysql.connector.connect(user=config.user,password=config.password,host=config.host,database=config.db)
    print(connection)
    mySql_insert_query = """INSERT INTO details (billamount,serviceQuality,numofpeople)
                            VALUES
                            ('1003', 'good', '60') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into details table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into details table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
    print("MySQL connection is closed")