import sqlite3
import random

''' Database connection creation'''    
database_file_path = r"D:\\Django\\AssignmentNonStop\\db.sqlite3"
conn = sqlite3.connect(database_file_path)

'''Default values assign to the product fields in list format for location,shape,size and price '''
location_list = ["Mumbai", "Pune", "Bangalore", "Rajasthan", "Gujarat"]
shapes_list = ["Circle", "Rectangle", "Triangle", "Square", "Oval", "Diamond", "Heart", "Star", "Haxagon", "Trapezoid", "Parallelogram", "Cone"]
size_list = ["S", "M", "L", "XL", "2XL", "3XL"]
price_list =  [100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0, 650.0, 700.0, 750.0, 800.0, 850.0, 900.0, 950.0, 1000.0]

cur = conn.cursor()

for i in range(1):
    '''Choice random data from list for location,shape,size and price and store in the product table'''
    shape = random.choice(shapes_list)    
    size = random.choice(size_list)    
    location = random.choice(location_list)    
    price = random.choice(price_list)    
    query = """insert into app_product(shape,size,location,price) values(?,?,?,?);"""
    data = (shape, size, location, price)

    cur.execute(query, data)

conn.commit()

cur.execute("select * from app_product")

output = cur.fetchall()

print("Output:",output)

cur.close()