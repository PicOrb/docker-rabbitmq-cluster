FROM centos:centos6
MAINTAINER Biju Kunjummen biju.kunjummen@gmail.com

RUN yum install -y wget unzip tar git openssl

RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum install -y erlang

RUN rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc

RUN yum install -y  http://www.rabbitmq.com/releases/rabbitmq-server/v3.2.1/rabbitmq-server-3.2.1-1.noarch.rpm

#CMD /usr/sbin/rabbitmq-server

ADD erlang.cookie /var/lib/rabbitmq/.erlang.cookie

RUN chown rabbitmq:rabbitmq /var/lib/rabbitmq/.erlang.cookie

RUN chmod 400 /var/lib/rabbitmq/.erlang.cookie

# RabbitMQ
RUN git clone git://github.com/joemiller/joemiller.me-intro-to-sensu.git
RUN cd joemiller.me-intro-to-sensu/; ./ssl_certs.sh clean && ./ssl_certs.sh generate
RUN mkdir /etc/rabbitmq/ssl
RUN cp /joemiller.me-intro-to-sensu/server_cert.pem /etc/rabbitmq/ssl/cert.pem
RUN cp /joemiller.me-intro-to-sensu/server_key.pem /etc/rabbitmq/ssl/key.pem
RUN cp /joemiller.me-intro-to-sensu/testca/cacert.pem /etc/rabbitmq/ssl/
ADD ./rabbitmq.config /etc/rabbitmq/
RUN chmod u+rw /etc/rabbitmq/rabbitmq.config

RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_mqtt rabbitmq_stomp rabbitmq_management rabbitmq_management_agent rabbitmq_management_visualiser rabbitmq_federation rabbitmq_federation_management sockjs