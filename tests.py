from django.test import TestCase

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurantsite.settings")

import django
django.setup()
from django.db import connection
import pandas as pd

from django.core.management import call_command
from django.test import TestCase
from customer.models import Item, Order, User

# def product_list(request):
products = Item.objects.raw("SELECT * FROM customer_category where name = 'Beverages'")
for item in products:
    print(item.name)
# Connect to MySQL
cursor = connection.cursor()
users = cursor.execute("SELECT * FROM customer_user")
data = cursor.fetchall()
for user in data:
    print("print 1st element")
    print(user[0])

df = pd.DataFrame(data)
print("Does not show column names")
print(df)
column_names = [desc[0] for desc in cursor.description]
print(column_names)
df.columns = column_names
print("shows column names")
print(df)