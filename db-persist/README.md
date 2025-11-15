### Create a database (ANY) and attach it to a host volume to make the data persist regardless of the container availability

Your task:
- Create a volume 
- Create a container (mysql:9.5.0 or postgre:15)
- Attach the volume to container while spinning it up (docker run)
- Test the working by removing the container and re-creating and login to the db 
