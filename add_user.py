from db_config import get_connection

conn = get_connection()
c1 = conn.cursor()

us = input("Enter new username: ")
pa = input("Enter password: ")

c1.execute("INSERT INTO login_info VALUES (%s, %s)", (us, pa))
conn.commit()
print("User added successfully!")

conn.close()
