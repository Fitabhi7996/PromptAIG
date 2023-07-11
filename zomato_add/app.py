from flask import Flask, render_template, request, redirect,jsonify
from chatbot_logic import process_message

app = Flask(__name__)

# Define the dishes and orders data structures
dishes = []
orders = []
order_id_counter = 1


@app.route('/')
def list_dishes():
    return render_template('dishes.html', dishes=dishes)


@app.route('/dishes/add', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        # Retrieve the form data
        dish_id = request.form['dish_id']
        dish_name = request.form['dish_name']
        price = request.form['price']
        availability = request.form['availability']

        # Create a new dish dictionary
        dish = {
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': availability
        }

        # Add the dish to the dishes list
        dishes.append(dish)

        return redirect('/')

    return render_template('add_dish.html')


@app.route('/dishes/update/<dish_id>', methods=['GET', 'POST'])
def update_dish_availability(dish_id):
    dish = next((dish for dish in dishes if dish['dish_id'] == dish_id), None)

    if not dish:
        return 'Dish not found'

    if request.method == 'POST':
        availability = request.form['availability']
        dish['availability'] = availability
        return redirect('/')

    return render_template('update_dish.html', dish=dish)


@app.route('/dishes/remove/<dish_id>')
def remove_dish(dish_id):
    dish = next((dish for dish in dishes if dish['dish_id'] == dish_id), None)

    if not dish:
        return 'Dish not found'

    dishes.remove(dish)
    return redirect('/')


@app.route('/orders/new', methods=['GET', 'POST'])
def take_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form.getlist('dish_ids')

        # Validate dish availability
        unavailable_dish_ids = [
            dish_id for dish_id in dish_ids if not is_dish_available(dish_id)
        ]

        if unavailable_dish_ids:
            return f"The following dishes are not available: {', '.join(unavailable_dish_ids)}"

        # Create a new order dictionary
        global order_id_counter
        order = {
            'order_id': str(order_id_counter),
            'customer_name': customer_name,
            'dish_ids': dish_ids,
            'status': 'received'
        }
        order_id_counter += 1

        # Add the order to the orders list
        orders.append(order)

        return redirect('/orders')

    return render_template('new_order.html', dishes=dishes)


@app.route('/orders/update/<order_id>', methods=['GET', 'POST'])
def update_order_status(order_id):
    order = next((order for order in orders if order['order_id'] == order_id), None)

    if not order:
        return 'Order not found'

    if request.method == 'POST':
        new_status = request.form['status']
        order['status'] = new_status
        return redirect('/orders')

    return render_template('update_order.html', order=order)


@app.route('/orders')
def list_orders():
    return render_template('orders.html', orders=orders)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = process_message(message)  # Use the chatbot logic function
    return jsonify({'message': response})


@app.route('/exit')
def exit_operations():
    # Perform any necessary cleanup or data storage operations
    return 'Goodbye!'


def is_dish_available(dish_id):
    dish = next((dish for dish in dishes if dish['dish_id'] == dish_id), None)
    return dish and dish['availability'].lower() == 'yes'


if __name__ == '__main__':
    app.run(debug=True)
