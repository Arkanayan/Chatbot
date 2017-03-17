from flask import Flask, request, jsonify
import random

def get_message_format(name, message):
    """
    Gives a dict containing the message that needs to be shown to the user
    :return dict message format
    """
    return {'name': name, 'message': message}


def get_error_format(err_msg):
    """
    Constructs dictionary of error message format
    :param err_msg: error message
    :return: dictionary of error format
    """
    return {'error': err_msg}

message_strings = [
    'You have have not claimed anything',
    'You are stupid',
    'Turn off your mind'
]

def get_random_message(msg_list=message_strings):
    return random.choice(msg_list)

app = Flask(__name__)
name_input = 'name'
dob_input = 'dob'


@app.route('/getDetails', methods=['POST'])
def get_details():
    """
    Url format: www.whatever.com/getDetails
    method: POST
    Takes two POST inputs;
    'name' -> name of the person,
    'dob' -> date of birth of the person
    :return: the ultimate Message
    """
    if request.method == 'POST':
        name = request.form.get(name_input, None)
        dob = request.form.get(dob_input, None)
        if name is None and dob is None:
            return jsonify(get_error_format("Please check your inputs")), 400

    return jsonify(get_message_format(name, get_random_message()))
