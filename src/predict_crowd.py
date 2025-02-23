# # predict_crowd.py - API for real-time prediction

# from flask import Flask, request, jsonify
# import numpy as np
# import tensorflow as tf
# import os
# from tensorflow.keras.losses import MeanSquaredError


# app = Flask(__name__)

# # Check if TensorFlow/Keras is installed
# try:
#     from tensorflow import keras
# except ImportError:
#     raise ImportError("TensorFlow/Keras cannot be imported. Please install it using: pip install tensorflow")

# # Load trained LSTM model
# model_path = os.path.join("models", "crowd_lstm_model.h5")
# if not os.path.exists(model_path):
#     raise FileNotFoundError(f"Model file not found: {model_path}")


# # Define custom objects
# custom_objects = {"mse": MeanSquaredError()}

# # Load model with custom objects
# model = keras.models.load_model(model_path, custom_objects=custom_objects)


# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.json.get("footfall", [])
#         if not data:
#             return jsonify({"error": "No footfall data provided"}), 400
        
#         data = np.array(data).reshape(1, -1, 1)
#         prediction = model.predict(data)
#         return jsonify({"predicted_footfall": float(prediction[0][0])})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)


# import os
# import xgboost as xgb
# import tensorflow as tf
# from tensorflow.keras.losses import MeanSquaredError
# from fastapi import FastAPI, HTTPException
# import numpy as np

# app = FastAPI()

# # Load LSTM Model
# try:
#     lstm_model = tf.keras.models.load_model("models/crowd_lstm_model.h5", custom_objects={"mse": MeanSquaredError()})
#     print("LSTM model loaded successfully.")
# except Exception as e:
#     print(f"Error loading LSTM model: {e}")
#     lstm_model = None

# # Load XGBoost Model
# xgb_model = xgb.Booster()
# xgb_model_path = "models/congestion_xgboost.model"

# if os.path.exists(xgb_model_path):
#     try:
#         xgb_model.load_model(xgb_model_path)
#         print("Successfully loaded XGBoost model.")
#     except xgb.core.XGBoostError as e:
#         print(f"Error loading XGBoost model: {e}")
# else:
#     print(f"XGBoost model file not found: {xgb_model_path}")

# @app.post("/predict")
# def predict_crowd(features: list):
#     try:
#         features_array = np.array(features).reshape(1, -1)
#         dmatrix = xgb.DMatrix(features_array)
#         xgb_prediction = xgb_model.predict(dmatrix).tolist()
#         lstm_prediction = lstm_model.predict(features_array).tolist() if lstm_model else "LSTM model not loaded"
#         return {"xgb": xgb_prediction, "lstm": lstm_prediction}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8080)



import os
import xgboost as xgb
import tensorflow as tf
from fastapi import FastAPI
import numpy as np
import uvicorn

app = FastAPI()

# Register MSE loss function for loading LSTM model
tf.keras.utils.get_custom_objects()["mse"] = tf.keras.losses.MeanSquaredError()

# Load LSTM Model
try:
    lstm_model = tf.keras.models.load_model("models/crowd_lstm_model.h5")
    print("LSTM model loaded successfully.")
except Exception as e:
    print(f"Error loading LSTM model: {e}")
    lstm_model = None

# Load XGBoost Model with Error Handling
xgb_model = xgb.Booster()
try:
    xgb_model.load_model("models/congestion_xgboost.json")
    print("XGBoost model loaded successfully from JSON.")
except Exception as e:
    print(f"Error loading XGBoost JSON model: {e}")
    try:
        xgb_model.load_model("models/congestion_xgboost.bin")
        print("XGBoost model loaded successfully from BIN backup.")
    except Exception as e:
        print(f"Error loading XGBoost BIN model: {e}")
        xgb_model = None

@app.post("/predict")
def predict_crowd(features: list):
    if xgb_model is None or lstm_model is None:
        return {"error": "Model loading failed."}
    
    features_array = np.array(features).reshape(1, -1)
    dmatrix = xgb.DMatrix(features_array)
    xgb_prediction = xgb_model.predict(dmatrix).tolist()
    lstm_prediction = lstm_model.predict(features_array).tolist()
    
    return {"xgb": xgb_prediction, "lstm": lstm_prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)