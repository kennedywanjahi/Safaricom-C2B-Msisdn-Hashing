import MySQLdb
import hashlib

# Open database connection #Replace accordingly
DB_HOST = "your_host"
DB_USER = "username"
DB_PASSWORD = "password"
DB_NAME = "database_name"


db = MySQLdb.connect(DB_HOST,DB_USER,DB_PASSWORD,DB_NAME)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Select All records that are missing a msisdn hash #Replace your query based on the table structure
cursor.execute("SELECT msisdn FROM table WHERE msisdn_hash is null")
results = cursor.fetchall()

# qSQL = results[0]

# cursor.execute(qSQL)
for result in results:
    msisdn = result[0]
    string_to_hash = msisdn
    hash_object = hashlib.sha256(str(string_to_hash).encode('utf-8'))
    msisdn_hash = hash_object.hexdigest()
    print("Mobile no is %r Generated hash is  %r " % (msisdn, msisdn_hash))
    #SQL query to INSERT msisdn hashes into the table Profile. #Replace based on table structure
    print("Insering hash for msisdn")
    sql_update_query = """UPDATE table SET msisdn_hash = %s WHERE msisdn = %s"""
    input_data = (str(msisdn_hash), str(msisdn))
    cursor.execute(sql_update_query, input_data)
    db.commit()


# disconnect from server
db.close()