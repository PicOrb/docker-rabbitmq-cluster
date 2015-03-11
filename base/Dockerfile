FROM centos
MAINTAINER Biju Kunjummen biju.kunjummen@gmail.com

RUN yum install -y wget unzip tar 

RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm

RUN yum install -y erlang

RUN rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc

RUN yum install -y  http://www.rabbitmq.com/releases/rabbitmq-server/v3.5.0/rabbitmq-server-3.5.0-1.noarch.rpm

RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_mqtt rabbitmq_stomp rabbitmq_management  rabbitmq_management_agent rabbitmq_management_visualiser rabbitmq_federation rabbitmq_federation_management sockjs

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
