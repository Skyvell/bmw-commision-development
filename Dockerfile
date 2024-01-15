FROM amazonlinux:2

RUN yum install -y python3-pip zip
RUN python3 -m pip install --upgrade pip

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt -t /var/task/python/lib/python3.11/site-packages/

CMD ["sh", "-c", "cd /var/task && zip -r /var/task/lambda-layer.zip python"]
