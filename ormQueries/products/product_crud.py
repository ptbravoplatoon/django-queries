from .models import Product 
from django.db.models import Q

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        all_entries = Product.objects.all()
        return all_entries

    @classmethod
    def get_query_ids(cls, product_id):
        product_ids = Product.objects.filter(pk=product_id).values_list('id', flat=True)
        return product_ids

    @classmethod
    def find_by_model(cls, model_name):
        product = Product.objects.get(model=model_name)
        return product

    @classmethod
    def last_record(cls):
        last_product = Product.objects.all().last()
        # last_product = Product.objects.latest('pk') - another option
        return last_product

    @classmethod
    def by_rating(cls, product_rating):
        specific_rating = Product.objects.filter(rating=product_rating)
        return specific_rating

    @classmethod
    def by_rating_range(cls, lower_range, upper_range):
        products_in_range = Product.objects.filter(rating__range=(lower_range, upper_range))
        return products_in_range

    @classmethod
    def by_rating_and_color(cls, product_rating, product_color):
        product_ids = Product.objects.filter(rating=product_rating).filter(color=product_color)
        return product_ids

    @classmethod
    def by_rating_or_color(cls, product_rating, product_color):
        # product_ids = Product.objects.filter(rating=product_rating|color=product_color)
        product_ids = Product.objects.filter(Q(rating=product_rating) | Q(color=product_color))
        return product_ids

    @classmethod
    def no_color_count(cls):
        colorless_products = Product.objects.filter(color__isnull=True).count()
        return colorless_products

    @classmethod
    def below_price_or_above_rating(cls, product_price, product_rating):
        product_ids = Product.objects.filter(Q(price_cents__lt=product_price) | Q(rating__gt=product_rating)).values_list('id', flat=True)
        return product_ids

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        product_ids = Product.objects.all().order_by('category', '-price_cents')
        return product_ids

    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer_name):
        product_ids = Product.objects.filter(manufacturer__contains=manufacturer_name)
        return product_ids

    @classmethod
    def manufacturer_names_for_query(cls, manufacturer_name):
        manufacturer_names = Product.objects.values_list('manufacturer', flat=True).filter(manufacturer__contains=manufacturer_name)
        return manufacturer_names

    @classmethod
    def not_in_a_category(cls, product_category):
        product_ids = Product.objects.exclude(category='Garden')
        return product_ids
