import sqlalchemy as db
engine=db.create_engine('mysql://root:password@localhost/organization')
connection=engine.connect()
metadata=db.MetaData(bind=engine)

#-- Task 1 Creating a table called Employee
emp=db.Table('employee',metadata,
db.Column("Id",db.Integer()),
db.Column("Name",db.String(255),nullable=False),
db.Column("Department",db.String(50)),
db.Column("Basic_Salary",db.Float()),
db.Column("Da",db.Integer()),
db.Column("Hra",db.Integer()))
metadata.create_all()

#-- Task 2 Inserting Values into the Table
query=db.insert(emp)
values_list=[{'Id':1,'Name':'sai','Department':'sales','Basic_Salary':2500,'Da':100,'Hra':500},
{'Id':2,'Name':'krishna','Department':'marketing','Basic_Salary':4000,'Da':200,'Hra':600},{'Id':3,'Name':'sk','Department':'marketing','Basic_Salary':6500,'Da':1000,'Hra':1500},{'Id':4,'Name':'sai','Department':'delivery','Basic_Salary':8000,'Da':2000,'Hra':1000},
{'Id':5,'Name':'krishna','Department':'it','Basic_Salary':10000,'Da':2000,'Hra':1000},{'Id':6,'Name':'vamshi','Department':'delivery','Basic_Salary':3500,'Da':500,'Hra':1000},{'Id':7,'Name':'kiran','Department':'marketing','Basic_Salary':7500,'Da':1000,'Hra':2000},
{'Id':8,'Name':'raju','Department':'sales','Basic_Salary':5000,'Da':1000,'Hra':1500},{'Id':9,'Name':'vamshi','Department':'it','Basic_Salary':12000,'Da':3000,'Hra':3000},{'Id':10,'Name':'ramu','Department':'delivery','Basic_Salary':15000,'Da':5000,'Hra':6000},
{'Id':11,'Name':'rahul','Department':'sales','Basic_Salary':4000,'Da':500,'Hra':1000},{'Id':12,'Name':'ravi','Department':'it','Basic_Salary':6500,'Da':500,'Hra':500},{'Id':13,'Name':'sai','Department':'marketing','Basic_Salary':10000,'Da':3000,'Hra':4000},{'Id':14,'Name':'krishna','Department':'delivery','Basic_Salary':12000,'Da':5000,'Hra':7000},
{'Id':15,'Name':'sk','Department':'it','Basic_Salary':13000,'Da':3000,'Hra':1500}]
result=connection.execute(query,values_list)

#-- Task 3 Retrieving all the Inserted Values
result_lst=connection.execute(db.select([emp])).fetchall()
print(result_lst)

#-- Task 4 Display Total Salary of The Employees
query=db.select([emp.columns.Id,emp.columns.Name,emp.columns.Department,(emp.columns.Basic_Salary+emp.columns.Da+emp.columns.Hra).label('Total_Salary')])
result_lst=connection.execute(query)
print(result_lst)

#-- Task 5 Display employee details whose Total salary(basic_Salary+da+hra) is less than 15000
query=db.select([emp]).where(emp.columns.Basic_Salary+emp.columns.Da+emp.columns.Hra<15000)
result_lst=connection.execute(query).fetchall()
print(result_lst)

#-- Task 6 Select Distincy Employee names
result_lst=connection.execute(db.select([emp.columns.Name.distinct()])).fetchall()
print(result_lst)

#-- Task 7 Display Employee Details Whose Total salary(basic_Salary+da+hra) is (2500,5000,7500)
query=db.select([emp]).where((emp.columns.Basic_Salary+emp.columns.Da+emp.columns.Hra).in_([2500,5000,7500]))
result_lst=connection.execute(query).fetchall()
print(result_lst)

#-- Task 8 Display Employee Details In Descending order of Total salary(basic_Salary+da+hra)
query=db.select([emp.columns.Id,emp.columns.Name,emp.columns.Department,(emp.columns.Basic_Salary+emp.columns.Da+emp.columns.Hra).label('Total_Salary')]).order_by(db.desc("Total_Salary"))
result_lst=connection.execute(query).fetchall()
print(result_lst)

#-- Task 9 Get The count of Employees Working in each Department
result_lst=connection.execute(db.select([emp.columns.Department,db.func.count(emp.columns.Id)]).group_by(emp.columns.Department)).fetchall()
print(result_lst)

#-- Task 10 Select Employee Whose Name Starts with Ra
result_lst=connection.execute(db.select([emp.columns.Name]).where(emp.columns.Name.like("Ra%"))).fetchall()
print(result_lst)
