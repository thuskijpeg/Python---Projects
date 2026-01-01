import sqlite3

def display_menu():
    print("\nStudent Database Menu")
    print("1. Create Table student")
    print("2. Add new student(s)")
    print("3. PLACEHOLDER")
    print("4. PLACEHOLDER")
    print("5. PLACEHOLDER")
    print("6. Drop Table student")
    print("7. Exit")

def create_table():
    try:
        conn = sqlite3.connect("Students.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                average_mark REAL
            )
        """)
        conn.commit()
        print("Table 'students' created or already exists.")
    except Exception as e:
        print("Error creating table:", e)
    finally:
        conn.close()

def add_student():
    try:
        conn = sqlite3.connect("Students.db")
        cursor = conn.cursor()

        while True:
            try:
                student_id = int(input("Enter Student ID (integer): "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                average_mark = float(input("Enter Average Mark: "))

                cursor.execute("""
                    INSERT INTO students (student_id, first_name, last_name, average_mark)
                    VALUES (?, ?, ?, ?)
                """, (student_id, first_name, last_name, average_mark))
                conn.commit()

                print(f"Student added: {student_id} - {first_name} {last_name}, Average Mark: {average_mark}")
            except Exception as e:
                print("Error adding student:", e)

            cont = input("Do you want to add another student record? (y/n): ").lower()
            if cont != 'y':


        print("Student input process completed.")
    except Exception as e:
        print("Database error:", e)
    finally:
        conn.close()

def drop_table():
    try:
        confirm = input("Are you sure you want to drop the 'students' table? (y/n): ").lower()
        if confirm != 'y':
            print("Drop table cancelled.")
            return

        conn = sqlite3.connect("Students.db")
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        print("Table 'students' has been dropped.")
    except Exception as e:
        print("Error dropping table:", e)
    finally:
        conn.close()

def main():
    user_option = ""

    while user_option != "7":

        display_menu()
        user_option = input("Choose an option: ")

        if user_option == "1":
            create_table()
        elif user_option == "2":
            add_student()
        elif user_option in {"3", "4", "5"}:
            print("This feature is not yet implemented.")
        elif user_option == "6":
            drop_table()
        elif user_option == "7":
            print("Goodbye!")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
