from .models import Product
from django.db.models import Avg, Max
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    @classmethod  
    def find_by_model(cls, model): 
        return Product.objects.get(model=model)
    @classmethod
    def last_record(cls):
        return Product.objects.last()
        
    @classmethod
    def by_rating(cls, rate):
        return Product.objects.filter(rating=rate)
    @classmethod
    def by_rating_range(cls, start, end):
        return Product.objects.filter(rating__gte=start, rating__lte=end)
    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating=rating, color=color)

    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(rating=rating) | Product.objects.filter(color=color)

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()

    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(price_cents__lt=price) | Product.objects.filter(rating__gt=rating)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, name):
        return Product.objects.filter(manufacturer__contains=name)
    
    @classmethod
    def manufacturer_names_for_query(cls, name):
        manufacturers = Product.objects.filter(manufacturer__contains=name).values('manufacturer')
        manufacturers_list = []
        for name in manufacturers:
            manufacturers_list.append(name['manufacturer'])
        return manufacturers_list
    
    @classmethod
    def not_in_a_category(cls, name):
        return Product.objects.exclude(category=name)
    
    @classmethod
    def limited_not_in_a_category(cls, name, limit):
        return Product.objects.exclude(category=name)[:3]

    @classmethod
    def category_manufacturers(cls, category):
        manufacturers = Product.objects.filter(category=category).values('manufacturer')
        manufacturers_list = []
        for name in manufacturers:
            manufacturers_list.append(name['manufacturer'])
        return manufacturers_list

    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(category=category).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        longest_name = Product.objects.order_by(Length('model').desc())[0]
        return longest_name.id

    @classmethod
    def ordered_by_model_length(cls):
        # return Product.objects.all().order_by(Length('model').asc())
        return Product.objects.extra(select={'length':'Length(model)'}).order_by('length')