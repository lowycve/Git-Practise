import sqlite3
import string
import random
from itertools import permutations
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

id_list = []
for i in range(1, 1112):
    id_list.append(i)
flw_count_list = []
for y in range(20):
    flw_count_list.append(y)
conn = sqlite3.connect('friends.db')
c = conn.cursor()


for o in id_list:
    print(o)
    sql_cmd1 = 'SELECT user_name FROM user WHERE id=' + str(o)
    flwer_result = c.execute(sql_cmd1)
    for q in flwer_result:
        flwer_username = q[0]
    flw_count = random.choice(flw_count_list)
    all_list = list(id_list)
    all_list.remove(o)
    for f in range(flw_count):
        crt_flw_id = random.choice(all_list)
        if crt_flw_id == o:
            raise ValueError('No!')
        all_list.remove(crt_flw_id)
        sql_cmd2 = 'SELECT user_name FROM user WHERE id=' + str(crt_flw_id)
        flwing_result = c.execute(sql_cmd2)
        for a in flwing_result:
            flwing_username = a[0]
        c.execute('''INSERT INTO Relation(follower_id, follower_username, following_id, following_username) Values(?, ?, ?, ?)''', (o, flwer_username, crt_flw_id, flwing_username))
conn.commit()
c.close()
conn.close()