import random

# Define a list of responses for different intents
greetings = ['Hello!', 'Hi there!', 'Hey, how can I help?']
hours_of_operation = 'Our hours of operation are from 9am to 6pm, Monday to Friday.'
order_status = 'To check the status of your order, please provide your order number.'
popular_dish = 'Our most popular dish is the Zesty Zomato Special!'

# Function to process user messages and generate chatbot responses
def process_message(message):
    message = message.lower()  # Convert the message to lowercase for easier handling

    # Check the user's intent and provide a corresponding response
    if any(greeting in message for greeting in ['hello', 'hi', 'hey']):
        return random.choice(greetings)
    elif any(keyword in message for keyword in ['hours', 'operation']):
        return hours_of_operation
    elif any(keyword in message for keyword in ['status', 'order']):
        return order_status
    elif any(keyword in message for keyword in ['popular', 'dish']):
        return popular_dish
    else:
        return "I'm sorry, I couldn't understand your query. How can I assist you?"

