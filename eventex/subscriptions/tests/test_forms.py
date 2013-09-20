# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeFormTest(TestCase):
    def test_form_has_fiels(self):
        'Form must have 4 fiels.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
