# Task 3 - Run Python code to connect to DB pool

A Python script that is used to connect to the PostgreSQL DB and execute queries as transactions.

The logic utilizes the Singleton pattern and is designed as a DB Connections Pool

(when we want to execute the query, we get 1 connection from the pool and after it is done it returns to the pool)

### 1. Install the required packages
```
$ pip install -r requirements.txt
```

### 2. Configure the connection data
```
/src/car_wash/python/users.py
```

### 3. Run the app
```
/src/car_wash/python/main.py
```
