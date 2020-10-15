import json

def test_update_order(test_app):
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

    resp = client.post('/cancel_orders', data = testOrder)

    assert "Order Cancelled!" in json.loads(resp.data.decode())

