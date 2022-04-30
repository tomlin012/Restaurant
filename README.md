# Restaurant

How to run:
-------------
1. install docker (https://www.docker.com/get-started/)

2. . cd ./api -> docker-compose up
* If cpu is Intel, remove `platform: linux/amd64` in docker-compose file.yaml.
* Api service takes few seconds to start because the process is waiting for the database.

3. cd ./front -> docker-compose up
* Start api service before frontend because it refers the external network defining in backend's docker compose.


Web Application
-------------
localhost:3000
### features:
Use navigation bar to go through different features.
1. Insert order -> `/order`
2. Search and delete order in specified table -> `/table`
3. Search specified item -> `/item`



API Document
-------------
localhost:8000/docs
