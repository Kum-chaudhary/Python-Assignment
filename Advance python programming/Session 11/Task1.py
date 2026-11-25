from Connection import get_connection

def create_table():
    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS STUDENTS
    (
        ID SERIAL PRIMARY KEY,
        NAME VARCHAR(50),
        CLASS_NAME VARCHAR(50),
        MONTHLY_FEE INT
    )
""")
    conn.commit()
    print("sucessfully table created !")

    conn.close()

create_table()    

    
