FROM alpine

RUN mkdir /run/sshd && apk add --no-cache --update openssh-server openssh py3-pip 
RUN rm /usr/bin/nc

COPY motd /etc/motd
COPY math_challenge.py /usr/src/app/
COPY startsh /usr/src/app/

# setup ssh keys partially and change the config to allow port forwarding 
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa
RUN touch /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_ecdsa_key && touch /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_ecdsa_key
RUN sed -i "s/AllowTcpForwarding no/AllowTcpForwarding yes/g ; s/GatewayPorts no/GatewayPorts yes/g ;  s/#PermitTunnel no/PermitTunnel yes/g ;" /etc/ssh/sshd_config

RUN adduser -g "bobby brown" -D "bob" && mkdir -p /home/bob/.ssh/ && chown -R bob:bob /home/bob && echo "bob:bobiscool" | chpasswd

EXPOSE 22

CMD ["/bin/sh","/usr/src/app/startsh"]
