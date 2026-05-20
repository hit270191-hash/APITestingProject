from faker import Faker
import random

from datamodels.Product import Product

class Payload:
    faker = Faker()
    categories= ["electronics", "fitness", "home", "furniture", "wearables"]

    def product_payload(self):

        title = self.faker.unique.catch_phrase()
        price = float(self.faker.pricetag().replace("$","").replace(",", ""))
        description = self.faker.sentence()
        category= random.choice(self.categories)
        stock = random.randint(1,100)
        return Product(title, price, description, category, stock)

