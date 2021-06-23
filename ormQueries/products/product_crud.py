from django.db.models.aggregates import Avg, Max
from .models import Product 
from django.db.models import Q
from django.db.models.functions import Length


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_val):
        return Product.objects.get(model = model_val)

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rating_val):
        return Product.objects.filter(rating = rating_val)

    @classmethod
    def by_rating_range(cls, lb, ub):
        return Product.objects.filter(rating__gte = lb, rating__lte = ub)

    @classmethod
    def by_rating_and_color(cls, rating_val, color_val):
        return Product.objects.filter(rating = rating_val, color = color_val)

    @classmethod
    def by_rating_or_color(cls, rating_val, color_val):
        return Product.objects.filter(Q(rating = rating_val) | Q(color = color_val))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color = None).count()

    @classmethod
    def below_price_or_above_rating(cls, price_val, rating_val):
        return Product.objects.filter(Q(price_cents__lte = price_val) | Q(rating__gte = rating_val))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.all().order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, name_val):
        return Product.objects.filter(manufacturer__contains = name_val)

    @classmethod
    def manufacturer_names_for_query(cls, name_val):
        return Product.objects.filter(manufacturer__contains = name_val).values_list('manufacturer', flat = True)

    @classmethod
    def not_in_a_category(cls, name_val):
        return Product.objects.exclude(category = name_val)

    @classmethod
    def limited_not_in_a_category(cls, name_val, limit):
        return Product.objects.exclude(category = name_val)[:limit]

    @classmethod
    def category_manufacturers(cls, name_val):
        return Product.objects.filter(category = name_val).values_list('manufacturer', flat = True)

    @classmethod
    def average_category_rating(cls, name_val):
        return Product.objects.filter(category = name_val).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.annotate(model_name_len = Length('model')).order_by('-model_name_len').values_list('id', flat = True)[0]

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.annotate(model_name_len = Length('model')).order_by('model_name_len')