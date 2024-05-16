import datetime

import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'path')

class DbConnector():

    def __init__(self):
        self.conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'path')
        self.cursor=self.conn.cursor()
    def get_fail(self):
        self.cursor.execute(f"select * from Fail")
        result = self.cursor.fetchall()
        return result
    def get_employees(self):
        self.cursor.execute("select * from Employee")
        result = self.cursor.fetchall()
        return result
    def get_orders(self):
        self.cursor.execute("select * from Orders")
        result = self.cursor.fetchall()
        for x in result:
           return result
    def get_customers(self):
        self.cursor.execute(f"select * from Customers")
        result = self.cursor.fetchall()
        for x in result:
            return result
    def get_customer_order(self, cust_name: str):
        self.cursor.execute(f"select * from Orders where cust_name = '{cust_name}'")
        result = self.cursor.fetchall()
        for x in result:
            return result
    def add_employee(self, emp_ID: int, emp_name: str, emp_spec: str, date_of_emp: datetime.date):
        self.cursor.execute(f"insert into Employee (emp_ID, emp_name, emp_spec, date_of_emp) values "
                            f"('{emp_ID}','{emp_name}','{emp_spec}','{date_of_emp}')")
        self.cursor.commit()
    def add_customer(self, phone_number: str, cust_name: str):
        self.cursor.execute(f"insert into Customers (cust_number, cust_name) values ('{phone_number}','{cust_name}')")
        self.cursor.commit()
    def add_order(self, order_code: int, pc_code: int, master_ID: int, rep_begin: datetime.date,
                  rep_end: datetime.date, cost: float, failure: str, cust_name: str):
        self.cursor.execute(f"insert into Orders (order_code, pc_code, master_ID, rep_begin, rep_end, cost, failure, cust_name) "
                            f"values ({order_code},{pc_code},{master_ID},'{rep_begin}','{rep_end}',{cost},'{failure}','{cust_name}')")
        self.cursor.commit()
    def add_fail(self, ID: int, order_ID: int, emp_ID: int, fail_cause: str, description: str):
        self.cursor.execute(f"insert into Fail (ID, order_ID, emp_ID, fail_cause, description) "
                            f"values ('{ID}','{order_ID}','{emp_ID}','{fail_cause}','{description}')")
        self.cursor.commit()

    def remove_customer(self, cust_name: str):
        self.cursor.execute(f"delete from Customers where cust_name = '{cust_name}'")
        self.cursor.commit()
    def remove_fail(self, ID: int):
        self.cursor.execute(f"delete from Fail where ID = '{ID}'")
        self.cursor.commit()

    def remove_employee(self, emp_name: str):
        self.cursor.execute(f"delete from Employee where emp_name = '{emp_name}'")
        self.cursor.commit()

    def remove_orders(self, order_code: str):
        self.cursor.execute(f"delete from Orders where order_code = '{order_code}'")
        self.cursor.commit()

a = DbConnector()
#a.add_customer("7057021021", "Renata Bamper")
#a.remove_customer("7057021021")
#a.get_orders()
#a.add_order(3,1201,1, "20.05.2024", "26.05.2024",200000.0,"Installation", "Kostantin Bikkurazov" )
#a.add_employee(3,"Alina Bibler", "Dust","04.07.2022")
#a.get_fail()
#a.add_fail(3, 3, 3, "Dust", "Dust everywhere")
print(a.get_employees())


