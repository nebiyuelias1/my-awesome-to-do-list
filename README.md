# My awesome To do list
## Backend
The backend of this project is built using FastAPI.

### Requirements
* Intall [Git](https://git-scm.com/downloads) for your system.
* Install [Python](https://www.python.org/downloads/) for your system (It has to be version 3).
* Install [PostgreSQL](https://www.postgresql.org/download/) and set the following details on the database:
  - Database user: `todouser`
  - Database password: `testpassword`
  - Database name: `tododb`
  
  **NB**: If you want to setup a different DBMS, you can do that. But make sure to update the connection string in the database.py file:
  ```SQLALCHEMY_DATABASE_URL = "postgresql://todouser:testpassword@localhost/tododb"```
  
### Steps to run this project
* Clone the repository by doing: ```git clone https://github.com/nebiyuelias1/my-awesome-to-do-list.git```
* Navigate to the cloned directory by: ```cd my-awesome-to-do-list```
* Navigate to the backend directory by: ```cd backend```
* Create a virtual environment name **venv** using: ```python -m venv venv```
* Activate the virtual environment: ```source venv/bin/activate``` (But this command might be different for your OS, this one is tested on Linux)
* Install the depencies: ```pip install -r requirements.txt```
* Run the project using: ```uvicorn app.main:app --reload```

