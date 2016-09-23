[![Docker Pulls](https://img.shields.io/docker/pulls/delermando/locust-load-test.svg?maxAge=2592000)]() [![Docker Layers](https://images.microbadger.com/badges/image/delermando/locust-load-test:1.0.svg)](http://microbadger.com/images/delermando/locust-load-test:1.0 "Get your own image badge on microbadger.com") [![Docker Version](https://images.microbadger.com/badges/version/delermando/locust-load-test:1.0.svg)](http://microbadger.com/images/delermando/locust-load-test:1.0 "Get your own version badge on microbadger.com") 

# Locust Load Test  

## Introduction  
This is simple project that Dockerize **Locust** tool, allowing you to simply and quickly test.

## Requirements:  
1. git
2. docker
3. docker-compose

## How to use:  
**1ª Step:** Clone this project  
`git clone git@github.com:Delermando/locust-load-test.git`  

**2ª Step:** Accesse the project folder  
    `cd locust-load-test`  

**3ª Step:** Define test settings, editing the configuration file **src/load_test_definition.py**, on that you'll the property **host**. If you want define definir other configurations access [locust.io](http://docs.locust.io/en/latest/).  
![Definition test file]
(https://s32.postimg.org/fww94rmat/image.png)

**4ª Step:** Start container  
    `make run`  

**5ª Step:** Access the locust interface on browser on the following address `localhost:8089`  
![Locust Web Interface]
(https://s32.postimg.org/uu4q5rzj9/image.png)

**6ª Step:** First define the number of requests, concurrent users and so click on **start swarming** button  
![Requestes definition]
(https://s32.postimg.org/morq4qhlx/image.png)

**7ª Step:** Now enjoy  
![Tela final]
(https://s32.postimg.org/4zzzd45ut/image.png)

## Commands Refence
- **make run** (Start the project containers)
- **make kill**  (Kill all containers)
- **make rm**  (Remove all containers)
- **make restart** (Restart it's a combination of the **kill**, **rm** and **run** commands) 
