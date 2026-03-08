import json
import random
class load_json:
    def __init__(self,dict):
        self.dict = dict
    
    def load(self):
        x = random.randint(1,100)
        json_file= f"datafile/jfile{x}.json"
        with open(json_file, "w") as file:
            json.dump(self.dict,file,indent=4)
        return file

book={
    "name": "MyWork",
    "pages": 378,
    "Author": "Kanhaya Kumar"
}

q = load_json(book)
print(q)

        