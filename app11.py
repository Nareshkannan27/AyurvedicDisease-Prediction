import numpy as np
from flask import Flask, request, render_template
import pickle

# Load the trained classifier
# Assuming `clf` is your trained classifier model

with open('new_gestational.pkl', 'rb') as f:
    model = pickle.load(f)
try:
    # Load the trained classifier from the pickle file
    with open('new_gestational.pkl', 'rb') as f:
        model = pickle.load(f)
        print("Model loaded successfully!")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")


# Create Flask app
app = Flask(__name__)

# Route to render the HTML form
@app.route("/")
def home():
    return render_template("prediction_form.html")

# Route to handle prediction
@app.route("/predict", methods=["POST"])
def predict():
    # Extract the input values from the form
    features = [int(request.form[field]) for field in ["itching", "skin_rash", "nodal_skin_eruptions", "stomach_pain", "skin_peeling", "shivering", "continuous_sneezing", "lethargy"]]


    try:
        # Make prediction
        prediction = model.predict([features])[0]
        label_1, label_2 = prediction

        # Convert prediction to human-readable format
        prediction_text = "Kapha" if label_1 == 0 else ("Pitta" if label_1 == 1 else "Vata")
        prognosis_labels = {
                0: '(vertigo) Paroymsal  Positional Vertigo',
                1: 'AIDS',
                2: 'Acne',
                3: 'Alcoholic hepatitis',
                4: 'Allergy',
                5: 'Arthritis',
                6: 'Bronchial Asthma',
                7: 'Cervical spondylosis',
                8: 'Chicken pox',
                9: 'Chronic cholestasis',
                10: 'Common Cold',
                11: 'Dengue',
                12: 'Diabetes ',
                13: 'Dimorphic hemmorhoids(piles)',
                14: 'Drug Reaction',
                15: 'Fungal infection',
                16: 'GERD',
                17: 'Gastroenteritis',
                18: 'Heart attack',
                19: 'Hepatitis B',
                20: 'Hepatitis C',
                21: 'Hepatitis D',
                22: 'Hepatitis E',
                23: 'Hypertension',
                24: 'Hyperthyroidism',
                25: 'Hypoglycemia',
                26: 'Hypothyroidism',
                27: 'Impetigo',
                28: 'Jaundice',
                29: 'Malaria',
                30: 'Migraine',
                31: 'Osteoarthristis',
                32: 'Paralysis (brain hemorrhage)',
                33: 'Peptic ulcer diseae',
                34: 'Pneumonia',
                35: 'Psoriasis',
                36: 'Tuberculosis',
                37: 'Typhoid',
                38: 'Urinary tract infection',
                39: 'Varicose veins',
                40: 'Hepatitis A'
            }

        prognosis_label_2 = prognosis_labels.get(label_2, "Unknown")


    
        # Return the prediction as a response
        return render_template("prediction_result.html", prediction=prediction_text, prognosis=prognosis_label_2)


    except Exception as e:
        return f"An error occurred: {e}"
        

if __name__ == "__main__":
    app.run(debug=True,port=5001)
