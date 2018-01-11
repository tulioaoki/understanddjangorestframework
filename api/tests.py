from django.test import TestCase

class SubscriptionTest(TestCase):
    def test_str(self):
        self.assertEqual('Nome Sobrenome', str(self.obj))