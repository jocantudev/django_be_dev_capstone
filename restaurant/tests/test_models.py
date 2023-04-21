from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Sandwich", price=2, inventory=4)
        self.assertEqual(item.title, "Sandwich")
        self.assertEqual(item.price, 2)
        self.assertEqual(item.inventory, 4)