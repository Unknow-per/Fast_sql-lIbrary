# Fast_sqlite

<b>Fast SQL</b> is a Python library to make and use a sqlite3 database. For use this library you can copy the file in your code directory and use below codes or read <b>example/write_and_read_data.py</b> file

# Create values to use library
```python

from fast_sql import fast_sqlite

fsql = fast_sqlite(db_name="database.db", table_name="users", attributes=["username", "email", "password"])

```

# Connect to a database

```python

fsql.connect()
# Congratulation! You have been connected :)

```

# Close connection

```python

fsql.close()
# Oh... You have been disconnected :( 
# We will work together for next time

```

# Insert data in database

```python

fsql.Insert_in(values=["admin", "admin.root@admin.com", "admin"]) # output: True/False

# This is how it save:
# --> users:
#      ________________________________________________________________
#     |                |                         |                     |
#     |    username    |          email          |       password      |
#     |________________|_________________________|_____________________|
#     |                |                         |                     |
#     |     admin      |     admin.root@ad...    |        admin        |
#     |                |                         |                     |
#     |     user1      |     user.1234@use...    |        12345        |
#     |                |                         |                     |
#     |________________|_________________________|_____________________|

```

# Select data from database

```python

#                    select "password", where username='username'
password = fsql.Select_from("password", "username", username) # output: password

```

# Use a custome command

```python

output = fsql.Custome_command("command") # output: output of your command :)
print(output)

```

<<<<<<< HEAD
# Fast-sql CLI
For have the CLI mode of Fast-sql library you can get the <a href="https://www.github.com/Unknow-per/Fast_sql-cli">Fast_sql-cli</a>.
=======
# <a href='https://learnsql.com/blog/sql-basics-cheat-sheet/01-sample-data.webp' target='_blank'>Sqlite database schematic </a>

[<img href="[https://learnsql.com/blog/sql-basics-cheat-sheet/01-sample-data.webp](https://learnsql.com/blog/sql-basics-cheat-sheet/01-sample-data.webp)" width="100%" height="500px" />](https://learnsql.com/blog/sql-basics-cheat-sheet/01-sample-data.webp)
>>>>>>> 558b02bc4cefb4c1856c88f50d0e9162c7d51368

# Contributes
<h3> 1.<a target="_blank" href="https://www.github.com/Unknow-per/">Unknow-per</a></h3>
