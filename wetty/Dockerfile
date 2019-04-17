FROM krishnasrinivas/wetty 

EXPOSE 3000

CMD ["/bin/sh","-c","ssh-keyscan -H wetty-ssh >> ~/.ssh/known_hosts && node bin --sshhost box0"]
