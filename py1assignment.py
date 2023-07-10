import csv
import mysql.connector
class Employee:
    def __init__(self):
        self.connection= mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="abhadatabase"
        )
        self.cursor= self.connection.cursor()
        print("this is working")
    def setter(self,employee_id,email,name,phone,pf_id,DOJ,DOB,department):
        self.employee_id=employee_id
        self.email=email
        self.is_email_valid()
        self.name=name
        self.phone=phone
        self.is_phone_number_valid()
        self.pf_id = pf_id
        self.DOJ = DOJ
        self.DOB = DOB
        self.department = department
        #print("setter")
    def is_email_valid(self):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not( re.match(pattern, self.email) ):
            while not( re.match(pattern, self.email) ):
                self.email=input("Enter valid email ")
    def is_phone_number_valid(self):

        if not( self.phone.isdigit() and len(self.phone) >= 10):
            while not(self.phone.isdigit() and len(self.phone) >= 10):
                self.phone=input("Enter valid phone ")

    #create the table
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                EmployeeId INT AUTO_INCREMENT,
                Email VARCHAR(25) UNIQUE,
                Name VARCHAR(25),
                Phone VARCHAR(35),
                PfID int,
                DOJ DATE,
                DOB DATE,
                Department VARCHAR(255),
                PRIMARY KEY (EmployeeId)
            )
        """)
        print("table created")
        
    
    def add_employee(self):
        self.cursor.execute("""insert into Employees (EmployeeId, Email, Name, Phone, PfId, DOJ, DOB, Department)
                            values (%s, %s, %s, %s, %s, %s, %s, %s) """, (self.employee_id, self.email, self.name, self.phone, self.pf_id, self.DOJ, self.DOB, self.department))
        self.connection.commit()
        print("Employee added")
    def read_employee(self):
        self.cursor.execute("select * from Employees")
        employees = self.cursor.fetchall()

        if employees:
            employeedetails=["EmployeeId Email  Name  Phone  Pf ID date of Joining  Date of Birth  Department"]
            print(employeedetails)
            for employee in employees:
                row=[x for x in employee ]
                print(row,'\n')
        else:
            print("No employees found.")
        print("read")
    
    def update_employee(self):
        self.cursor.execute("SELECT EmployeeId, Phone FROM Employees")
        employees = self.cursor.fetchall()

        for employee in employees:
            employee_id, current_phone = employee
            self.phone = input(f"Enter new phone number for employee {employee_id}: ")
            self.is_phone_number_valid()     
            self.cursor.execute("UPDATE Employees SET Phone = %s WHERE EmployeeId = %s", (self.phone, employee_id))
        self.connection.commit()


    
    def get_employee(self):
        self.cursor.execute("SELECT * FROM Employees WHERE YEAR(DOJ) = %s", (2021,))
        self.employees= self.cursor.fetchall()
    
    def write_to_csv(self):
        if self.employees:
            file_path = "employees.csv"
            with open(file_path, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([
                    "Employee Id", "Email", "Name", "Phone", "Pf Id", "Date of Joining",
                    "Date of Birth", "Department"
                ])
            writer.writerows(self.employees)
            print("Employees written to CSV file successfully.")
        else:
            print("No employees found to write to CSV.")
        
    
    def close(self):
        self.cursor.close()
        self.connection.close()

    
    





def main():
    print("abha")
    obj=Employee()
    obj.create_table()
    while True:
        print("1. add employee")
        print("2.read employee")
        print("3. Update employees Phone Numbers")
        print("4. Get Employees with Joining Year 2021 and Write to CSV")
        print("5. Exit")
        choose=input("select any point")
        if choose =="1" :
            print("Enter employee details:")
            employee_id = input("Employee Id: ")
            email = input("Email: ")
            name = input("Name: ")
            phone = input("Phone: ")
            pf_id = input("Pf Id: ")
            DOJ = input("Date_of_oining:")
            DOB = input("Date_of_Birth: ")
            department = input("Department: ")
            obj.setter(employee_id,email,name,phone,pf_id,DOJ,DOB,department)
            obj.add_employee()
        elif choose =="2":
            obj.read_employee()
        elif choose =="3":
            obj.update_employee()
        elif choose =="4":
            obj.get_employee()
            obj.write_to_csv()
        elif choose =="5":
            break
        else:
            print("invalid point")
    obj.close()
            
if __name__ == "__main__":
    main()