from django.test import TestCase
from Posts.models import Blog

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTest: set up test for all non-modified class methods.")
        pass

    def setUp(self):
        print("setUp: test the test method to setup data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)



    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)



class PostsModelTest(TestCase):
    @classmethod





    def test_title(self):
        max_length = Blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_pubdate(self):
        field_label = Blog._meta.get_field('pub_date').verbose_name
        self.assertEquals(field_label, 'date published')

    def test_body(self):
        field_label = Blog._meta.get_field('body')
        self.assertEquals(field_label,field_label)



