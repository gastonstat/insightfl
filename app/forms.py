from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField, IntegerField
from wtforms.validators import Required


category_menu = [('--select--', '--select--'),
('after-shave', 'after-shave'),
('anti-aging', 'anti-aging'),
('baby-lotion', 'baby-lotion'),
('baby-shampoo', 'baby-shampoo'),
('baby-soap-bath', 'baby-soap-bath'),
('baby-sunscreen', 'baby-sunscreen'),
('baby-wipes', 'baby-wipes'),
('body-wash-cleanser', 'body-wash-cleanser'),
('bubble-bath', 'bubble-bath'),
('concealer-foundation', 'concealer-foundation'),
('conditioner', 'conditioner'),
('dental-floss', 'dental-floss'),
('deodorants-antiperspirants-mens', 'deodorants-antiperspirants-mens'),
('deodorants-antiperspirants-womens', 'deodorants-antiperspirants-womens'),
('eye-makeup', 'eye-makeup'),
('feminine-moisturizer', 'feminine-moisturizer'),
('feminine-powder_deodorant', 'feminine-powder_deodorant'),
('foot-care', 'foot-care'),
('fragrance-for-men', 'fragrance-for-men'),
('fragrance-for-women', 'fragrance-for-women'),
('hair-spray', 'hair-spray'),
('hand-sanitizer', 'hand-sanitizer'),
('lipstick-lip-gloss-balm', 'lipstick-lip-gloss-balm'),
('moisturizer', 'moisturizer'),
('mouthwash', 'mouthwash'),
('nail-polish', 'nail-polish'),
('personal-cleansing', 'personal-cleansing'),
('scrubs-oils-powders', 'scrubs-oils-powders'),
('shampoo', 'shampoo'),
('shaving-cream', 'shaving-cream'),
('soap', 'soap'),
('sunless-tanning', 'sunless-tanning'),
('sunscreen-below-spf-15', 'sunscreen-below-spf-15'),
('sunscreen-spf-15-above', 'sunscreen-spf-15-above'),
('tanning-oil', 'tanning-oil'),
('toothpaste',  'toothpaste')]


class CategoryForm(Form):
    category = SelectField('category', 
                    choices=category_menu)
    number_ingredients = IntegerField('number_ingredients', default = 0, validators=[Required("Integer")])
    has_toxics = SelectField('has_toxics', 
                    choices=[('no', 'no'),
                            ('yes', 'yes')])


#class ChafaForm(Form):
#    category = SelectField('category', 
#                    choices=[('select', 'select'), 
#                            ('baby-shampoo', 'baby-shampoo'), 
#                            ('baby-lotion', 'baby-lotion'), 
#                            ('baby-sunscreen', 'baby-sunscreen'), 
#                            ('baby-wipes', 'baby-wipes'),
#                            ('dental-floss', 'dental-floss'),
#                            ('mouthwash', 'mouthwash')])
#    number_ingredients = IntegerField('number_ingredients', default = None, validators=[Required("Integer")])
#    has_triclosan = BooleanField('has_triclosan', default = False)
#    has_fragrance = BooleanField('has_fragrance', default = False)
    
#    def validate_number_ingredients(self, field):
#        if field.data < 0:
#            raise ValidationError("Number of ingredients must be positive")
#        if field.data > 200:
#            raise ValidationError("Too many ingredients")


class LoginForm(Form):
    #openid = TextField('openid', validators = [Required()])
    openid = TextField('openid')
    remember_me = BooleanField('remember_me', default = False)