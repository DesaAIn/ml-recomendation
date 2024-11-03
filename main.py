from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model dan label encoder
with open('xgb_model.pkl', 'rb') as model_file:
    xgb_model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as le_file:
    le = pickle.load(le_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari request
    data = request.json
    
    # Pastikan input data sesuai
    if not all(key in data for key in ['Kesesuaian_Rencana', 'Persentase_Dana', 'Selisih_Hari']):
        return jsonify({'error': 'Data tidak lengkap'}), 400

    # Ambil fitur dari input JSON
    features = np.array([[data['Kesesuaian_Rencana'], data['Persentase_Dana'], data['Selisih_Hari']]])
    
    # Prediksi menggunakan model
    prediction_encoded = xgb_model.predict(features)
    
    # Decode hasil prediksi kembali ke label asli
    prediction = le.inverse_transform(prediction_encoded)
    
    # Kembalikan hasil prediksi sebagai response JSON
    return jsonify({'saran': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
