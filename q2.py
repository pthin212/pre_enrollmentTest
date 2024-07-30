import json
import pyodbc
import datetime

def extract_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def transform_data(data):
    transformed_data = []
    for employee in data:
        employee['join_date'] = datetime.datetime.strptime(employee['join_date'], '%Y-%m-%d').date()
        transformed_data.append(employee)
    return transformed_data

def load_data(data):
    conn = None
    try:
        conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                              "Server=TPT_COMPANY;"
                              "Database=test;"
                              "Trusted_Connection=yes;")
        cursor = conn.cursor()

        for employee in data:
            cursor.execute('''
                INSERT INTO employees (id, name, department, salary, join_date)
                VALUES (?, ?, ?, ?, ?)
            ''', employee['id'], employee['name'], employee['department'], employee['salary'], employee['join_date'])

        conn.commit()
        
    except pyodbc.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    file_path = 'employees.json'
    data = extract_data(file_path)
    transformed_data = transform_data(data)
    load_data(transformed_data)