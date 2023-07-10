import csv

def create_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Example usage:
file_path = 'employees.csv'
data = [
    ['EmployeeId', 'Email', 'Name', 'Phone'],
    ['1', 'john@example.com', 'John Doe', '1234567890'],
    ['2', 'jane@example.com', 'Jane Smith', '9876543210']
]

create_csv_file(file_path, data)
print(f"CSV file '{file_path}' has been created.")
