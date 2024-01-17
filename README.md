# Katze's super cool microservice scaffold

This is intended as a relatively useful skeleton for building python microservices that comes with some nice built in tools, like job managment and prebuilt healthchecks, along with a ready-made docker/docker-compose for local development. The end goal here is to speed up development time, and handle a lot of the frustrating setup-y parts that get in the way of actually building stuff.

## How 2 use:

Anything asynchronous goes into celery_app, anything realtime can live in app. You should know how 2 python and stuff, keep your .env and anything with secrets in gitignore, and make as much use of config.py as possible for handling environmental variables. building and using the docker-compose bit follows pretty standard/expected docker behavior. Only really weird bit is celery's monitoring service is exposed on :5557 rather than :5555. 

