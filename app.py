from flask import Flask, render_template, request
import joblib
import pandas as pd
import sqlite3

app = Flask(__name__)

# Load trained ML model
model = joblib.load("models/placement_model.pkl")


# =========================================================
# DATABASE - SAVE PREDICTION
# =========================================================

def save_prediction(data, prediction, probability):

    connection = sqlite3.connect("student_placement.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            age,
            gender,
            cgpa,
            tenth_percentage,
            twelfth_percentage,
            aptitude_score,
            coding_score,
            communication_score,
            technical_skills,
            certifications,
            internship_experience,
            projects,
            prediction,
            probability
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["Age"],
        data["Gender"],
        data["CGPA"],
        data["Tenth_Percentage"],
        data["Twelfth_Percentage"],
        data["Aptitude_Score"],
        data["Coding_Score"],
        data["Communication_Score"],
        data["Technical_Skills"],
        data["Certifications"],
        data["Internship_Experience"],
        data["Projects"],
        prediction,
        probability
    ))

    connection.commit()
    connection.close()


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "Age": int(request.form["age"]),
        "Gender": request.form["gender"],
        "CGPA": float(request.form["cgpa"]),
        "Tenth_Percentage": float(request.form["tenth"]),
        "Twelfth_Percentage": float(request.form["twelfth"]),
        "Aptitude_Score": float(request.form["aptitude"]),
        "Coding_Score": float(request.form["coding"]),
        "Communication_Score": float(request.form["communication"]),
        "Technical_Skills": int(request.form["technical"]),
        "Certifications": int(request.form["certifications"]),
        "Internship_Experience": int(request.form["internship"]),
        "Projects": int(request.form["projects"])
    }

    input_data = pd.DataFrame([data])

    # ML prediction
    prediction = model.predict(input_data)[0]

    # Probability
    probabilities = model.predict_proba(input_data)[0]
    class_names = model.classes_

    probability_dict = dict(
        zip(class_names, probabilities)
    )

    placed_probability = probability_dict.get(
        "Placed", 0
    ) * 100

    placed_probability = round(
        placed_probability, 2
    )

    # =====================================================
    # RECOMMENDATIONS
    # =====================================================

    recommendations = []

    if data["CGPA"] < 7:
        recommendations.append(
            "Improve your academic performance and maintain CGPA above 7."
        )

    if data["Coding_Score"] < 60:
        recommendations.append(
            "Improve coding skills through Python, SQL and problem solving."
        )

    if data["Aptitude_Score"] < 60:
        recommendations.append(
            "Practice quantitative aptitude and logical reasoning."
        )

    if data["Communication_Score"] < 60:
        recommendations.append(
            "Improve communication and interview skills."
        )

    if data["Certifications"] == 0:
        recommendations.append(
            "Complete relevant technical certifications."
        )

    if data["Internship_Experience"] == 0:
        recommendations.append(
            "Try to gain internship or practical industry experience."
        )

    if data["Projects"] < 2:
        recommendations.append(
            "Build at least 2 strong real-world projects."
        )

    if data["Technical_Skills"] < 5:
        recommendations.append(
            "Develop more technical skills relevant to your target job."
        )

    if not recommendations:
        recommendations.append(
            "Your profile looks strong. Continue improving your technical and interview skills."
        )

    # =====================================================
    # SKILL GAP
    # =====================================================

    skill_scores = {

        "CGPA": round(data["CGPA"] * 10, 1),

        "Aptitude": data["Aptitude_Score"],

        "Coding": data["Coding_Score"],

        "Communication": data["Communication_Score"],

        "Technical Skills": data["Technical_Skills"] * 10
    }

    # Save prediction
    save_prediction(
        data,
        prediction,
        placed_probability
    )

    return render_template(
        "result.html",
        prediction=prediction,
        probability=placed_probability,
        recommendations=recommendations,
        skill_scores=skill_scores
    )


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect("student_placement.db")
    cursor = connection.cursor()

    # =====================================================
    # BASIC STATISTICS
    # =====================================================

    total = cursor.execute(
        "SELECT COUNT(*) FROM predictions"
    ).fetchone()[0]

    placed = cursor.execute(
        """
        SELECT COUNT(*)
        FROM predictions
        WHERE prediction = 'Placed'
        """
    ).fetchone()[0]

    not_placed = cursor.execute(
        """
        SELECT COUNT(*)
        FROM predictions
        WHERE prediction = 'Not Placed'
        """
    ).fetchone()[0]

    average_probability = cursor.execute(
        """
        SELECT AVG(probability)
        FROM predictions
        """
    ).fetchone()[0]

    # =====================================================
    # PREDICTION HISTORY
    # =====================================================

    records = cursor.execute(
        """
        SELECT
            id,
            age,
            gender,
            cgpa,
            prediction,
            probability
        FROM predictions
        ORDER BY id DESC
        """
    ).fetchall()

    # =====================================================
    # CGPA BUCKET DATA
    # =====================================================

    cgpa_data = cursor.execute(
        """
        SELECT cgpa, prediction
        FROM predictions
        """
    ).fetchall()

    cgpa_labels = [
        "5-6",
        "6-7",
        "7-8",
        "8-9",
        "9-10"
    ]

    cgpa_placed = [0, 0, 0, 0, 0]
    cgpa_not_placed = [0, 0, 0, 0, 0]

    for cgpa, prediction in cgpa_data:

        if 5 <= cgpa < 6:
            index = 0

        elif 6 <= cgpa < 7:
            index = 1

        elif 7 <= cgpa < 8:
            index = 2

        elif 8 <= cgpa < 9:
            index = 3

        elif 9 <= cgpa <= 10:
            index = 4

        else:
            continue

        if prediction == "Placed":
            cgpa_placed[index] += 1

        else:
            cgpa_not_placed[index] += 1

    # =====================================================
    # CODING SCORE BUCKET DATA
    # =====================================================

    coding_data = cursor.execute(
        """
        SELECT coding_score, prediction
        FROM predictions
        """
    ).fetchall()

    coding_labels = [
        "0-20",
        "20-40",
        "40-60",
        "60-80",
        "80-100"
    ]

    coding_placed = [0, 0, 0, 0, 0]
    coding_not_placed = [0, 0, 0, 0, 0]

    for coding, prediction in coding_data:

        if 0 <= coding < 20:
            index = 0

        elif 20 <= coding < 40:
            index = 1

        elif 40 <= coding < 60:
            index = 2

        elif 60 <= coding < 80:
            index = 3

        elif 80 <= coding <= 100:
            index = 4

        else:
            continue

        if prediction == "Placed":
            coding_placed[index] += 1

        else:
            coding_not_placed[index] += 1

    # =====================================================
    # PROBABILITY DISTRIBUTION
    # =====================================================

    probability_data = cursor.execute(
        """
        SELECT probability
        FROM predictions
        """
    ).fetchall()

    probability_ranges = [
        "0-20%",
        "20-40%",
        "40-60%",
        "60-80%",
        "80-100%"
    ]

    probability_counts = [0, 0, 0, 0, 0]

    for row in probability_data:

        probability = row[0]

        if probability < 20:
            probability_counts[0] += 1

        elif probability < 40:
            probability_counts[1] += 1

        elif probability < 60:
            probability_counts[2] += 1

        elif probability < 80:
            probability_counts[3] += 1

        else:
            probability_counts[4] += 1

    connection.close()

    # =====================================================
    # AVERAGE
    # =====================================================

    average_probability = round(
        average_probability or 0,
        2
    )

    # =====================================================
    # SEND DATA TO DASHBOARD
    # =====================================================

    return render_template(

        "dashboard.html",

        total=total,

        placed=placed,

        not_placed=not_placed,

        average_probability=average_probability,

        records=records,

        cgpa_labels=cgpa_labels,

        cgpa_placed=cgpa_placed,

        cgpa_not_placed=cgpa_not_placed,

        coding_labels=coding_labels,

        coding_placed=coding_placed,

        coding_not_placed=coding_not_placed,

        probability_ranges=probability_ranges,

        probability_counts=probability_counts
    )


# =========================================================
# RUN
# =========================================================
    
# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )