# UK-tax-income-calculation
## Set up:
### Install virtual env virtualenv
````
python -m pip install --user virtualenv
````
### Create and activate virtual environment
````
virtualenv env
source env/bin/activate
````
### Install python 3
````
pip install python3
````
### Install project dependencies
````
pip install -r requirements.txt
````
### To run Flask server
```
flask run --host=0.0.0.0 --port=5000
Access with browser to: http://127.0.0.1:5000/
```

### Tax bands configurations
The tax bands can be configurated on JSON file tax_bands.json
```
"rate": is the band rate 
"top": is the maximum value of the band 
"bottom": is the minimum value of the band
```
# Income tax endpoint


POST http://127.0.0.1:5000/income-tax

REQUEST
```json
{     
    "income": "52000"
}
```

RESPONSE
```json
{
    "tax": 8300.0
}

```
