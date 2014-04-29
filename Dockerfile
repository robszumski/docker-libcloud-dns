FROM ubuntu
RUN apt-get install -y python python-setuptools
RUN sudo easy_install pip
RUN pip install apache-libcloud
ADD . /opt/docker-libcloud-dns
ENTRYPOINT [/opt/docker-libcloud-dns/update.py]
