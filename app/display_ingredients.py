import pymysql
import random
import sys

def display_ingredients(category):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='care_products')
    cur = conn.cursor()
    cur.execute("""
    SELECT ingredient
    FROM category_ingredients
    WHERE concern='high' AND category='%s'
    ORDER BY proportion DESC
    LIMIT 10;""" % category)
    sql_output = cur.fetchall()
    cur.close()
    conn.close()
    if len(sql_output) > 0:
        displayed = [res[0] for res in sql_output]
    else:
        displayed = ['fragrance']
    return displayed
    
    

def get_id_category(category):    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='care_products')
    cur = conn.cursor()
    cur.execute("""
    SELECT id_category, category
    FROM products
    WHERE category='%s'
    GROUP BY category;""" % category)
    sql_output = cur.fetchall()
    cur.close()
    conn.close()
    id_categ = sql_output[0][0]
    categ = sql_output[0][1]
    result = str(id_categ) + '-' +  categ
    href = 'http://www.goodguide.com/products?category_id=' + result + '&sort_order=DESC'
    return href


def get_recommendations(category):    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='care_products')
    cur = conn.cursor()
    cur.execute("""
    SELECT product
    FROM products
    WHERE category='%s' AND health>8
    ORDER BY health DESC
    LIMIT 25;""" % category)
    sql_output = cur.fetchall()
    cur.close()
    conn.close()
    query_products = [res[0] for res in sql_output]
    sample_size = min(len(query_products) , 5)
    sample = random.sample(range(len(query_products)), sample_size)
    recom_products = []
    for s in sample:
        recom_products.append(query_products[s])
    return recom_products

