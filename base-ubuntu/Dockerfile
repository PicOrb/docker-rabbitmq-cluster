FROM phusion/baseimage
MAINTAINER Biju Kunjummen biju.kunjummen@gmail.com

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
RUN curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -
RUN echo "deb http://packages.erlang-solutions.com/ubuntu trusty contrib" >> /etc/apt/sources.list
RUN curl http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc | apt-key add -

RUN apt-get update && apt-get install -y wget unzip tar git openssl

#Dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y default-jdk build-essential libncurses5-dev openssl libssl-dev fop xsltproc unixodbc-dev

#Erlang
RUN wget --no-check-certificate https://packages.erlang-solutions.com/erlang/esl-erlang-src/otp_src_R16B03-1.tar.gz && \
    tar xvf otp*tar.gz && \
    rm otp*tar.gz
RUN cd otp_src* && \
    ./configure && \
    make && \
    make install
RUN rm -rf otp_src*
RUN echo 'export PATH=/usr/local/lib/erlang/lib/erl_interface-3.7.15/bin:$PATH' >> /root/.bashrc

#RUN apt-get update && apt-get install -y \
#  erlang=1:17.4 \
#  erlang-base-hipe=1:17.4

RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates rabbitmq-server

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
ADD ./rabbitmq-server /etc/default/rabbitmq-server
RUN chmod u+rw /etc/rabbitmq/rabbitmq.config

RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_mqtt rabbitmq_stomp rabbitmq_management rabbitmq_management_agent rabbitmq_management_visualiser rabbitmq_federation rabbitmq_federation_management sockjs

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
