from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('./model/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input values from the form
        bwd_packet_length_std = float(request.form['bwd_packet_length_std'])
        flow_bytes_per_s = float(request.form['flow_bytes_per_s'])
        total_length_fwd_packets = float(request.form['total_length_fwd_packets'])
        fwd_packet_length_std = float(request.form['fwd_packet_length_std'])
        flow_iat_std = float(request.form['flow_iat_std'])
        flow_iat_min = float(request.form['flow_iat_min'])
        flow_iat_total = float(request.form['flow_iat_total'])

        # Create a feature vector from the input values
        features = [[bwd_packet_length_std, flow_bytes_per_s, total_length_fwd_packets, fwd_packet_length_std, flow_iat_std, flow_iat_min, flow_iat_total]]

        # Make the prediction using the loaded model
        prediction = model.predict(features)

        # Return the prediction result to the user
        if (prediction[0]==1):
            return render_template('index.html', prediction='<span class="error-message">The network is compromised</span>')
        else:
            return render_template('index.html', prediction='The network is benign')
    except ValueError:
         return render_template('index.html', error_message="Please enter valid numbers for all input fields.")

if __name__ == '__main__':
    app.run(debug=True)
'''
["Bwd Packet Length Std", "Flow Bytes/s", "Total Length of Fwd Packets", "Fwd Packet Length Std",
     "Flow IAT Std", "Flow IAT Min", "Fwd IAT Total"]
'''
