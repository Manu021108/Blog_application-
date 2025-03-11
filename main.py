from  fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return{'data':{
        'Name': 'Manish'
    }}
@app.get('/about')
def about():
    return {
        'data':{
            'About Page'
        }
    }