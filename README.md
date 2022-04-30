# Restaurant

How to run:
-------------
1. install docker
2. cd ./api -> docker-compose up
* Api service takes few seconds to start because the process is waiting the database.
3. cd ./front -> docker-compose up
* Start api service before frontend because it refers the external network defining in backend's docker compose.


Web Application
-------------
localhost:3000


API Document
-------------
localhost:8000/docs
