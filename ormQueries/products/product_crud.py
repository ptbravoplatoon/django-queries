from .models import Product 

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model):
        return Product.objects.get(model__exact=model)

    @classmethod
    def last_record(cls):
        return Product.objects.all().last()

    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating__exact=rating)

    @classmethod
    def by_rating_range(cls, val1, val2):
        return Product.objects.filter(rating__range=(val1, val2))

    @classmethod
    def by_rating_and_color(cls,rating, color):
        return Product.objects.filter(rating__exact=rating, color__exact=color)
        
    @classmethod
    def by_rating_or_color(cls, rating, color):
        from django.db.models import Q
        return Product.objects.filter(Q(rating__exact=rating) | Q(color__exact=color))
        
    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()
        
    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        from django.db.models import Q
        return Product.objects.filter(Q(price_cents__lt=price) | Q(rating__gt=rating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')
        
    @classmethod
    def products_by_manufacturer_with_name_like(cls, val):
        return Product.objects.filter(manufacturer__icontains=val)
        
    @classmethod
    def manufacturer_names_for_query(cls, val):
        return Product.objects.filter(manufacturer__icontains=val).values_list('manufacturer', flat=True)
        
    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.exclude(category__exact=category)
        
    @classmethod
    def limited_not_in_a_category(cls, category, count):
        return Product.objects.exclude(category__exact=category)[:count]
        
    @classmethod
    def category_manufacturers(cls, category):
        return Product.objects.filter(category__exact=category).values_list('manufacturer', flat=True).distinct()
        
    @classmethod
    def average_category_rating(cls, category):
        from django.db.models import Avg
        return Product.objects.filter(category__exact=category).aggregate(Avg('rating'))
        
    @classmethod
    def greatest_price(cls):
        from django.db.models import Max
        return Product.objects.all().aggregate(Max('price_cents'))
        
    @classmethod
    def longest_model_name(cls):
        from django.db.models.functions import Length
        return Product.objects.all().order_by(Length('model').desc()).values_list('id', flat=True)[0]
        
    @classmethod
    def ordered_by_model_length(cls):
        from django.db.models.functions import Length
        return Product.objects.all().order_by(Length('model'))
        
    