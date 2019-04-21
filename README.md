# ssh_tunnels
The user must be fluent in python and ssh tunnels to win.

Build using docker compose.  
```
cd build 
docker-compose up
```
Then in your browser of your choice navigate to 

http://localhost:3000 and try logging in as user:start

After that you should be able to open more windows with
```
http://localhost:3000/wetty/ssh/user?sshpass=start
```
Optionally you may ssh into box0 to begin with your native client, but you should not be able to ssh directly into other systems. 