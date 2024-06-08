import sqlite3

def insert_student(name: str, grade: float):
    try:
      
        conn = sqlite3.connect('sample.db')

        cursor = conn.cursor()

        cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))

        conn.commit()

        print("Student inserted successfully.")

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
  
        cursor.close()
        conn.close()


insert_student("Venubabu", 90) # calling function with data you want to save table.
