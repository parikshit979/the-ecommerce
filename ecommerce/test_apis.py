import unittest
from run import create_app


class ProductTestCase(unittest.TestCase):
    """This class represents the products test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.app.testing = True
        self.client = self.app.test_client()

    def test_api_get_all_products(self):
        """Test API can get all products (GET request)."""

        res = self.client.get('/api/products/')
        self.assertEqual(res.status_code, 200)

    def test_api_filter_products(self):
        """Test API can get all products (GET request)."""

        # category, brand, source, subcategory, title
        data = {"category": "Men's Clothing", "brand": "Campus Sutra"}
        res = self.client.get('/api/products/', data=data)
        self.assertEqual(res.status_code, 200)

    def test_api_get_product_by_sku(self):
        """Test API can get products by sku (GET request)."""

        res = self.client.get('/api/products/SDL197918102')
        self.assertEqual(res.status_code, 200)

    def test_api_update_products(self):
        """Test API products update (PUT request)"""

        data = {"category": "Men's Clothing", "brand": "Campus Sutra"}
        res = self.client.put('/api/products/SDL197918102', data=data)
        self.assertEqual(res.status_code, 201)

    def test_api_get_products_discounts(self):
        """Test API can get products discounts (GET request)."""

        res = self.client.get('/api/products/discounts')
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
