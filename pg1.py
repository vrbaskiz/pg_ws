import pg8000


def program():
    conn = pg8000.connect(
        user='tweet',
        password='tweet',
        host='localhost',
        port=5432,
        database='pg_example'
    )
    print(conn)
    print()
    print('cursor():', conn.cursor.__doc__)
    print('-----------------------------------')
    print('commit():', conn.commit.__doc__)
    print('-----------------------------------')
    print('rollback()', conn.rollback.__doc__)
    print('-----------------------------------')
    print('close():', conn.close.__doc__)

    conn.close()


if __name__ == '__main__':
    program()
