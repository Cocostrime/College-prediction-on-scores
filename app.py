from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load full dataset
df = pd.read_csv("expanded_dataset_with_gmat.csv")
df = df.drop(columns=['Serial No.'])


gre_df = df[df['GRE Score'].notnull()]
X_gre = gre_df[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']]
y_gre = gre_df['Chance of Admit ']


gmat_df = df[df['GMAT Score'].notnull()]
X_gmat = gmat_df[['GMAT Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']]
y_gmat = gmat_df['Chance of Admit ']

# Train models
gre_model = LinearRegression()
gre_model.fit(X_gre, y_gre)

gmat_model = LinearRegression()
gmat_model.fit(X_gmat, y_gmat)

# Flask app
app = Flask(__name__)

tier_colleges = {
    1: ["MIT", "Stanford", "Harvard", "Caltech", "Princeton"],
    2: ["CMU", "Berkeley", "Georgia Tech", "Cornell", "UCLA"],
    3: ["Penn State", "UC Irvine", "Arizona State", "Texas A&M", "Wisconsin-Madison"],
    4: ["SUNY Buffalo", "Northeastern", "Rutgers", "University of Utah", "University of Colorado Boulder"],
    5: ["San Jose State", "New Jersey Institute of Technology", "UT Arlington", "University of Houston", "Wichita State"]
}

# Landing page
@app.route('/')
def select_test():
    return render_template('select_test.html')

# Redirect to GRE or GMAT form based on user choice
@app.route('/form', methods=['POST'])
def form_redirect():
    test = request.form.get('test')
    if test == 'gre':
        return render_template('form_gre.html')
    elif test == 'gmat':
        return render_template('form_gmat.html')
    else:
        return redirect(url_for('select_test'))

# GRE prediction
@app.route('/predict', methods=['POST'])
def predict():
    gre = float(request.form['gre'])
    toefl = float(request.form['toefl'])
    rating = int(request.form['rating'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    research = int(request.form['research'])

    input_data = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])
    chance = round(gre_model.predict(input_data)[0] * 100, 2)

    if rating in [1, 2] and gre > 320 and toefl > 100:
        suggested_tier = 3 if rating == 1 else 4
        message = "🌟 Your profile is strong! Consider applying to a broader range of good colleges."
    elif chance < 70:
        suggested_tier = min(rating + 1, 5)
        message = "⚠️ Your predicted chance is low. It's better to look for a lower-tier college."
    else:
        suggested_tier = rating
        message = "✅ You are recommended to apply to colleges in this tier."

    suggested_colleges = tier_colleges.get(suggested_tier, [])

    return render_template("result.html", chance=chance, colleges=suggested_colleges, message=message)

@app.route('/predict_gmat', methods=['POST'])
def predict_gmat():
    try:
        gmat = float(request.form['gmat'])
        toefl = float(request.form['toefl'])
        rating = int(request.form['rating'])
        sop = float(request.form['sop'])
        lor = float(request.form['lor'])
        cgpa = float(request.form['cgpa'])
        research = int(request.form['research'])

        # Prepare input for prediction
        input_data = np.array([[gmat, toefl, rating, sop, lor, cgpa, research]])
        chance = round(gmat_model.predict(input_data)[0] * 100, 2)

        # Tier & recommendation logic
        if rating in [1, 2] and gmat > 700 and toefl > 100:
            suggested_tier = 3 if rating == 1 else 4
            message = "🌟 Excellent profile! You can apply to a wider range of good B-schools."
        elif chance < 70:
            suggested_tier = min(rating + 1, 5)
            message = "⚠️ Your predicted chance is low. Consider targeting safer options."
        else:
            suggested_tier = rating
            message = "✅ You can confidently apply to this tier of colleges."

        suggested_colleges = tier_colleges.get(suggested_tier, [])

        return render_template("result.html", chance=chance, colleges=suggested_colleges, message=message)

    except Exception as e:
        return f"Something went wrong: {e}"
    
if __name__ == '__main__':
    app.run(debug=True)