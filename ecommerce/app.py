from flask import Blueprint
from flask_restful import Api
from resources.product import Product, \
    ProductList, ProductDiscount

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ProductList, '/products')
api.add_resource(Product, '/products/<string:sku>')
api.add_resource(ProductDiscount, '/products/discounts')
