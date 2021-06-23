from django.db.models.aggregates import Avg, Max, Count
from .models import Product
from django.db.models import Q
from django.db.models.functions import Lower, Length


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, product_model_name):
        return Product.objects.get(
            model__exact=product_model_name
        )  # get() because test expect one record...

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating__exact=rating)

    @classmethod
    def by_rating_range(cls, rating_start, rating_end):
        return Product.objects.filter(rating__range=(rating_start, rating_end))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) & Q(color=color))

    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) | Q(color=color))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__exact=None).count()

    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(price_cents__lt=price) | Product.objects.filter(
            rating__gt=rating
        )

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by(Lower("category"), "-price_cents")

    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer):
        return Product.objects.filter(manufacturer__contains=manufacturer)

    @classmethod
    def manufacturer_names_for_query(cls, manufacturer_query):
        return Product.objects.filter(
            manufacturer__contains=manufacturer_query
        ).values_list("manufacturer", flat=True)

    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.exclude(category=category)

    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        return Product.objects.exclude(category=category)[:limit]

    @classmethod
    def category_manufacturers(cls, category):
        return Product.objects.filter(category__exact=category).values_list(
            "manufacturer", flat=True
        )

    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(category__exact=category).aggregate(Avg("rating"))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max("price_cents"))

    @classmethod
    def longest_model_name(cls):
        return (
            Product.objects.values("id")
            .annotate(model_len=Length("model"))
            .order_by("-model_len")[0]["id"]
        )

    @classmethod
    def ordered_by_model_length(cls):
        return (
            Product.objects.values("model")
            .annotate(letter_count=Length("model"))
            .order_by("letter_count")
        )
