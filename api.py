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
    description: str
    code_snippet: str
    created: str


@app.get('/')
async def home():
    return {"Message": "Welcome to Code Snippet API"}


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
        
        # If there is a data retrieved
        if item:
            item["_id"] = str(item["_id"])
            return item
        
        # If there is no data retrieved
        return {"Message": "No code snippet data found"}
    
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}
    

# Get by name of the coder or language
@app.get('/code-snippet')
async def get_code_snippet_by_query_params(coder_name: Optional[str] = None, 
                                   prog_language: Optional[str] = None):
    try:
        cursor = collection.find()
        filtered = [
            doc 
            for doc in cursor 
            if coder_name in doc.values() or 
               prog_language in doc.values()
        ]
        
        # Convert ObjectID type to string
        convert_obj_id_to_str(filtered)
        
        return filtered if filtered else {"Message": "No code snippets data found"}
        
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}
    
    
# Insert code snippet data
@app.post('/create-code-snippet')
async def create_code_snippet(data: CodeSnippet):
    try:
        collection.insert_one(dict(data))
        
        # Return a response when a code snippet data is successfully inserted to the database
        return [
            {"message": "Successfully created code snippet data" },
            dict(data),
        ]
    
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}


# Update code snippet data
@app.put('/update-code-snippet/{code_snippet_id}')
async def update_code_snippet(code_snippet_id: str, data: CodeSnippet):
    try:
        collection.find_one_and_update({"_id": ObjectId(code_snippet_id)}, {
            "$set": dict(data)
        })
        
        # Return a response when a code snippet data is successfully updated in the database
        return [
            {"message": "Successfully updated code snippet data" },
            dict(data),
        ]
        
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}
    
    
# Delete code snippet data
@app.delete('/delete-code-snippet/{code_snippet_id}')
async def delete_code_snippet(code_snippet_id: str):
    try:
        object_id  = ObjectId(code_snippet_id)
        item = collection.find_one_and_delete({"_id": object_id})
        item["_id"] = str(item["_id"])
        
        # Return a response when a code snippet data is successfully deleted in the database
        return [
            {"Message": "Successfully deleted code snippet data"}, dict(item)
        ] if item else {"Message": "No code snippet data found for deletion"}
    
    except Exception as e:
        return {"Message": f"Error: {str(e)}"}
    

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()
    
    

