import psycopg2
import names
import secrets
import string

conn = psycopg2.connect(dbname='test_base',
                        user='postgres',
                        password='qwerty',
                        host='localhost',
                        port='5432')

cursor = conn.cursor()
letters = string.ascii_letters
digits = string.digits
alphabet = letters + digits

pwd_length = 12
phone_length = 11

for i in range(10):

    if conn:

        pwd = ''
        for ii in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        phn = '+'
        for j in range(phone_length):
            phn += ''.join(secrets.choice(digits))

        user_name = names.get_full_name()
        user_email = user_name.replace(' ', '') + '@gmail.com'
        user_password = pwd
        user_phone = phn

        base_data = (user_email, user_password, user_phone, user_name)

        insert_query = '''insert into public.users (email, password_field, phone, user_name) values (%s, %s, %s, %s)'''

        cursor.execute(insert_query, base_data)
        conn.commit()
        print(f'Set user {i+1} - {base_data}')

cursor.close()