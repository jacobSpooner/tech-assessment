#Test create_order endpoint

import json

def test_create_order(test_app):
    #Set Client
    client = test_app.test_client()

    testOrder = {
            "firstName": "testFirstCreate",
            "lastName": "TestLastCreate",
            "address": {
                "streetAddress": "TestCreate",
                "city": "New York",
                "state": "NY",
                "postalCode": "10016"
            },
            "phoneNumber": "2125551234",
            "item": "Phone"
        }

    #Send order
    resp = client.post('/create_order', data = testOrder)
    data = json.loads(resp.data.decode())

    assert "Order Created!" in data