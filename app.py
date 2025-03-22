from flask import Flask, jsonify, request
from pickle import load as pload
app = Flask(__name__)


#Create Service
with open ('model_dict_car_eval_rf.pkl', 'rb') as file:
    model_dict = pload(file)


@app.route('/', methods=['POST'])
def predict_car_evaluation ():
    if request.method == 'POST':
        data = request.get_json()
        buying=data.get('buying')
        maint=data.get('maint')
        doors=data.get('doors')
        persons=data.get('persons')
        lug_boot=data.get('lug_boot')
        safety=data.get('safety')
