# Instructions
 The url endpoint is 
 - www.website.com/**getDetails**

 **POST** inputs:
- `name`: name of the person
- `dob`: date of birth of the person
### Install dependencies
- run `pip install -r requirements.txt`

### Responses:
#### Message: 
    {
        "message": "You have have not claimed anything",
        "name": "hello"
    }
#### Error:
    {
        "error": "Please check your inputs"
    }

### Run 
- `python runDebug.py` or `python run.py`