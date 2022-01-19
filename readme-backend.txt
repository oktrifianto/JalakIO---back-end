
### ============= install mysql  =============

$ pip install flask-mysql

### ============= Running Development Mode ======

$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run -p 3001

### ============= git =============
# with main branch

$ git init -m main 

## ============= TODO ========
[] Checking Empty query in MySQL

[√] Create 'users' table
  - id                int PK auto_increment
  - username          varchar
  - email             varchar
  - password (hash)   varchar
  - first name        varchar
  - last name         varchar
  - address           varchar