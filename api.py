from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
import pymongo


# Database Route
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dev_db"]
collection = db["code_snippets"]


app = FastAPI()


def convert_obj_id_to_str(data_list: list[dict]):
    for data in data_list:
        data["_id"] = str(data["_id"])
        

# Class for creating Code Snippet
class CodeSnippet(BaseModel):
    coder: str
    language: str
    code_snippet: str
    created: str


@app.get('/')
async def home():
    return {"Message": "Hello World!"}


# Get all code snippets
@app.get('/code-snippets')
async def get_all_code_snippets():
    try:
        cursor = collection.find()   
        filtered = [doc for doc in cursor]
        
        # Convert ObjectID type to string
        convert_obj_id_to_str(filtered)
            
        return filtered
        
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}


# Get by id
@app.get('/code-snippet/{item_id}')
async def get_code_snippet_by_id(item_id: str):
    try:
        object_id  = ObjectId(item_id)
        item = collection.find_one({"_id": object_id})
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")  # Return a 404 response for not found items
        item["_id"] = str(item["_id"])
        
        return item
    
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}
    

# Get by name of the coder or language
@app.get('/code-snippet')
async def get_code_snippet_by_name(coder_name: Optional[str] = None, 
                                   prog_language: Optional[str] = None):
    try:
        cursor = collection.find()
        filtered = [
            doc 
            for doc in cursor 
            if coder_name in doc.values() or 
               prog_language.title() in doc.values()
        ]
        
        # Convert ObjectID type to string
        convert_obj_id_to_str(filtered)
        
        return filtered if filtered else {"Message": "No Code Snippets Found"}
        
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}
    
    
# Insert data
@app.post('/create-code-snippet')
async def create_code_snippet(data: CodeSnippet):
    try:
        collection.insert_one(dict(data))
        result = collection.insert_one(data)
        
        # Return a response when a code snippet data is successfully inserted to database
        return {"message": "Code snippet created", "inserted_id": str(result.inserted_id)}
    
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}


# Update data


def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()
    
    

