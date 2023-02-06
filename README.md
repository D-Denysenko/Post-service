# Post Service

## Basic Commands

### How to run application using docker-compose


        $ docker-compose -f local.yml build

        $ docker-compose -f local.yml up


### Docs

All endpoint you can see on the next link:

        $ http://0.0.0.0:8000/api/docs/

### Testing bot


    $ docker-compose -f local.yml run django pytest tests/bot.py

All variables placed in that scripts.
