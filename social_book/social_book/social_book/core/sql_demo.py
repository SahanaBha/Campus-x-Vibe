import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_book.settings")

# Set up the Django environment
django.setup()

import sqlite3
from models import LikePost

conn=sqlite3.connect('login.db')

c=conn.cursor()

#c.execute("""CREATE TABLE login
#(
#    username text,
#     password text
# )""")

#c.execute("INSERT INTO login VALUES('Saanvi','pwd4@Soc123')")
#conn.commit()

like_1=LikePost('10','Sahana')
like_2=LikePost('110','Saanvi')
print(like_1.post_id)
print(like_2.post_id)
print(like_2.username)
print(like_1.username)

c.execute("SELECT * FROM login WHERE password='pwd4@Soc123'")
print(c.fetchall())



conn.commit()
conn.close()