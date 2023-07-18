import psycopg2

conn = psycopg2.connect(dbname='qa_ddl_f_1_200',
                        user='padawan_user_200',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor()

if conn:

    print('Connected to database')

    sql_req = '''select * from salary'''
    cursor.execute(sql_req)

    req_result = cursor.fetchall()

    for i in req_result:
        print(f'id = {i[0]}, salary = {i[1]}')

    conn.commit()
    conn.close()