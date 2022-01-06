# SQL ALCHEMY
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

In Simple Words SQlAlchemy lets user to Interact with Databases by Using Python Lnaguage Instead of SQL, as users can write code in Python to Interact with Databases.

### Setup To Run SQLAlchemy:
1. Install Python From [Python Website](https://www.python.org/downloads/) Following Installation [Document](https://www.tutorialspoint.com/how-to-install-python-in-windows) for Successful Installation
2. After Successfull Installation of Python Open Command Prompt and Type `pip install sqlalchemy` to install SQLAlchemy
3. Next Type `pip install sqlclient` to install SqlClient
4. Next Type `pip install mysql-connector-python` to Install MySQL Python Connector
5. Now Go to Any folder and create a Python File and the first Thing we Need to do is Import Packages and Create a Engine
6. Basic Syntax for Creating Engine **`dialect+driver://username:password@host:port/database`**
7. Here in the File I Used MySQL.However, You can use Your Own Choice of Database For More info about Configuring Different Databases [Click Here](https://docs.sqlalchemy.org/en/14/core/engines.html#postgresql)
8. However, For your Understanding I Added Comments for Each Task. So Please go Through Incase you are Stuck.

#### References
1. https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
2. https://www.makeuseof.com/tag/python-object-relational-maps/
