import factory

from product.models import Category
from product.models import Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        skip_postgeneration_save = True

    price = factory.Faker("pyint")
    title = factory.Faker("pystr")

    @factory.post_generation
    def category(self, create, extracted, **Kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

        else:
            self.category.add(CategoryFactory())
