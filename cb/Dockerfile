FROM alpine

RUN apk add --update py3-pip

COPY callback.py /usr/src/app/

CMD ["python3","/usr/src/app/callback.py","box2"]
