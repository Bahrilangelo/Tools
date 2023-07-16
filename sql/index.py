import sqlite3

sqlfile = './sql/example.sql'

# Sql Connection
def get_database_connection():
    con = sqlite3.connect(sqlfile)

    return con

# Sql Query
def get_sql_query(sql):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    con.close()

    return result

# Sql Table Create

def create_table():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, address TEXT)")
    con.commit()
    con.close()

# Sql INSERT

def insert_data(name, age, address):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO users (name, age, address) VALUES (?, ?, ?)", (name, age, address))
    con.commit()
    con.close()

# Sql UPDATE

def update_data(name, age, address, id):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("UPDATE users SET name = ?, age = ?, address = ? WHERE id = ?", (name, age, address, id))
    con.commit()
    con.close()

# Sql DELETE

def delete_data(id):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE id = ?", (id,))
    con.commit()
    con.close()

# Sql SELECT

def select_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT WHERE

def select_where_data(id):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (id,))
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT LIKE

def select_like_data(name):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name LIKE ?", ('%'+name+'%',))
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT ORDER BY

def select_orderby_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users ORDER BY id DESC")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT LIMIT

def select_limit_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users LIMIT 2")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT OFFSET

def select_offset_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users LIMIT 2 OFFSET 2")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT COUNT

def select_count_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT SUM

def select_sum_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT SUM(age) FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT AVG

def select_avg_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT AVG(age) FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT MAX

def select_max_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT MAX(age) FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT MIN

def select_min_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT MIN(age) FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT GROUP BY

def select_groupby_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT age, COUNT(*) FROM users GROUP BY age")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT HAVING

def select_having_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 1")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT JOIN

def select_join_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT users.name, users.age, users.address, users2.name, users2.age, users2.address FROM users INNER JOIN users2 ON users.name = users2.name")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT UNION

def select_union_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT name, age, address FROM users UNION SELECT name, age, address FROM users2")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT UNION ALL

def select_unionall_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT name, age, address FROM users UNION ALL SELECT name, age, address FROM users2")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT EXIST

def exists(table):
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT EXISTS(SELECT * FROM users WHERE name = ?)", (table,))
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT CASE

def select_case_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT name, CASE WHEN age < 20 THEN '20歳未満' WHEN age < 30 THEN '20代' WHEN age < 40 THEN '30代' WHEN age < 50 THEN '40代' WHEN age < 60 THEN '50代' ELSE '60歳以上' END AS age FROM users")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT IN

def select_in_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name IN ('佐藤', '鈴木')")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT NOT IN

def select_notin_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE name NOT IN ('佐藤', '鈴木')")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT BETWEEN

def select_between_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE age BETWEEN 20 AND 30")
    result = cur.fetchall()
    con.close()

    return result

# Sql SELECT NOT BETWEEN

def select_notbetween_data():
    con = get_database_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE age NOT BETWEEN 20 AND 30")
    result = cur.fetchall()
    con.close()

    return result
