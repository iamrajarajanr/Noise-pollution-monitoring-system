# Import necessary libraries
from flask import Flask, render_template, request, jsonify

app = Flask(__name)

# Simulated data from IoT sensors
noise_data = {"sensor1": 70, "sensor2": 60, "sensor3": 75}

@app.route('/')
def index():
    return render_template('index.html', data=noise_data)

@app.route('/update', methods=['POST'])
def update_data():
    sensor_id = request.form['sensor_id']
    noise_level = request.form['noise_level']
    noise_data[sensor_id] = float(noise_level)
    return jsonify({"message": "Data updated successfully"})

if __name__ == '__main__':
    app.run(debug=True)

