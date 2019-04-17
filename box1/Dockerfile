FROM alpine

RUN mkdir /run/sshd && apk add --no-cache --update openssh-server openssh 

RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa
RUN touch /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_ecdsa_key && touch /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_ecdsa_key

RUN adduser -g "bobby brown" -D "bob" && mkdir -p /home/bob/.ssh/ && chown -R bob:bob /home/bob && echo "bob:bobiscool" | chpasswd

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
