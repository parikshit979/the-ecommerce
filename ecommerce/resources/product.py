import json
from flask import request

from dbconnector import DBConnector
from flask_restful import Resource

from settings import (DB_HOST, DB_PORT,
                      DB_USER, DB_PASSWORD)

db_inst = DBConnector(host=DB_HOST, username=DB_USER, password=DB_PASSWORD, port=DB_PORT)


class ProductList(Resource):
    def get(self):
        json_data = request.get_json(force=True)

        # category, brand, source, subcategory, title
        conditions = []
        for key, value in json_data.items():
            conditions.append("{key}='{value}'".format(key=key, value=value))
        if conditions:
            conditions = 'WHERE {cond}'.format(cond=" AND ".join(conditions))

        query = "SELECT sku,title,thumbnail,mrp,discount,stock FROM " \
                "dataweave_india.products {condition};".format(condition=conditions)
        result = db_inst.select_query_dict(query=query)

        return {'status': 'success', 'data': json.dumps(result)}, 200


class Product(Resource):
    def get(self, sku):
        query = "SELECT sku,title,thumbnail,mrp,discount,stock FROM " \
                "dataweave_india.products WHERE sku='{sku}';".format(sku=sku)
        result = db_inst.select_query_dict(query=query)

        return {'status': 'success', 'data': json.dumps(result)}, 200

    def put(self, sku):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        # brand, category, subcategory, product_type
        conditions = []
        for key, value in json_data.items():
            conditions.append("{key}='{value}'".format(key=key, value=value))
        if conditions:
            conditions = '{cond}'.format(cond=",".join(conditions))

        query = "UPDATE dataweave_india.products SET {condition} " \
                "WHERE sku='{sku}';".format(condition=conditions, sku=sku)
        db_inst.execute_single(query)

        return {'status': 'success'}, 201


class ProductDiscount(Resource):
    def get(self):
        query = "SELECT CONCAT(IFNULL(ranges.min, '-inf'), '-', IFNULL(ranges.max, 'inf')) AS `range`, " \
                "COUNT(discount) AS count FROM ( SELECT 0 AS min, 10 AS max UNION ALL " \
                "SELECT 10, 30 UNION ALL SELECT 30, 50 UNION ALL SELECT 50, NULL ) AS ranges " \
                "LEFT JOIN dataweave_india.products ON (ranges.min IS NULL OR discount >= ranges.min) AND " \
                "(ranges.max IS NULL OR discount <  ranges.max) " \
                "GROUP BY ranges.min, ranges.max;"
        result = db_inst.select_query_dict(query=query)

        return {'status': 'success', 'data': json.dumps(result)}, 200
