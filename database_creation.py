import mysql.connector

# For Windows
# pip install mysql-connector-python
# pip install mysql-connector

# For Mac
# pip3 install mysql-connector
# pip3 install mysql-connector-python

db = mysql.connector.connect(
    host="localhost",
    user="root", # Change if necessary
    passwd="root", # Change if necessary
    # database="libraryproject" # Uncomment After Database creation
)

# mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE libraryproject")

# Check If Database is Created or not
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)



# CREATE TABKE FOR BOOK DETAILS

# mycursor.execute("CREATE TABLE books (book_id smallint PRIMARY KEY AUTO_INCREMENT, book_name VARCHAR(250), author_name VARCHAR(50), price smallint, stock smallint, edition smallint)")

# Check if table is created or not :
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# CREATES TABLE FOR MEMBER DETAILS
# mycursor.execute("CREATE TABLE members (member_id smallint PRIMARY KEY AUTO_INCREMENT, member_name VARCHAR(50), member_address VARCHAR(250), member_phone VARCHAR(14))")

# CREATES TABLE FOR STORING BOOK ISSUING Details
# mycursor.execute("CREATE TABLE issues (s_no smallint PRIMARY KEY AUTO_INCREMENT, member_id smallint, FOREIGN KEY (member_id) REFERENCES members(member_id), book_id smallint, FOREIGN KEY (book_id) REFERENCES books(book_id), date_issue DATE, date_return DATE )")
