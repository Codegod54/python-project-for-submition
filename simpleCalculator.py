from datetime import datetime
import sqlite3
import math

def date_time():
    now = datetime.now()
    dt = now.date()
    ti = now.time()
    return dt, ti

def save_result(numa, operator, numb, result, date, time):
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            numa REAL,
            operator TEXT,
            numb REAL,
            result REAL,
            date str,
            time str
        )

    ''')

    cursor.execute('''
        INSERT INTO results (numa, operator, numb, result, date, time) VALUES (?, ?, ?, ?, ?, ?)
    ''', (numa, operator, numb, result, date, time ))

    conn.commit()
    conn.close()


def display_history():
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM results')
    results = cursor.fetchall()
    for result in results:
        print(f"{result[1]} {result[2]} {result[3]} = {result[4]} on {result[5]} at {result[6]}")
    conn.close()

def main():
    while True:

        try:
            g = int(input("""Select the function:
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                5. Exit
                6. Display history
                        """))
        except:
            print("Invalid input. Please enter a valid number.")
            continue

        if g == 5:
            break

        if g == 6:
            display_history()
            continue
        try:
    
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except:
            print("character not accepted")
            continue
        if g == 1:
            result = math.fsum(a, b)
            operator = "Addition"
        elif g == 2:
            result = math.fsum(a, -b)
            operator = "Subtraction"
        elif g == 3:
            result = a * b
            operator = "Multiplication"
        elif g == 4:
            if b == 0:
                print("Error: Division by zero.")
                continue
            result = a / b
            operator = "Division"

        else:
            print("Invalid input")
            continue

        print(f"The result is: {result}")
        dt, ti = date_time()
        save_result(a, operator, b, result, str(dt), str(ti))

if __name__ == "__main__":
    main()
