from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Специи', 'description': 'Пряности, специи, перцы'},
            {'name': 'Молочка', 'description': 'Молоко, сыры'},
        ]
        category_for_creation = [Category(**category) for category in category_list]
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_creation)
        product_list = [
            {'name': 'Черный перец', 'description': 'Черный перец молотый',
             'category': Category.objects.get(name='Специи'), 'price': 50},
            {'name': 'Простоквашино', 'description': 'Молоко 2.5%',
             'category': Category.objects.get(name='Молочка'), 'price': 70},
            {'name': 'Село Зеленое', 'description': 'Сыр Бри', 'category': Category.objects.get(name='Молочка'),
             'price': 120},
        ]
        product_for_creation = [Product(**product) for product in product_list]
        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_creation)
