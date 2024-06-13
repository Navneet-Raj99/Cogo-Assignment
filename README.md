
# CogoPort Assignment API Documentation

API’S to develop a robust and scalable FastAPI application to manage a 
Configuration Management system for onboarding Organizations from each country

### Base_URL: 
Base URL for the API is http://localhost:8000

### Authentication:
No Authentication Method is used in it.

### Setup:
 


### Locally Setup (via GitBASH)

Setting up Virtual Environment:
```bash
source cogoport/scripts/activate
```
Installation and Setup of packages

```bash
pip install -r requirements.txt
```

Running the server

```bash
uvicorn app.main:app --reload
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file as the URL of postgreSQL

`DATABASE_URL="postgresql://{username}:{password}@localhost:{port}/cogoDb"` 




### API Routes:
1.) Create a Configuration: ROUTE FOR Creating Configuration
```bash 
    POST /api/create_configuration
```

2.) Get Specific Configuration: ROUTE FOR Creating Config via country_code

```bash 
GET /api/get_configuration/{country_code}
```

3.)  Update Specific Config. : ROUTE FOR Updating Config via country_code

```bash 
POST /api/update_configuration
```
4.) DELETE Specific Config.: ROUTE FOR Deleting Config via country_code
```bash
DELETE /api/delete_configuration?country_code=IND
```
## Made By

- [@Navneet Raj](https://github.com/Navneet-Raj99)

