from flask import render_template
from app import app, host, port, user, passwd, db
from app.helpers.database import con_db
from app.compute_score import compute_score
from app.display_ingredients import display_ingredients, get_id_category, get_recommendations
from forms import CategoryForm, LoginForm

from flask import flash, redirect, request

import pymysql
import json


# To create a database connection, add the following
# within your view functions:
# con = con_db(host, port, user, passwd, db)


# ROUTING/VIEW FUNCTIONS
# routes define the content to be served in our website
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/slides')
def slides():
    # Renders slides.html.
    return render_template('slides.html')

@app.route('/about')
def about():
    # Renders about.html.
    return render_template('about.html')

@app.route('/graph')
def graph():
    # Renders graph.html.
    return render_template('graph.html')

@app.route('/plot')
def plot():
    # Renders plot.html.
    return render_template('plot.html')

@app.route('/scatter')
def scatter():
    # Renders scatter.html.
    return render_template('scatter.html')

@app.route('/barchart')
def barchart():
    # Renders barchar.html.
    return render_template('barchart.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/score', methods = ['GET', 'POST'])
def category():
    # generate forms and get requests
    form = CategoryForm(csrf_enabled = False)
    category_data = form.category.data
    score = False
    error_text = False
    id_cat = False
    recom = False
    #if request.form.get('continue', None) == 'Fill Info':
    if category_data == '--select--':
        return render_template('score.html', form=form, ings=False, score=False, 
            error_text=error_text, id_cat=id_cat, recom=recom)
    else:
        ings = display_ingredients(category_data)
        if request.form.get('continue', None) == 'Fill Info':
            form.number_ingredients.data = ''
            return render_template('score.html', form=form, ings=ings, score=False, 
                error_text=error_text, id_cat=id_cat, recom=recom)
        else:
            if request.form.get('submit', None) == 'Get Score':
                # check toxic selection
                if form.has_toxics.data == 'select':
                    error_text = "Indicate ingredients"
                    return render_template('score.html', form=form, ings=ings, score=False, 
                        error_text=error_text, id_cat=id_cat, recom=recom)
                else:
                    number_ingredients = form.number_ingredients.data
                    if number_ingredients is None:
                        number_ingredients = 0
                    has_toxic = form.has_toxics.data
                    score = compute_score(category_data, number_ingredients, has_toxic)
                    id_cat = get_id_category(category_data)
                    return render_template('score.html', form=form, ings=ings, score=score, 
                        error_text=error_text, id_cat=id_cat, recom=recom)
            else:
                if request.form.get('submit', None) == 'Show Recom':
                    number_ingredients = form.number_ingredients.data
                    has_toxic = form.has_toxics.data
                    score = compute_score(category_data, number_ingredients, has_toxic)
                    id_cat = get_id_category(category_data)
                    recom = get_recommendations(category_data)
                    return render_template('score.html', form=form, ings=ings, score=score, 
                        error_text=error_text, id_cat=id_cat, recom=recom)
    return render_template('score.html', form=form, ings=False, score=False, 
    error_text=error_text, id_cat=id_cat, recom=recom)



#@app.route('/score', methods = ['GET', 'POST'])
#def score():
#    # generate forms and get requests
#    #add_form = TestForm(csrf_enabled = False)
#    form = TestForm(csrf_enabled = False)
#    #score = []
#    category_data = form.category.data
#    if category_data != 'select':
#        number_ingredients = form.number_ingredients.data
#        triclosan_flag = form.has_triclosan
#        fragrance_flag = form.has_fragrance.data
#        error_text = ""            
#        category = form.category.data
#        score = compute_score(category, number_ingredients)
#        if fragrance_flag:
#            score = str(0.0)
#        return render_template('score.html', form=form, score=score, error_text=error_text)
#    else:
#        score = ""
#        error_text = "Please select a category"
#        return render_template('score.html', form=form, score=score, error_text=error_text)
#    return render_template('score.html', form=form, score=score, error_text=error_text)







#    # check number of ingredients 
#    if number_ingredients:
#        if isinstance(number_ingredients, int):
#            if (number_ingredients < 0):
#                error_text = "Incorrent number of ingredients"
#                return render_template('/score', form=form, error_text=error_text)




#@app.route('/login', methods = ['GET', 'POST'])
#def login():
#    add_form = LoginForm(csrf_enabled = False)
#    form = LoginForm(csrf_enabled = False)
#    if form.validate_on_submit():
#        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
#        return redirect('/index')
#    return render_template('score.html', 
#        title = 'Score it',
#        form = form,
#        add_form = add_form)


#### new stuff to handle the MySQL database
#@app.route("/db")
#def baby_sunscreen():
#    db.query("SELECT product FROM products WHERE category = 'baby-sunscreen' AND has_high = 1;")
#    query_results = db.store_result().fetch_row(maxrows=0)
#    cities = ""
#    for result in query_results:
#    	cities += unicode(result[0], 'utf8')
#    	cities += "<br>"
#    return cities


#### Query to display product categories
#SELECT category
#FROM products
#GROUP BY category;

