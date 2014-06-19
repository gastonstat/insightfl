import pymysql
import sys


cluster_avoid = ['after-shave','anti-aging','baby-wipes','concealer-foundation','eye-makeup',
'feminine-moisturizer','foot-care','fragrance-for-men','fragrance-for-women',
'hand-sanitizer','moisturizer','sunless-tanning','sunscreen-below-spf-15',
'sunscreen-spf-15-above','tanning-oil']

cluster_average = ['after-shave','baby-wipes','deodorants-antiperspirants-mens',
'feminine-moisturizer','fragrance-for-men','fragrance-for-women','feminine-moisturizer',
'fragrance-for-men','fragrance-for-women','hair-spray','mouthwash','shaving-cream',
'sunless-tanning','tanning-oil']


def compute_score(category, num_ings, has_toxic):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='care_products')
    cur = conn.cursor()
    cur.execute("""
    SELECT ROUND(AVG(health), 2)
    FROM products
    WHERE category='%s';""" % category)
    returned_score = cur.fetchall()
    cur.close()
    conn.close()
    tmp_score = returned_score[0][0]
    
    if has_toxic == 'yes':
        final_score = '0.0'
    else:
        if num_ings >= 16:
            if category in cluster_avoid:
                final_score = 2
            else:
                final_score = 4
        else:
            if num_ings >= 10:
                final_score = 5
            else:
                if num_ings == 0:
                    final_score = tmp_score
                else:
                    if category in cluster_average:
                        final_score = 5
                    else:
                        final_score = 7
    return final_score
    
 