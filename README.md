# kriptokitty
Based on my analysis the Data Model for the given task is depicted as follow: 
![alt text](https://github.com/whitehacker/kriptokitty/blob/main/gx/db.png?raw=true)

## Run the Application
1. Create and activate a Python virtual environment
    - `python3 -m venv env` (depends what python version do you use and how are your local Python setup)
    - `source env/bin/activate`
2. Install requirements.txt file 
    - `pip install -r requirements.txt`
3. Install PostgreSQL or any other preferred RDBMS, in our case we have used Postgres
    1. `brew install postgresql` (macOS)
    2. `sudo apt install postgresql postgresql-contrib` (Linux - Ubuntu)
4. Open `main.py` and add your database credentials
    1. You can use my below Heroku Database URL if you like to host the databasee on Heroku
        - `engine = engine = create_engine('postgresql://hhjardtsyafudh:369cb6e16691ec547da99b7ee1579ef52678f72e8c1dc1e7d85ddba477ea1e5b@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d19bk58uf580m2')`
    2. Or you can use your local DB engine but you should add your database credentials
        - `engine = engine = create_engine('postgresql://postgres:postgres@localhost/kriptokitty')`
5. Run the application
    - Open a new terminal and execute the below command:
        - `uvicorn main:app --reload`
6. View the Endpoints and utilize the API
    - Open a browser window and navigation to `127.0.0.1:8000/docs` (make sure you are accessing the right IP and port number)
7. For easy access, the API is hosted on Heroku servers and can be accessed at <https://kriptokitty.herokuapp.com/docs#/>