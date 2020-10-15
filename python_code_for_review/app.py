from flask import Flask
from flask import request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Test complete!"

#Create Order
@app.route("/create_order", methods=["POST"])
def create_order():
    data = request.get_json()

    #Open JSON to append data
    with open('./data/orders.json') as json_file:
        orders = json.load(json_file)
        
    #Start new JSON object in orders
    temp = orders['orders'] 

    #Store all relevant customer data
    order = {
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        "address": 
        {
            'streetAddress': data['address']['streetAddress'],
            'city': data['address']['city'],
            'state': data['address']['state'],
            'postalCode': data['address']['postalCode'],
        },

        'phoneNumber': data['phoneNumber'],
        'item': data['item'] #Should be a simple product name
    }

    #add JSON data to orders file
    temp.append(order)

    #Attempt to save data
    try:
        with open('./data/orders.json', 'w') as outfile:
            json.dump(orders, outfile, indent=4)
    except:
        return "Order placement failure" #Save failure

    return "Order Placed!"

#List all orders by customer
@app.route("/list_orders")
def list_orders():
    
    #Open order file
    with open('./data/orders.json') as json_file:
        orders = json.load(json_file)
        
    #Return orders in JSON format
    return jsonify(orders)

#Update order
@app.route("/update_order", methods=["POST"])
def update_order():
    data = request.get_json()

    #open file and find correct order
    with open('./data/orders.json') as json_file:
        orders = json.load(json_file)
        for o in orders['orders']:
            if(o['firstName'] == data['firstName'] and o['lastName'] == data['lastName']):
                o.update(data) #update order

                #Attempt to save order
                try:
                    with open('./data/orders.json', 'w') as outfile:
                        json.dump(orders, outfile, indent=4)
                    return "Order updated!"
                except:
                    return "Order update failure"
    
    return "Could not find order."
    
    

#Cancel Order
@app.route("/cancel_order", methods=["POST"])
def cancel_order():
    data = request.get_json()

    #Open file and find correct order
    with open('./data/orders.json') as json_file:
        orders = json.load(json_file)
        for o in orders['orders']:
            if(o['firstName'] == data['firstName'] and o['lastName'] == data['lastName'] and o['item'] == data['item']):
                orders['orders'].remove(o) #remove order

                #Attempt to save data
                try:
                    with open('./data/orders.json', 'w') as outfile:
                        json.dump(orders, outfile, indent=4)
                        return "Order Cancelled!"
                except:
                    return "Order cancel failure"
    
    
    
    return "Could not find order."


#NEED TESTS