import pytest
from app import create_app
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_price_over_2000(client):
    order_data = {
        "id": "A0000001",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "2050",
        "currency": "TWD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Price is over 2000" in response.json["errors"]

def test_name_contain_nonenglish(client):
    order_data = {
        "id": "A0000003",
        "name": "Holiday ;;;",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "200",
        "currency": "TWD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Name contains non-English characters" in response.json["errors"]

def test_name_isnt_capitalized(client):
    order_data = {
        "id": "A0000003",
        "name": "Melody holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "200",
        "currency": "TWD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Name is not capitalized" in response.json["errors"]

def test_currency_TWD(client):
    order_data = {
        "id": "A0000002",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "1500",
        "currency": "TWD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 200

def test_currency_JPY(client):
    order_data = {
        "id": "A0000002",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "1500",
        "currency": "JPY"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Currency format is wrong" in response.json["errors"]

def test_currency_USD_over_2000(client):
    order_data = {
        "id": "A0000002",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "1500",
        "currency": "USD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Price is over 2000" in response.json["errors"]

def test_currency_USD(client):
    order_data = {
        "id": "A0000002",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road"
        },
        "price": "15",
        "currency": "USD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json["price"] == "465"
    assert response.json["currency"] == "TWD"

def test_missing_address_field(client):
    order_data = {
        "id": "A0000003",
        "name": "Melody Holiday Inn",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district"
            # 缺少 'street'
        },
        "price": "1500",
        "currency": "TWD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Missing required field in address: street" in response.json["errors"]

def test_data_type_mismatch(client):
    order_data = {
        "id": "A0000003",
        "name": "Melody Holiday Inn",
        "address": "taipei-city",
        "price": "1500",
        "currency": "TWD"
    }

    response = client.post('/api/orders', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 400
    assert "Field 'address' must be a dictionary" in response.json["errors"]
