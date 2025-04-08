from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

items_db = []

origins = [

    'http://localhost:8000',
    'http://localhost:3000'
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/form/")
async def check(name: str='', email: str=''):

    if name_empty(name):
        return 'Please enter a valid name'
    
    elif email_empty(email):
        return 'Please enter a valid email'
    
    elif email_exists(email):
        return 'Email already exists'
    
    else:
        items_db.append({"name": name, "email": email})
        return 'Thanks'
    
@app.get("/items/")
async def get_items():
    return items_db

def name_empty(name):
    if name == '' or name == None:
        return True
    return False

def email_empty(email):
    if email == '' or email == None:
        return True
    return False
            
def email_exists(email):
    for item in items_db:
        if email == item["email"]:
            return True
        
    return False


