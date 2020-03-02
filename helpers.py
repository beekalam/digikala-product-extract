import json
import psycopg2
import config


# database
def get_db():
    dsn = 'dbname={} user={} password={}'.format(
        config.db['database'],
        config.db['user'],
        config.db['password'],
    )
    conn = psycopg2.connect(dsn)
    return conn


def insert_product(product):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""insert into products(name , category,product_id ,seller,seller_price,features,name_from_title)
                               values(%s,%s,%s,%s,%s,%s,%s)""",
                (product['name'], product['category'], product['product_id'], product['seller'], product['price'],
                 json.dumps(product['features']), product['product_title']))
    conn.commit()
    cur.close()
    conn.close()


def has_product(product_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("select count(*) from products where product_id='{}'".format(product_id))
    product_count = cur.fetchone()
    cur.close()
    conn.close()
    return product_count[0] > 0


def clean_persian_number(number):
    return number.replace("۰", "0").replace("۱", "1").replace("۲", "2").replace("۳", "3").replace("۴", "4") \
        .replace("۵", "5").replace("۶", "6").replace("۸", "8").replace("۷", "7").replace("۹", "9").replace(",", "")
