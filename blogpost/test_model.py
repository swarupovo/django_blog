from django.test import TestCase
from model_mommy import mommy
from model_mommy.recipe import Recipe,foreign_key

from .models import Blogger

class KidTestModel(TestCase):
    """
    Class to test the model
    Kid
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.kid = mommy.make(Blogger)