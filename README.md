# MotorQ Task
- By Rudrank B

## Installation:
1. Install the modules with `pip install -r requirements.txt`
2. Run `python manage.py migrate`
3. define a .env file at `motorqtask/.env` with the following
```
AIRTABLE_KEY=<AIRTABLE KEY>
BASE_ID=<AIRTABLE BASE ID>
REDIS_URL=<REDIS URL>
```
4. Run the backend with `python manage.py runserver`


## TASK Completion:
    Rate Limiting Executed 
    Airtable populated with 20 records
    API endpoint to fetch data from airtable /coins
