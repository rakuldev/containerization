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


### Docker
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

Some basic commands:
```
docker images                               # view the docker images
docker ps                                   # view the running containers
docker ps -a                                # view all the containers (stopped ones too)
docker rmi image-name/id                    # remove an image
docker build -t dockerusername/repo:tag     # build the Dockerfile
docker run image                            # to run the docker image that has been created before
```
