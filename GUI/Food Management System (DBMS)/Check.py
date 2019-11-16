import pymysql.cursors
connection = pymysql.connect(host='localhost',user='root',password='WeRock',db='foodchainmanagement',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
print ("Connected Successful!!")

try: 
    with connection.cursor() as cursor:
        sql = "SELECT Name,Mobile,State,City,Pincode FROM Farmer"
        cursor.execute(sql)
        print ("cursor.description: ", cursor.description)
        print()
        for row in cursor:
            print(row)
             
finally:
    connection.close()