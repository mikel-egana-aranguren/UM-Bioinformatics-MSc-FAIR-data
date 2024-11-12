FROM openjdk:8-buster

RUN mkdir /blazegraph 
RUN cd /blazegraph 

ADD blazegraph.jar /blazegraph/blazegraph.jar
ADD entrypoint.sh /blazegraph/entrypoint.sh

RUN chmod +x /blazegraph/blazegraph.jar
RUN chmod +x /blazegraph/entrypoint.sh

EXPOSE 9999

WORKDIR /blazegraph

ENTRYPOINT ["/blazegraph/entrypoint.sh"]