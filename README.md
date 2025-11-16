 # Containerization
Putting on my understanding of containers, use cases of containers, reason behind using containers, and few practical examples from the repository to enhance the understanding of docker &amp; containers

Engineering is not only about building something new or working, it all about achieving efficiency in something. So does devops tools are designed to induce 100% utilization of resources. Containerization is similar process which we will look in a detail. 

### What are Containers? 
Containers are environments which has been created for covering various use-cases. In general, a container is an environment which can encapsulate the application data, app specific dependencies, and packages to an unified space and execute them in an isolated manner. Containers can serve as a run-time environment to execute microservices/monolith applications, and have their own filesystem which would compress all the essential data needed specifically for the application to run independently.

### Why Containers? 
Before jumping into containers, let's have a look into a server (i.e., nothing but a computing environment with large filesystem). A server typically has an Operating System (Linux, Windows, MacOS), and provides us an environment to develop and deploy our application. Traditionally, before the rose of cloud, this is how things were. But later, many new startups, even MNCs noticed a lack of efficiency in their systems which is they pay for something which they don't utilize. To have a clear picture, we'll first understand how data-centers and servers in them provide the access to create our namespace in their instances. 

This is how typically an AWS VM setup looks like:

<img width="900" height="516" alt="image" src="https://github.com/user-attachments/assets/c8e0c4c3-1f4e-4063-83b8-26a4575036c8" />

To gain access to a ssh namespace, a developer will essentially choose the type of Operating system that he/she is going to deploy and play around, and further details will be entered. Now in AWS's architecture, they are trying to completely use the server's resources by placing a bare-metal hypervisor on top of the Linux machine. 

### Now what is a Hypervisor? 
Hypervisor is a tool which runs on top of the kernel (the place where system software communicates to the hardware/CPU to request for resources via system calls) of the host operating system or hardware depending upon its type and provides a virtual environment where we can spin up our virtual machines.
Type 1: Bare-metal hypervisor: Runs directly on top of hardware. The Xen hypervisor would be a potential example for the same.
Type 2: Hosted Hypervisor: Runs on a host OS enabling us to create multiple guest OS. VMWare Virtualbox could be an example.

Lets imagine that we have a Linux server, on which we have 4 VMs each running its own microservice. Now everything will be up and running, and there will not be any overhead in the app availability, but the concern is totally the resources that its consuming. 
Revisiting the same architecture: 

<img width="900" height="516" alt="image" src="https://github.com/user-attachments/assets/3f3e8a14-381c-4bba-b039-5c846b83623c" />

Here, we can clearly see that the microservices doesn't really consume the entire pool of resources from the VMs, ending up wasting a lot of storage space, RAM and etc., 

The reason why each microservice is being hosted in different VM is:
- Each microservice would require a different configuration and clearly to facilitate communication between each of them
- We would need them to be isolated in a different environment which would be a best practice too
so, that the shared resources from the CPU could be used, avoiding the dependency congestions. As a result, this architecture can lead to higher infrastructure costs and lower resource utilization, where the containers comes into place.

### How container solve this problem?

<img width="900" height="516" alt="image" src="https://github.com/user-attachments/assets/f1ab1ac0-17f0-48ca-90bf-84b7350d46b9" />

Now, each microservice has been assigned with a resource (i.e., container) and all those exists in one single VM saving a lot of disk space, RAM and budget for the organization. Even though, the primary reason behind relying on container is to utilize resources effectively, there is another stong reason as well which is <b>isolation</b>. So each docker container has a level of isolation which is desired and security aspect. Imagine if containers share the same set of dependencies other than shared resources/libraries from the host OS, like packages, libraries. This system would be vulnerable in such case, so considering that, and to isolate each microservice, containers has some level of isolation. It could not be like VMs as they have their own OS, Ram limit and storage etc., but still, containers have their own filesystem.

A typical ubuntu based docker container might have:
- /bin - binary executable resources
- /sbin - system binary executable resources
- /etc - configuration files & data-driven libraries
- /usr - user information
likewise, it goes on depending upon the type of container.

Resource transmission workflow:

<img width="1006" height="433" alt="image" src="https://github.com/user-attachments/assets/55e6fbba-8789-4146-9713-85646fbcb200" />


## Docker
Docker is a container run time environment which serves as a platform to ease the container creation, start and other processes. Typically a docker engine would consist of:
- Docker CLI
- Docker API
- Docker daemon

Docker workflow:

<img width="1324" height="235" alt="image" src="https://github.com/user-attachments/assets/978d0337-12c5-4786-8248-4e139f63456b" />

As we can see: Docker daemon is responsible for the creation, and images which obviously will also be a Single Point of Failure. If the daemon is down, container orchestrator calls would fail resulting in system downtime.

### Lifecycle of docker
It all starts with the Dockerfile creation. There are three fine steps:
- docker build
- docker run
- docker push (push your image to the registry [Optional])

<img width="700" height="384" alt="image" src="https://github.com/user-attachments/assets/825debe7-4dc1-4dd1-b8ed-3eb095fa86b6" />

Inorder to push to docker registry/any artifactory (like Jfrog), we'll need an account and place it to our terminal to enable remote pull & push. So lets login to https://www.docker.com and create an account and follow these steps:
- Click on profile
- Go to account settings
- Choose "Personal access tokens"
- Hit "Generate new token"
- Make sure to note down the token

On terminal:
```
docker login -u username
```
and then, paste the token. 

Some commands used on day-to-day basis:
```
docker images                               # view the docker images
docker ps                                   # view the running containers
docker ps -a                                # view all the containers (stopped ones too)
docker rmi image-name/id                    # remove an image
docker build -t dockerusername/repo:tag     # build the Dockerfile
docker run image imageid                    # to run the docker image that has been created before
  flags:
    - -d - detached mode (will run the container in background and will let you continue to interact with the container without any hindrance
    - it - Interactive terminal
    - --rm - auto-remove container when stops
    - --name - obviously the container name
    - -p - port mapping
    - --network - connect to specific network
    - -v - to bind/mount a volume to the container (to have logs, persistant db volumes, run app without building)
    - -w - set the working directory
    - -e or --env - environment variable set
    - -m or --memory - to set memory
    - --cpus - to limit CPU usage
    - --cpuset-cpus - to assign to specific cores
there are a quite more, with regards to health checks, security & compliance, restarts, logging etc.,
docker image prune
  options:
    - -a or --all                           # docker image prune -a
    - --filter                              # docker image prune --filter="until=24h" [until=<timestamp>) the dangling images existing until the last 24 hours would be erased] 
    - -f or --force                         # docker image prune -f
docker container prune
  options:
    - --filter                              # docker container prune --filter="until=24h" [until=<timestamp>) the crashed or stopped containers created until last 24 hours should be erased]
    - -f or --force                         # docker container prune -f
docker exec appname -it /bin/bash           # to open a local terminal within container [ -i (interactive), -t (terminal), appname - WORKDIR ]
docker logs -f appname                      # to view logs
docker inspect appname                      # to view the container detials (like ip address, etc.,)

for more details, visit the docker cli docs: https://docs.docker.com/reference/cli/docker/ 
```

Dockerfile is a file where we write down all our steps to perform containerization of docker builds. 

### Best Practices
Before getting into multistage dockerfile and docker compose, let's take a look into some best practices to have a core understanding and efficient usage of docker file. 

<b>layering</b>:
  Every line written in the docker file would be a layer, and would be a cache. Docker layer cache checks if current instruction AND all previous instructions are unchanged. Lets say:
  ```
  FROM ubuntu 
  RUN sudo apt-get update && sudo apt install python3 python3-pip
  COPY requirements.txt .
  RUN pip install requirements.txt
  COPY . /app
  ```
Each of these instructions will take place sequentially. Which means, on running the same set of code without any changes, will lead to a faster execution: 
 ```
  FROM ubuntu                                                      (no changes) - CACHE HIT!
  RUN sudo apt-get update && sudo apt install python3 python3-pip  (no changes) - CACHE HIT!
  COPY requirements.txt .                                          (no changes) - CACHE HIT!
  RUN pip install requirements.txt                                 (no changes) - CACHE HIT!
  COPY . /app                                                      (code changes) - CACHE MISS!
  ```
But there could be various other scenarios as well. 

Build 1 (first time):
- Line 1: MISS (no cache exists yet) → downloads base image
- Line 2: MISS → installs linux packages
- Line 3: MISS → copies file
- Line 4: MISS → installs packages (2 minutes)
- Line 5: MISS → copies code

Build 2 (you changed only app.py):
- Line 1: HIT → skips (base image unchanged)
- Line 2: HIT → skips (same packages)
- Line 3: HIT → skips (requirements.txt unchanged)
- Line 4: HIT → skips (layer above hit + instruction unchanged)
- Line 5: MISS → rebuilds (source code changed)

Build 3 (you added a package to requirements.txt):
- Line 1: HIT → skips
- Line 2: HIT → skips
- Line 3: MISS → rebuilds (file content changed)
- Line 4: MISS → rebuilds (layer above missed)
- Line 5: MISS → rebuilds (layer above missed)

So, now we could get a clear context that, if one line changes, the following sequence of lines will miss the cache and rebuilds again. Each layer is being rebuilt.

Next, lets understand port mapping during run. What is port forwarding? 
Since we have different layers (i.e., container within a VM, we should be running our application in container, but the customer hits the load balancer -> VM where the machine will not have any idea of what the port means).
So mapping container port to VM's port is a mandatory part in web applications. 

```
docker run -d -p 8000:8000 myapp                         # -d - run in detached mode, -p - port. docker run -p <host_port>:<container_port> image
```

Docker has various commands to look for, but its not possible to remember all of them by heart, so developers rely on docs sometime to gather knowledge as needed. One of the important usage utility - Mount; which is used for doing various things. 

```
RUN docker ---mount=type=cache,target=/root/.cache/pip \
pip install requirements.txt
```

Here, the catch is, when there is a cache miss, the layer would be re-run completely. For instance, there's a change in requirements.txt, the installation layer that comes after that will actually re-install the entire set of packages residing in requirements.txt. But when we use mount alongside cache, then we would actually store the pypi packages within cache (basically the location we are putting our cache is the location where the pip packages sit in, we are converting it into a cache so it will stay unchanged and only the newer ones will be added to it). NOTE: The docker manages the volume in the host not in the container as container doesn't have a FS (Filesystem). 

There are a quite lot of attribute types we can have for mount like:
- secret
- volume
- tmpfs

### Docker Networks
<img width="1155" height="669" alt="image" src="https://github.com/user-attachments/assets/ad51710a-3c72-4801-8f20-d30eb46d2c8c" />

In a systems perspective, this architecture seems reilable and enables communication between microservices and to host, but in a security point of view, there is a shared point of contact, which would be a root cause to <b>Single Point of Failure</b>. When 2 containers shares network traffic flow would disrupt since containers resides private behind a network, and this would mimic the NAT architecture. 
- NAT - Network Address Translation: When a virtual machine resides in a host server machine, it basically shares the ip of host. It is create entrypoint for the incoming traffic.
- Bridge - This would make the service (the containers) appear as a seperate device within the network. This will allow isolation between services and host and enables synchronous flow of communication between the containers without jeoparadizing the system. 

Docker Network commands:
```
docker network ls                                               # to list the set of networks associated with the containers
docker run -d container_name --network=network_type image_name  # to set the network type to a container         
```

## Docker Compose:
So far, we saw Docker which is a container run time environment. Basically docker is one environment that can hold a single service in its filesystem, likewise multiple microservices are consolidated in-order to form an application. We need microservices to communicate to each other to have a successful execution of a service, also we need something which could manage the container all in one single environment, because in enterprise software, we'll have a huge bucket of microservcies which should be put on place manually one-by-one which is not efficient. To solve that issue, and also to perform local checks all-in-one instead of going on for k8s for orchestration, we use docker-compose, as it manages containers on basis of the dependencies. 

Lets look into the format of docker-compose and some important attributes of it. Fundamentally, docker compose uses YAML which carries the containers, networks, volumes & etc., in it. Each entity carries its own attributes. 

We'll have compose.yaml (previously called docker-compose.yaml - a file rename with no technical modifications happened of 2021), which we'll be building just like Dockerfile. 

### Format of docker-compose:
```
compose.yaml

# version
version: '4.1'

# containers
services:
  app1:
    image:
    ports:

  app2:

volumes:
  volume1:

networks:
   mynet: 
```

### Service Attributes:
1. Image vs Build:
```
# Use existing images from local or remote

services:
  web:
    image: python:3.11-alpine

# Create image from Dockerfile

services:
  web:
    context: ./build          # Location of where the Dockerfile resides
    dockerfile: Dockerfile    # Name of Dockerfile (since Dockerfile can be of any name like Dockerfile.dev or whatever the developer wishes to) \
```

2. Environment:
```
environment:
  - NODE_ENV=prod
  - API_KEY=key

environment:
  - NODE: prod
  - API_KEY: key

env_file:
  - .env
```

3. Ports:
```
ports:               # Its always host:container
  - 8000:8000
  - 8080:80 
```

4. Volumes:
```
services:
  volumes:                      # its always host:container
    - $(pwd):/var/lib/mysql     # Named volume
    - $(pwd):./app              # bind mount

    - ./config/json:/app/config.json:ro     # read-only
```

5. Networks:
```
services:
  web:
    networks:
      - frontend
      - backend

  db:
    networks:
      - backend
networks:
  - frontend:
  - backend:
```

6. Depends On (Critical one):
```
services:
  app:
    depends_on:
      - db
      - cache   # meaning if these services are up, only then the app will be turned up and running (for service reliability)
```

7. Command & Entrypoint:
```
services:
  app:
    - image: python:3.11-alpine
    - command: python app.py
      # Overrides Dockerfile's CMD

      # Even multiple commands can be used
    - command: sh -c "python manage.py migrate &&
                   python manage.py runserver 0.0.0.0:8000"
    - entryoint: /bin/bash
```

8. Working Directory:
```
services:
  app:
    working_dir: /app
```

9. Restart Policy:
```
services:
  app:
    restart: no
    restart: always
    restart: unless-stopped 
    restart: on-failure
```

10. Resource limits (CPU & RAM mostly):
```
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
        reservations: 
          cpus: '0.25'
          memory: 256M
```

11. Container name:
```
services:
  app:
    container_name: web1
```

There are a few more like health check, labels, logging etc., which a simple google search might get you the format. Building a docker compose is pretty simple if you know how the system works, as compose is nothing but a architecture written in a compute file. If you know how to build it and work it locally, you can build the compose file pretty easily with the attributes that we have in place. 

### Docker Compose commands
```
# turn up the containers & system
docker-compose up

# start the services in detached mode
docker-compose up -d

# stop services
docker-compose stop

# stop services & remove containers
docker-compose down

# stop & remove volumes
docker-compose down -v

# stop & remove containers + images
docker-compose down --rmi all
```

### Docker Compose build commands
```
# build images
docker-compose build

# build images without cache
docker-compose build --no-cache            # We saw something before that Dockerfile runs every line and stores them as cache, and if nothing changes, cache HIT will happen, to avoid usage of cache and restart everything, we use this.

# build specific service
docker-compose build app

# build & start
docker-compose up --build

# force recreate containers
docker-compose up --force-recreate
```

### Log Monitoring
```
# see logs
docker-compose logs

# see live-logs
docker-compose logs -f

# logs for specific service
docker-compose logs app

# last 100 lines (basic linux commands like [tail & head])
docker-compose logs --tail=100

# with timestamps
docker-compose logs -t 
```

### Service Management
```
# see running containers
docker-compose ps

# see all containers
docker-compose ps -a

# Execute command in a service
docker-compose exec app bash
docker-compose exec db mysql -u root

# run one specific command in a service
docker-compose run app python manage.py migrate

# scale up the service (The k8s pods can manage it in production level usecases)
docker-compose up -d --scale app=3

# restart service
docker-compose restart app

# stop service
docker-compose stop app

# remove stopped containers
docker-compose rm
```

### Other commands
```
# pull images
docker-compose pull

# push images
docker-compose push

# pause services
docker-compose pause

# unpause services
docker-compose unpause

# show head processes
docker-compose top
```
To learn more about creating docker compose for various frameworks & languages, take a look into: https://github.com/docker/awesome-compose 
