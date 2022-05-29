import numpy as np
from flask import Flask, request, jsonify, render_template, session, redirect

import pickle

app = Flask(__name__)
model = pickle.load(open('rfc_model.pkl', 'rb'))
zip_dict= {97212: [9726.486486, 146186.0],
 97206: [7938.756428, 87404.0],
 97213: [7765.640274, 104868.0],
 97215: [7347.145877, 112734.0],
 97227: [7205.150977, 109494.0],
 97214: [5613.333333, 96678.0],
 97211: [4738.850772, 107669.0],
 97027: [4579.968944, 92998.0],
 97232: [4091.906005, 87464.0],
 97267: [3968.144232, 85929.0],
 97202: [3399.439851, 113578.0],
 97035: [3373.416653, 140650.0],
 97223: [3337.700683, 104461.0],
 97222: [3306.249306, 79481.0],
 97216: [3211.941479, 70982.0],
 97201: [3201.877934, 101606.0],
 97030: [3200.891686, 64612.0],
 97219: [3141.701769, 143475.0],
 97221: [3085.243553, 186288.0],
 97266: [2929.565794, 74418.0],
 97220: [2697.86745, 69069.0],
 97225: [2642.350856, 118799.0],
 97233: [2423.470499, 58121.0],
 97239: [2378.425151, 130573.0],
 97224: [2317.771248, 105065.0],
 97005: [2163.486644, 73178.0],
 97230: [1866.790801, 76745.0],
 97062: [1788.199181, 113680.0],
 97217: [1778.386606, 103943.0],
 97086: [1638.250928, 119895.0],
 97218: [1461.316397, 75978.0],
 97034: [1434.704401, 194490.0],
 97008: [1432.397004, 91244.0],
 97080: [1352.74886, 97765.0],
 97205: [1321.857486, 79657.0],
 97236: [1294.063567, 69998.0],
 97210: [1257.573735, 133214.0],
 97015: [1227.236558, 93965.0],
 97007: [1058.343648, 108969.0],
 97006: [955.6435103, 98207.0],
 97203: [922.9277448, 82238.0],
 97229: [845.9663121, 155336.0],
 97060: [781.8565594, 89749.0],
 97124: [659.8207293, 114264.0],
 97089: [564.6653365, 116132.0],
 97068: [490.3959871, 159411.0],
 97070: [480.160775, 105897.0],
 97045: [474.1716595, 100617.0],
 97123: [467.2792015, 102215.0],
 97132: [375.7468136, 102329.0],
 97009: [277.7759325, 98745.0],
 97140: [178.208847, 127500.0],
 97004: [139.110305, 108677.0],
 97113: [56.07914301, 90626.0],
 97023: [51.48943944, 82423.0],
 97038: [39.44446701, 83860.0],
 97231: [33.86120767, 161621.0],
 97019: [18.84010586, 99528.0]}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=('GET','POST'))

def predict():
    #input = [int(x) for x in request.form.values()]
    var = request.form.to_dict('Zip Code')
    MeanHHI=zip_dict[int(var['Zip Code'])][1]
    #zipPopDensity=zip_dict[int(var['Zip Code'])][0]
    
    m = int(MeanHHI)
    #d = int(zipPopDensity)
    y = request.form['Year Built']
    be = request.form['Bed']
    ba = request.form['Bath']
    s = request.form['Square Feet']
    #l = request.form['Lot Size']
    sq = int(s)
    #int_features = [int(x) for x in request.form.values()]
    int_features = [y,be,ba,sq,m]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction
   

    return render_template('index.html', prediction_text='Home Price Range Should be: $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)