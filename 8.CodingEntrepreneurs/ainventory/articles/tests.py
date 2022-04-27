from django.test import TestCase
from .utils import my_slugify
# Create your tests here.
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 1
        a1 = Article.objects.create(title='hej ho', content='something else')
        self.slug = a1.slug
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())
    def test_querysey_count(self):
        qs=Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)
    def test_hello_world_slug(self):
        obj = Article.objects.all().last()
        slug=obj.slug
        self.assertEqual(slug, self.slug)
    def test_my_slugify(self):
        obj=Article.objects.all().last()
        new_slugs = [my_slugify(obj) for i in range(0,5)]
        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))
    def test_article_search_manager(self):
        qs = Article.objects.search(query='hej ho')
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query='ej')
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query='something else')
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query='ome')
        self.assertEqual(qs.count(), self.number_of_articles)