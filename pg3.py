import pg8000

def connect():
    return pg8000.connect(
        user='tweet',
        password='tweet',
        host='localhost',
        port=5432,
        database='pg_example'
    )


def create_table(conn):
    print('\n*****CREATING TABLE*****\n')

    # CREATE TABLE
    cursor = conn.cursor()
    cursor.execute("CREATE TEMPORARY TABLE book (id SERIAL, title TEXT)")

    cursor.execute(
        "INSERT INTO book (title) VALUES (%s), (%s), (%s) RETURNING "
        "id, title",
        ("Ender's Game", "Lord of the Rings", "Wheel of Time")
    )

    res = cursor.fetchone()
    while res:
        print(res[0], res[1])
        res = cursor.fetchone()
    cursor.close()


def update(conn):
    print('\n*****UPDATE*****\n')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE book SET title=%s WHERE title LIKE '%%Game%%' RETURNING id",
        ("A Song of Ice and Fire",)
    )
    print('ROWCOUNT:', cursor.rowcount)
    res = cursor.fetchall()
    for row in res:
        print('updated id:', row[0])
    cursor.close()


def delete(conn):
    print('\n*****DELETE*****\n')
    cursor = conn.cursor()
    cursor.execute(
        "DELETE from book WHERE title IN ('A Song of Ice and Fire', 'Hobbit')",
    )
    print('ROWCOUNT:', cursor.rowcount)
    cursor.close()


def select(conn):
    print('\n*****SELECT*****\n')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title FROM book ORDER BY id"
    )
    # results = cursor.fetchall()

    for row in cursor: # it implements __iter__()
        id, title = row
        print("id = %s, title = %s" % (id, title))
    cursor.close()


if __name__ == '__main__':
    conn = connect()
    create_table(conn)
    select(conn)
    update(conn)
    select(conn)
    delete(conn)
    select(conn)
    conn.commit()
    conn.close()
