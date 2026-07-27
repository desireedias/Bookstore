import factory

from order.models import Order
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = factory.Faker('user_name')


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
        skip_postgeneration_save=True 


    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **Kwards):
        if not create:
            return
        
        if extracted:
            for product in extracted:
                self.product.add(product)