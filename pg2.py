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
    print(cursor)

    print('FUNCTIONS')
    print()
    print('.execute(...)', cursor.execute.__doc__)
    print('-----------------------------------')
    print('.fetchone()', cursor.fetchone.__doc__)
    print('-----------------------------------')
    print('.fetchall()', cursor.fetchall.__doc__)
    print('-----------------------------------')
    print('.close()', cursor.close.__doc__)
    print('-----------------------------------')
    print('.__iter__()', cursor.__iter__.__doc__)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    program()
