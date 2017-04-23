import pg8000


def program():
    conn = pg8000.connect(
        user='tweet',
        password='tweet',
        host='localhost',
        port=5432,
        database='pg_example'
    )

    cursor = conn.cursor()
    cursor.execute("CREATE TEMPORARY TABLE book (id SERIAL, title TEXT)")
    cursor.execute(
        "INSERT INTO book (title) VALUES (%s), (%s)",
        ("Ender's Game", "Speaker for the Dead"))

    cursor.execute(
        "SELECT id, title FROM book"
    )
    results = cursor.fetchall()
    for row in results:
        id, title = row
        print("id = %s, title = %s" % (id, title))

    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    program()
