import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='areum' password='areum' host='localohst' port='5434'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='areum' password='areum' host='localohst' port='5434'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='areum' password='areum' host='localohst' port='5434'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='areum' password='areum' host='localohst' port='5434'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='areum' password='areum' host='localohst' port='5434'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
#insert("Coffee Cup", 10, 5)
#delete("Wine Glass")
update(11, 6, "Water Glass")
print(view())
