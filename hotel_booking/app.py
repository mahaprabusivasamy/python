

import os
import socket
import json

# Get the absolute path to the directory containing the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the absolute path to the rooms.json file
rooms_json_path = os.path.join(current_directory, 'path/to/rooms.json')

# Load initial room status from the JSON file
with open(rooms_json_path, 'r') as file:
    room_status = json.load(file)

# ... rest of your code ...


from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load initial room status from a JSON file
with open('rooms.json', 'r') as file:
    room_status = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/room_status', methods=['GET', 'POST'])
def room_status_page():
    if request.method == 'POST':
        room_number = int(request.form.get('room_number'))
        guest_name = request.form.get('guest_name')

        if room_number in room_status and room_status[room_number] == "":
            room_status[room_number] = guest_name
            with open('rooms.json', 'w') as file:
                json.dump(room_status, file)
            return render_template('room_status.html', room_number=room_number, guest_name=guest_name)

    return render_template('room_status.html', room_number=None, guest_name=None, room_status=room_status)

if __name__ == '__main__':
    app.run(debug=True)
