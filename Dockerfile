FROM ubuntu
RUN apt-get install -y python python-setuptools ca-certificates
RUN sudo easy_install pip
RUN pip install apache-libcloud
ADD update.py /opt/docker-libcloud-dns/update.py
ENTRYPOINT ["/usr/bin/python", "/opt/docker-libcloud-dns/update.py"]
