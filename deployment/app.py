from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('./model/best_model.pkl', 'rb') as file:
    model = joblib.load(file)

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
        #features = [[bwd_packet_length_std, flow_bytes_per_s, total_length_fwd_packets, fwd_packet_length_std, flow_iat_std, flow_iat_min, flow_iat_total]]

        #unfortunately not providing column names does not work for xgb
        features = pd.DataFrame({
            'Bwd Packet Length Std': [bwd_packet_length_std],
            'Flow Bytes/s': [flow_bytes_per_s],
            'Total Length of Fwd Packets': [total_length_fwd_packets],
            'Fwd Packet Length Std': [fwd_packet_length_std],
            'Flow IAT Std': [flow_iat_std],
            'Flow IAT Min': [flow_iat_min],
            'Fwd IAT Total': [flow_iat_total]})

        # Make the prediction using the loaded model
        prediction = model.predict(features)

        # Return the prediction result to the user
        if (prediction[0]==1):
            return render_template('index.html', prediction='<span class="error-message">The network is benign</span>')
        else:
            return render_template('index.html', prediction='The network is compromised')
    except ValueError:
        return render_template('index.html', error='<span class="error-message">Invalid Input, Please input numeric value</span>')


if __name__ == '__main__':
  # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
