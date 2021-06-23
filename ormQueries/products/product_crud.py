from django.db.models.query_utils import Q
from .models import Product 

class ProductCrud:
    #test 1 complete
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    
    #test 2 complete
    @classmethod
    def find_by_model(cls,model_name):
        return Product.objects.get(model=model_name)#f"{model_name}")

    #test 3 complete
    @classmethod
    def last_record(cls):
        return Product.objects.latest('id')

    #test 4 complete
    def by_rating(rating):
        return Product.objects.filter(rating=f"{rating}")

    #test 5 complete
    def by_rating_range(start,end):
        return Product.objects.filter(rating__gte=f"{start}", rating__lte=f"{end}")

    #test 6 complete
    @classmethod
    def by_rating_and_color(cls,rating,color):
        return Product.objects.filter(rating=rating,color=color)
    
    #test 7 complete
    @classmethod
    def by_rating_or_color(cls,rating_,color_):
        return Product.objects.filter(Q(rating=rating_) | Q(color=color_))


    #test 8 complete
    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()



