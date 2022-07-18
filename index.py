import sqlite3


def create_table():
    connection = sqlite3.Connection("cinema.db")
    connection.execute("""
    CREATE TABLE "Seat" (
        "seat_id" TEXT,
        "occupied" INTEGER,
        "price"   REAL
                );


            """)
    connection.commit()
    connection.close()





def insert_record():
    connection = sqlite3.Connection("cinema.db")
    connection.execute("""
    INSERT INTO "Seat" ("seat_id","occupied","price") VALUES ("A1","0","100") ,("A2","1","120") ,("sofa","0","220")   
    """)
    connection.commit()
    connection.close()

def select_All():
    connection =  sqlite3.Connection("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    Select "seat_id" ,"price" from "Seat"
    Where "occupied"=0
    """)
    result = cursor.fetchall()
    connection.close()
    return result


def select_All_columns():
    connection =  sqlite3.Connection("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    Select "seat_id" ,"price","occupied" from "Seat"
    
    """)
    result = cursor.fetchall()
    connection.close()
    return result



def select_All_with_condition():
    connection =  sqlite3.Connection("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    Select "seat_id" ,"price" from "Seat"
    Where "occupied"=0
    """)
    result = cursor.fetchall()
    connection.close()
    return result






def update_value():
    connection = sqlite3.Connection("cinema.db")
    connection.execute("""
    Update "Seat" Set "occupied"=1
    """)
    connection.commit()
    connection.close()


def update_value_condition():
    connection = sqlite3.Connection("cinema.db")
    connection.execute("""
    Update "Seat" Set "occupied"=1
    where "seat_id" ="sofa"
    """)
    connection.commit()
    connection.close()

print(select_All())
update_value()