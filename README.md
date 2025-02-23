# SmartRail Crowd Prediction

SmartRail Crowd Prediction is an AI-powered system that predicts railway station footfall and congestion levels using real-time data, deep learning (LSTM), and machine learning (XGBoost). The system provides live footfall trends, train delays, and congestion predictions via a Streamlit dashboard.

## 📂 Folder Structure

```
📁 SmartRailCrowdPrediction
│── 📂 data
│   ├── station_data.csv          # Dataset 
|   |-- dataset.py                # program to create dataset
│   ├── station_cctv.mp4          # Sample CCTV footage for testing
│   ├── live_footfall_data.json   # Real-time data storage
│
│── 📂 models
│   ├── crowd_lstm_model.h5       # Trained LSTM model for crowd prediction
│   ├── congestion_xgboost.json   # XGBoost model for congestion analysis
│
│── 📂 src
│   ├── crowd_detection_yolo.py    # YOLOv8-based real-time people counting
│   ├── predict_crowd.py          # API for real-time prediction
│
│── dasgboard.py                   # Streamlit dashboard for live visualization
│── README.md                      # Project documentation
```

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

Ensure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Prediction API

Start the prediction service:

```bash
python src/predict_crowd.py
```

### 3️⃣ Launch the Dashboard

Run the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

## 🎯 Features

- **Live Footfall Tracking** 📊
- **Congestion Prediction (Normal, Medium, Overcrowded)** 🔴🟡🟢
- **Train Delays & Station Info** 🚉⏳
- **Real-time People Counting** 🎥

For further customization or issues, feel free to contribute! 🚆🚀

---
**Developed by Amit Prasad**

