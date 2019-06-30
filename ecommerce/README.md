# Ecommerce

Simple Flask application for Ecommerce.

### Apis
- Get all products lists.
    ```sh
  - GET /api/products
    ```
 - Get all products lists after filters.
    ```sh
    - GET /api/products {"category": "Men's Clothing", "brand": "Campus Sutra"}
    ```
 - Get product.
    ```sh
    - GET /api/products/{sku}
    ```
- Update a product information.
    ```sh
    - PUT /api/products/{sku} {"category": "Men's Clothing", "brand": "Campus Sutra"}
    ```
- Get all product discounts counts.
    ```sh
    - GET /api/products/discounts
    ```

### Installation

Ecommerce requires Python 2.7 to run.

Install the dependencies and start the server.

```sh
$ pip install -r requirements.txt
$ APP_SETTINGS=development python run.py
```

For production environments...

```sh
$ APP_SETTINGS=production python run.py
```

### Docker
Ecommerce is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 5000, so change this within the docker-compose.yml if necessary. When ready, simply use the docker-compose.yml to build the image.

```sh
$ cd ecommerce
$ docker-compose -f docker-compose.yml up --build
```
This will create the **ecommerce** image and start the service. 


### Testing

For testing environments...

```sh
$ APP_SETTINGS=testing python test_apis.py
```
