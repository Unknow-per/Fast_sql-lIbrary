from fast_sql import fast_sqlite
fsql = fast_sqlite("database.db", "Users", ["username", "email", "password"])
fsql.connect()
fsql.Insert_in(["admin", "admin.root@admin.com", "admin"])
email_addr = fsql.Select_from("email", "username", "admin")
fsql.close()
