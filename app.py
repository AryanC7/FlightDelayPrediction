from flask import Flask, render_template, request
import pickle
import numpy as np

with open('flight_delay.pkl', 'rb') as file:
    model = pickle.load(file) 
app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        d1 = request.form['Airline']
        # d1 = int(d1)
        if (d1 == 'Commutair Aka Champlain Enterprises, Inc.'):
            d1 = 7
    
        d2 = request.form['Origin']
        # d2 = int(d2)
        if (d2=='GJT'):
            d2 = 144

        d3 = request.form['Destination']
        # d3 = int(d3)
        if(d3=='DEN'):
            d3 = 98

        d4 = request.form['Departure_Time']
        d4 = int(d4)

        d5 = request.form['Origin_City']
        # d5 = int(d5)
        if(d5 == 'Grand Junction, CO'):
            d5 = 129

        d6 = request.form['Origin_State']
        # d6 = int(d6)
        if(d6 == 'Colorado'):
            d6 = 5

        d7 = request.form['Destination_City']
        # d7 = int(d7)
        if (d7 == 'Denver, CO'):
            d7 = 89

        d8 = request.form['Destination_State']
        # d8 = int(d8)
        if(d8 == 'Colorado'):
            d8 = 5
            
        d9 = request.form['Arrival_Time']
        d9 = int(d9)

        # d10 = request.form['Year']
        d10 = np.random.choice([2018,2019,2021,2022])

        # d11 = request.form['Month']
        d11 = np.random.randint(1,13)

        #arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11]])
        pred = model.predict(np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]]))[0]
        if pred == 0:
            return render_template('index.html', prediction_text="delay anywhere from 15 to 60 mins")
        else:
            return render_template('index.html', prediction_text="maximum delay of 15 mins")
    else:
        return render_template('index.html')

app.run(debug=True) 
