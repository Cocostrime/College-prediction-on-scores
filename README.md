🎓 Admit Ai — Admission Predictor

Admit Ai is a lightweight, ML-powered web app that predicts your chances of getting into an MBA/MTech program based on your GMAT/GRE score and academic profile.

It features:
🎯 Test-based chance prediction
🧠 Machine learning-backed model (trained inside the app or preloaded)
💻 Clean Bootstrap UI with animated components
🔄 Real-time result display with progress bar
🏷️ Tier suggestions: Reach, Match, or Safe


🚀 Features

Admission Form with:
  GMAT Score (for GMAT test)
  GRE Score (for GRE test)
  TOEFL Score
  University Rating
  SOP & LOR Strength
  CGPA
  - Research Experience
🎨 Beautiful animated prediction result page
🔢 ML model prediction (XGBoost/Linear Regression or similar)
💬 Borderline cases display multiple suggestions

📈 Input Fields

 GRE Prediction
- GRE Score
- TOEFL Score
- University Rating (1-5)
- SOP Strength (1.0–5.0)
- LOR Strength (1.0–5.0)
- CGPA
- Research Experience (0/1)

GMAT Prediction
- GMAT Score
- TOEFL Score
- University Rating (1-5)
- SOP Strength (1.0–5.0)
- LOR Strength (1.0–5.0)
- CGPA
- Research Experience (0/1)



🔧 How to Run Locally

1. Clone the repo
 
   git clone https://github.com/yourusername/College-prediction-on-scores.git
   cd College-prediction-on-scores

3. Create virtual environment

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

3. Install dependencies

pip install -r requirements.txt


4. Run the app

python app.py


5. Open browser at http://127.0.0.1:5000/


🧠 Model Training

The models were trained on real-world admissions datasets using Scikit-learn’s Linear Regression.
You can retrain the models using Jupyter notebooks or include your own dataset.
