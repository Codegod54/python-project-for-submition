# save the result until the user doesn't enter 6
# display the results when the user enters 7
# exit when the user enters 5
# once the operation is done, ask the user to enter the next operation
# the user can perform multiple operations
# the user can save multiple results
# the user can display all the saved results
# save the operator and the result in the database

import sqlite3

def save_result(operator, result):
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            operator TEXT,
            result INTEGER
        )
    ''')

    cursor.execute('''
        INSERT INTO results (operator, result) VALUES (?, ?)
    ''', (operator, result))

    conn.commit()
    conn.close()

def display_results():
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM results')
    results = cursor.fetchall()
    for result in results:
        print(f"{result[1]}: {result[2]}")
    conn.close()

def main():
    while True:
        g = int(input("""Select the function:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exit
            6. Display results
                      """))

        if g == 5:
            break

        if g == 6:
            display_results()
            continue

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if g == 1:
            result = a + b
            operator = "Addition"
        elif g == 2:
            result = a - b
            operator = "Subtraction"
        elif g == 3:
            result = a * b
            operator = "Multiplication"
        elif g == 4:
            result = a / b
            operator = "Division"
        else:
            print("Invalid input")
            continue

        print(f"The result is: {result}")
        h = input("Do you want to save the result? Enter 'y' to save the result: ")
        if h == 'y':
            save_result(operator, result)
        else:
            print("The result is not saved.")

if __name__ == "__main__":
    main()