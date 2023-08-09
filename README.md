# MotorQ Task
- By Rudrank Basant

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
    API endpoint /coins/price/id
    both scheduling/polling coin api works with 10 min and 1 min as mentioned



![image](https://github.com/rudrankbasant/motorq-task/assets/85751479/66c2636d-ed49-49ce-aefa-aed0852dbe0a)

![image](https://github.com/rudrankbasant/motorq-task/assets/85751479/7ed6df72-9db8-4815-ab83-d514b9f97e2e)

![image](https://github.com/rudrankbasant/motorq-task/assets/85751479/0ab1d87a-1585-4614-b1f8-dd60d5896023)


