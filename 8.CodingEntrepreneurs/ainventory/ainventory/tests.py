from django.test import TestCase
from django.conf import settings 
import os 
from django.contrib.auth.password_validation import validate_password
class ainventoryCongfigTest(TestCase):
    def test_secret_key_strength(self):
        #settings.SECRET_KEY 
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Bad Secret key {e.messages}'
            self.fail(msg)