import time
from django.core.management import BaseCommand
from shop.models import Item, Category, Tag
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.db import transaction
from faker import Faker
from django.db.models import F

faker = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # category = Category(name='Book')
        # category.save()
        # print(category.id)
        
        # category = Category.objects.create(name='Phones')
        # print(category)
        # print(category.id)
        
        # start = time.time()
        # for _ in range(1000):
        #     Category.objects.create(name=faker.word())
        # end = time.time()
        # print(end-start)
        
        # start = time.time()
        
        # categories = []
        
        # for _ in range(1000):
        #     category = Category(name=faker.word())
        #     categories.append(category)
            
        # Category.objects.bulk_create(categories)
        # end = time.time()
        # print(end-start)
        
        # for_delete = Category.objects.filter(id__gt=500)
        # for_delete.delete()
        # self.create_randoms(10)
        self.pricier()
        
    def create_randoms(self, num, with_bulk=True):
        start = time.time()
        items = []
        category = Category.objects.first()
        
        if with_bulk:
            for _ in range(num):
                item = Item(name=faker.word(), price = faker.random_int(), category=category)
                items.append(item)
            Item.objects.bulk_create(items)    
        
        else:
             for _ in range(num):
                Item.objects.create(name=faker.word(), price = faker.random_int())
        end = time.time()
        print(end-start)
        
    def pricier(self):
        items_to_price = Item.objects.filter(id__gt=500)
        items_to_price.update(price=F('price') * 1.1)

            
                
        
