# django-schools-map
An app to show schools locations on map with django, react, postgis, nginx and docker

## Configure the Application
Please make a copy of the '.env.example' file and update the variable values as needed. If necessary, modify docker-compose as needed.

## Run the Application
```
cd django-schools-map
run the command: make build
navigate to localhost:8088
```

## If you prefer traditional docker command
```
cd django-schools-map
run the command: docker compose --build -d --remove-orphans
navigate to localhost:8088
```
