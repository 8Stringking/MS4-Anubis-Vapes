from django.test import TestCase


class TestViews(TestCase):

    """
    this test is to check that the index view is rendering
    the correct template when used
    """

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
