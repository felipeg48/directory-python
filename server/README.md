# Server

## Run

```shell script
FLASK_APP=app.py flask run
```

## Get All Persons

- With `httpie`
   ```shell script
    http :5000/
   ```

## Adding a new Person

- With cURL:
   ```shell script
   curl -XPOST -H "Content-Type: application/json" -d '{"email":"felipe@email.com","name":"Felipe","phone":"1-800-AWESOME"}' localhost:5000/persons
   ```
- With `httpie`:
   ```shell script
   http :5000/persons email="felipe@email.com" name="Felipe" phone="1-800-awesome"
   ```
  
  
## Update a Person

- With `httpie`:
   ```shell script
   http PUT :5000/persons email="felipe@email.com" name="Felipe Gutierrez" phone="1-800-awesome"
   ```

## Delete a Person

- With `httpie`:
   ```shell script
   http DELETE :5000/persons/felipe@email.com
   ```
