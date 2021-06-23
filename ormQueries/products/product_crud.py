from .models import Product 
from django.db.models import Q, Avg, Max

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    def find_by_model(modelName):
        return Product.objects.get(model=modelName)

    def last_record():
        return Product.objects.latest('id')

    def by_rating(ratingNum):
        return Product.objects.filter(rating=ratingNum)

    def by_rating_range(low, high):
        return Product.objects.filter(rating__gte=low, rating__lte=high)

    def by_rating_and_color(ratingNum, prodColor):
        return Product.objects.filter(rating=ratingNum, color=prodColor)

    def by_rating_or_color(ratingNum, prodColor):
        return Product.objects.filter(Q(rating=ratingNum) | Q(color=prodColor))

    def no_color_count():
        return Product.objects.filter(color__isnull=True).count()

    def below_price_or_above_rating(belowPrice, aboveRating):
        return Product.objects.filter(Q(price_cents__lt=belowPrice) | Q(rating__gt=aboveRating))

    def ordered_by_category_alphabetical_order_and_then_price_decending():
        return Product.objects.all().order_by('category', '-price_cents')

    def products_by_manufacturer_with_name_like(nameLike):
        return Product.objects.filter(manufacturer__icontains=nameLike)

    def manufacturer_names_for_query(nameLike):1
        raw_result = Product.objects.filter(manufacturer__icontains=nameLike).values('manufacturer')
        result = []
        for entry in raw_result:
            group = entry.get('manufacturer')
            result.append(group)
        return result

    def not_in_a_category(notCat):
        return Product.objects.filter(~Q(category=notCat))

    def limited_not_in_a_category(notCat, limit):
        return Product.objects.filter(~Q(category=notCat))[:limit]

    def category_manufacturers(cat):
        raw_result = Product.objects.filter(category__icontains=cat).values('manufacturer')
        result = []
        for entry in raw_result:
            group = entry.get('manufacturer')
            result.append(group)
        return result

    def average_category_rating(cat):
        return Product.objects.filter(category=cat).aggregate(Avg('rating'))

    def greatest_price():
        return Product.objects.all().aggregate(Max('price_cents'))

    def longest_model_name():
        return Product.objects.extra(select={'length':'Length(model)'}).order_by('-length')[:1][0].id

    def ordered_by_model_length():
        return Product.objects.extra(select={'length':'Length(model)'}).order_by('length')