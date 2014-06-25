import pymysql
import sys


cluster_avoid = ['after-shave','anti-aging','baby-sunscreen','baby-wipes',
'concealer-foundation','eye-makeup','foot-care','fragrance-for-men','fragrance-for-women',
'hand-sanitizer','moisturizer','sunless-tanning','sunscreen-below-spf-15',
'sunscreen-spf-15-above','tanning-oil']

cluster_average = ['after-shave','baby-wipes','bubble-bath','concealer-foundation',
'conditioner','deodorants-antiperspirants-mens','deodorants-antiperspirants-womens',
'eye-makeup','feminine-moisturizer','feminine-powder_deodorant','foot-care',
'fragrance-for-men','fragrance-for-women','hair-spray','moisturizer','mouthwash',
'personal-cleansing','scrubs-oils-powders','shaving-cream','sunless-tanning',
'sunscreen-below-spf-15','tanning-oil','toothpaste']

cluster_ok = ['after-shave','baby-wipes','conditioner','deodorants-antiperspirants-mens',
'deodorants-antiperspirants-womens','feminine-moisturizer','foot-care','fragrance-for-men',
'fragrance-for-women','hair-spray','mouthwash','personal-cleansing','shaving-cream',
'sunless-tanning','tanning-oil']


def compute_score(category, num_ings, has_toxic):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='care_products')
    cur = conn.cursor()
    cur.execute("""
    SELECT ROUND(AVG(health))
    FROM products
    WHERE category='%s';""" % category)
    returned_score = cur.fetchall()
    cur.close()
    conn.close()
    tmp_score = int(round(returned_score[0][0]))
    
    if has_toxic == 'yes':
        final_score = '0'
    else:
        if num_ings >= 15:
            if category in cluster_avoid:
                if num_ings >= 21:
                    final_score = 2
                else:
                    final_score = 3
            else:
                if num_ings >= 21:
                    final_score = 4
                else:
                    final_score = 5
        else:
            if num_ings >= 10:
                if category in cluster_average:
                    final_score = 5
                else:
                    final_score = 7
            else:
                if num_ings == 0:
                    final_score = tmp_score
                else:
                    if category in cluster_ok:
                        final_score = 6
                    else:
                        if num_ings > 5:
                            final_score = 7
                        else:
                            final_score = 8
    return final_score
    
 