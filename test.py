from helpers import get_db
import json

conn = get_db()
cur = conn.cursor()
cur.execute("select features from products where product_id=45")
product = cur.fetchone()[0]
for (k, v) in product.items():
    print(k)
    print(v)
    print("=============")
# print(product.keys())
# print(product['اقلام همراه هارد دیسک'])
# print(product.keys())
