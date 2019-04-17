FROM alpine

RUN apk add --update py3-pip

COPY callback.py /usr/src/app/

CMD ["python3","/usr/src/app/callback.py","172.17.0.1"]
