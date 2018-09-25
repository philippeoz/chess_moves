# ChessMoves
Api to get possible moves of Chess Pieces based on current position.

[A temporary demo](http://chess.valfok.com)

## Challenge
Given a knight located on a coordinate chosen by the user find out all possible locations
where the knight can move in 2 turns.
You are expected to build an API.

### API
The api should:
 * receive cell coordinate (in Algebraic notation) and return an array with all possible locations where the knight can move within 2 turns

### Bonus
Some bonus points for implementing them correctly:
 - add docker/docker-compose :white_check_mark:
 - allow user to dynamically add rows/columns to the chessboard :white_check_mark: (max 26x26 [a-z])
 - save logs of all requests and results in a database :white_check_mark:

### Routes:

* /
* /admin/
* /api/
    * knight/
        * moves/

### How to Setup
Clone project:
-  `git clone https://github.com/philippeoz/chess_moves.git`

#### With Docker:

1. [Install docker](https://docs.docker.com/install/)
2. [Install docker-compose](https://docs.docker.com/compose/install/)
3. `cd chess_moves` to enter in project path.
4. `docker-compose up --build` or `docker-compose --build -d` (daemon)


#### With virtualenv:

1. [Install Postgresql](https://www.postgresql.org/download/) and create a database (let's say the name is `database`).
2. [Install Pipenv](https://github.com/pypa/pipenv): `pip install pipenv`
3. Enter in project dir: `cd myprofile`
4. `pipenv install`
5. `cd app`
6. Inside the 'app' dir, create a file `settings.ini` with the following configs:
    ```
    [settings]
    DEBUG=True
    DATABASE_URL=postgres://username:password@host/database
    ```
    There are more environment variables that can be configured in the `settings.ini`, see more on [settings module](https://github.com/philippeoz/chess_moves/tree/master/app/settings).
7. From here you can choose to enter virtualenv with `pipenv shell` or execute commands outside with `pipenv run  python ...`, the example will be outside, inside just remove the `pipenv run`.
8. `pipenv run python manage.py migrate`
9. `pipenv run python manage.py runserver`

### ToDo

 - Add all Chess Pieces
 - More endpoints/functions for pieces
 - More Tests
 - Improvements for better performance (something with asyncio maybe)
