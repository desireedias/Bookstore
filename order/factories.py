import factory

from order.models import Order
from django.contrib.auth.models import User

class UseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('pystr')
    username = factory.Faker('pystr')


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order


    user = factory.Subfactory(UseFactory)

    @factory.post_generation
    def product(self, create, extracted, **Kwards):
        if not create:
            return
        
        if extracted:
            for product in extracted:
                self.product.add(product)