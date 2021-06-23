from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    
    @classmethod
    def find_by_model(cls, modelFilter):
        return Product.objects.get(model=modelFilter)

    @classmethod
    def last_record(cls):
        return Product.objects.order_by("id").reverse()[0]

    @classmethod
    def by_rating(cls, ratingFilter):
        return Product.objects.filter(rating=ratingFilter)

    @classmethod
    def by_rating_range(cls, lower, upper):
        return Product.objects.filter(rating__gte=lower, rating__lte=upper)

    @classmethod
    def by_rating_and_color(cls, ratingFilter, colorFilter):
        return Product.objects.filter(rating=ratingFilter, color=colorFilter)

    @classmethod
    def by_rating_or_color(cls, ratingFilter, colorFilter):
        return Product.objects.filter(Q(rating=ratingFilter) | Q(color=colorFilter))

    @classmethod
    def no_color_count(cls):
        return len(Product.objects.filter(color=None))

    @classmethod
    def below_price_or_above_rating(cls, belowPrice, aboveRating):
        return Product.objects.filter(Q(price_cents__lt=belowPrice) | Q(rating__gt=aboveRating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category','-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, likeName):
        return Product.objects.filter(manufacturer__contains=likeName)

    @classmethod
    def manufacturer_names_for_query(cls, likeName):
        set = Product.objects.filter(manufacturer__contains=likeName)
        return [obj.manufacturer for obj in set]

    @classmethod
    def not_in_a_category(cls, categoryFilter):
        return Product.objects.filter(~Q(category=categoryFilter))

    @classmethod
    def limited_not_in_a_category(cls, categoryFilter, limit):
        return Product.objects.filter(~Q(category=categoryFilter))[:limit]

    @classmethod
    def category_manufacturers(cls, categoryFilter):
        set = Product.objects.filter(category=categoryFilter)
        return [obj.manufacturer for obj in set]

    @classmethod
    def average_category_rating(cls, categoryFilter):
        return Product.objects.filter(category=categoryFilter).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.annotate(model_length=Length('model')).order_by("-model_length")[0].id

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.annotate(model_length=Length('model')).order_by("model_length")
