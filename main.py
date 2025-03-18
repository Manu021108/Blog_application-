from  fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn


app = FastAPI()

@app.get('/blog')
def index(limit = 10, published:bool = True):
        if published:
            return {
                'data': f'{limit} published blogs from the db'}
        else:
             return{ 'data':f'{limit} published blogs from the db'}
        

        
@app.get('/about')
def about():
    return {
        'data':{
            'About Page'
        }
    }
@app.get('/contact')
def contact():
    return {
        'data':{
            'number':9553032002
        }
    }
@app.get('/blog/{id}')
def show(id:int):
    #fetch data with blog id
    return {
        'data':{id}
    }
@app.get('/blog/{id}/comments')
def show(id:int):
    #fetch data with blog id
    return {
        'data':{'Comments'}
    }
@app.get('/blog/{id}/unpublished')
def unpublished(id:int):
    #fetch data with blog id
    return {
        'data': 'All unpublished blogs'
    }
class Blog(BaseModel):
     title : str
     body : str
     published: bool  

@app.post('/blog')
def create_blog(blog: Blog):
     return {'data':'Blog is created'}



#if __name__ == "__main__":

    #uvicorn.run(app, host="127.0.0.1", port = 9000)
