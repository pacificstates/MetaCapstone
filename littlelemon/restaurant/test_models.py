from django.test import TestCase
from .models import Menu
from rest_framework.test import APIClient
from .serializers import MenuSerializer
from django.contrib.auth.models import User
from django.urls import reverse

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # create test instances of menu items
        self.menu_item1 = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.menu_item2 = Menu.objects.create(title='Burger', price=120, inventory=50)

        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # give the test client/user authentication
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_getall(self):
        url = reverse('menu-items')
        response = self.client.get(url)

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.data, serializer.data)
