from django.conf import settings
from django.test import Client, TestCase


class SEOEndpointTests(TestCase):
    def setUp(self):
        self.client = Client(HTTP_HOST='www.zaskotechsolutions.co.ke')

    def test_robots_allows_public_pages_and_blocks_admin(self):
        response = self.client.get('/robots.txt')

        self.assertEqual(response.status_code, 200)
        body = response.content.decode()
        self.assertIn('Allow: /', body)
        self.assertIn('Disallow: /admin/', body)
        self.assertIn(f'{settings.SITE_URL}/sitemap.xml', body)

    def test_sitemap_contains_public_canonical_urls(self):
        response = self.client.get('/sitemap.xml')

        self.assertEqual(response.status_code, 200)
        body = response.content.decode()
        self.assertIn(f'{settings.SITE_URL}/', body)
        self.assertIn(f'{settings.SITE_URL}/services/', body)
        self.assertNotIn('/admin/', body)

    def test_starter_route_redirects_to_canonical_homepage(self):
        response = self.client.get('/starter/')

        self.assertRedirects(response, '/')
