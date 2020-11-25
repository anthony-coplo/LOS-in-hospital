from flask import Flask, request, jsonify, render_template , redirect
import os
import pickle
from zipfile import ZipFile
import pickle

app = Flask(__name__)
port = int(os.getenv('PORT', '3000'))

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

def extract():
    with ZipFile('./model/LOS_model1.pkl.zip', 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall()


# make prediction 
@app.route('/predict', methods=['POST','GET'])
def predict():
    
    #check if extracted file exist
    if os.path.isfile('LOS_model.pkl'):
        print ("File exist")
    else:
        print ("création du fichier")
        extract()

    #chargement du modèle    
    model = pickle.load(open('LOS_model.pkl', 'rb'))

    #recup les inputs
    rcount = request.form.get('rcount')
    gender = request.form.get('gender')
    dialysisrenalendstage = request.form.get('dialysisrenalendstage')
    asthma = request.form.get('asthma')
    irondef = request.form.get('irondef')
    pneum = request.form.get('pneum')
    substancedependence = request.form.get('substancedependence')
    psychologicaldisordermajor = request.form.get('psychologicaldisordermajor')
    depress = request.form.get('depress')
    psychother = request.form.get('psychother')
    fibrosisandother = request.form.get('fibrosisandother')
    malnutrition = request.form.get('malnutrition')
    hemo = request.form.get('hemo')
    hematocrit = request.form.get('hematocrit')
    hemaneutrophilstocrit = request.form.get('neutrophils')
    sodium = request.form.get('sodium')
    glucose = request.form.get('glucose')
    bloodureanitro = request.form.get('bloodureanitro')
    creatinine = request.form.get('creatinine')
    bmi = request.form.get('bmi')
    pulse = request.form.get('pulse')
    respiration = request.form.get('respiration')
    secondarydiagnosisnonicd9 = request.form.get('secondarydiagnosisnonicd9')
    facid = request.form.get('facid')
    daysofweek_admit = request.form.get('daysofweek_admit')

    table = [[rcount,gender,dialysisrenalendstage,asthma,irondef,
        pneum,substancedependence,psychologicaldisordermajor,depress,psychother,fibrosisandother,
        malnutrition,hemo ,hematocrit, hemaneutrophilstocrit,sodium,glucose,bloodureanitro,creatinine,bmi,
        pulse,respiration,secondarydiagnosisnonicd9,facid,daysofweek_admit]]


    #inference sur le modèle
    prediction = model.predict(table)

    #return la prediction
    pred = str(prediction.item())
    return pred


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)