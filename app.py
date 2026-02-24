from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.User_input import User_input 
from Model.predict import MODEL_VERSION ,predict_output
from schema.prediction_response import PredictionResponse

app=FastAPI()



@app.get('/')
def home():
    return {'message':'insurance premium predictions api'}

@app.get('/health')
def health():
    return {
        'status':'ok',
        'version': MODEL_VERSION
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:User_input):

    user_input = {
        'bmi':data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code = 200,content={'response':prediction})
    
    except Exception as e :
        return JSONResponse(status_code=500,content=str(e))




    

    
