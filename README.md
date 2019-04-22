# ssh_python_tunnels
The user must be fluent in python and ssh tunnels to win.

After setup the user should have a network similar to below.

![Network Diagram](https://github.com/aringo/ssh_python_tunnels/raw/4061f3e0b2241786f697b7df7754745915375018/Setup.jpg "Network Diagram")

### Setup
Clone project and build using docker compose.

```
git clone https://github.com/aringo/ssh_python_tunnels.git
cd ssh_python_tunnels/build    
docker-compose up
```
Then in your browser of your choice navigate to 

http://localhost:3000 and try logging in as user:start

After that you should be able to open more windows with
```
http://localhost:3000/wetty/ssh/user?sshpass=start
```

Optionally you may ssh into box0 to begin with your native client, ssh user@192.0.2.3

### Cleanup

```
# stop all running containers
for i in $( docker ps -a -q ) ; do docker stop $i ; docker rm $i ; done

# remove all running images
docker rmi callback box2 box1 box0 wetty alpine krishnasrinivas/wetty

docker network prune
```
