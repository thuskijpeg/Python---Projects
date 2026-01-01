# Thusano Masalesa
# 45312222

import sqlite3

def display_menu():
    print("\nStudent Database Menu")
    print("1. Create Table student")
    print("2. Add new student(s)")
    print("3. View all students")
    print("4. View top-performing students")
    print("5. Search student by last name")
    print("6. Drop Table student")
    print("7. Exit")

def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            average_mark REAL
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'students' has been created (if it didn't already exist).")

def add_student():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    add_another = "y"
    while add_another.lower() == "y":
        print("\nEnter student details:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        average_input = input("Average mark: ")

        try:
            average_mark = float(average_input)
            cursor.execute('''
                INSERT INTO students (first_name, last_name, average_mark)
                VALUES (?, ?, ?)
            ''', (first_name, last_name, average_mark))
            conn.commit()
            print(f"Saved: {first_name} {last_name}, Average Mark: {average_mark}")
        except Exception as e:
            print(f"An error occurred: {e}")

        add_another = input("Do you want to add another student record? (y/n): ")

    conn.close()
    print("\nStudent input complete.")

def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    if not students:
        print("\nNo students found in the database.")
    else:
        print("\nAll Students:")
        print("-" * 50)
        print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Avg Mark':<10}")
        print("-" * 50)
        for student in students:
            print(f"{student[0]:<5}{student[1]:<15}{student[2]:<15}{student[3]:<10.2f}")
        print("-" * 50)
        print(f"Total students: {len(students)}")
    
    conn.close()

def view_top_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE average_mark >= 75 ORDER BY average_mark DESC")
    top_students = cursor.fetchall()
    
    if not top_students:
        print("\nNo top-performing students found (avg mark >= 75).")
    else:
        print("\nTop-Performing Students (Avg >= 75):")
        print("-" * 50)
        print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Avg Mark':<10}")
        print("-" * 50)
        for student in top_students:
            print(f"{student[0]:<5}{student[1]:<15}{student[2]:<15}{student[3]:<10.2f}")
        print("-" * 50)
        print(f"Total top students: {len(top_students)}")
    
    conn.close()

def search_student():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    last_name = input("Enter last name (or part of it) to search: ").strip()
    
    cursor.execute("SELECT * FROM students WHERE last_name LIKE ?", (f"%{last_name}%",))
    matched_students = cursor.fetchall()
    
    if not matched_students:
        print(f"\nNo students found with last name containing '{last_name}'.")
    else:
        print(f"\nSearch Results for '{last_name}':")
        print("-" * 50)
        print(f"{'ID':<5}{'First Name':<15}{'Last Name':<15}{'Avg Mark':<10}")
        print("-" * 50)
        for student in matched_students:
            print(f"{student[0]:<5}{student[1]:<15}{student[2]:<15}{student[3]:<10.2f}")
        print("-" * 50)
        print(f"Total matches: {len(matched_students)}")
    
    conn.close()

def drop_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    confirm = input("Are you sure you want to drop the 'students' table? This action cannot be undone. (y/n): ")
    if confirm.lower() == "y":
        try:
            cursor.execute("DROP TABLE IF EXISTS students")
            conn.commit()
            print("Table 'students' has been dropped.")
        except Exception as e:
            print(f"An error occurred while dropping the table: {e}")
    else:
        print("Drop table action cancelled.")

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
        elif user_option == "3":
            view_students()
        elif user_option == "4":
            view_top_students()
        elif user_option == "5":
            search_student()
        elif user_option == "6":
            drop_table()
        elif user_option == "7":
            print("Goodbye!")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
