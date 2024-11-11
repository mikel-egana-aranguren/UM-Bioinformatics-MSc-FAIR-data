# Linked Data Server

## About

This is a standalone, hassle-free [Linked Data](https://www.w3.org/standards/semanticweb/data) server. It is meant for teaching purposes, so do not use in production.

The bundle comprises:

* [Blazegraph](https://github.com/blazegraph/database) as Triple Store in `/blazegraph`.
* Trifid

## Dependencies

* Docker (version)
* docker-compose (version)

## Configuration

docker-compose file

## Usage

* `docker build -t="blazegraph" .`
* `docker-compose up` 




* Execute Blazegraph at `/blazegraph`: `java -server -Xmx4g -jar blazegraph.jar`. To change the port in which Blazegraph will listen, use `java -server -Xmx4g -Djetty.port=8181 -jar blazegraph.jar`.
* In `http://IP_NUMBER:9999/`, in the `NAMESPACES` tab, create namespace `um` and activate (click in "use").
* Load data from file `data/update.ttl` into Blazegraph at `http://IP_NUMBER:9999/`, in the `UPDATE` tab.
* Start Pubby at `LinkedDataServer/pubby/`: `java -jar start.jar jetty.port=3031`.
* To test content negotiation, try `curl -L --header "Accept: text/turtle" http://IP_NUMBER:3031/mikel`. Some data should be returned.
* To test the web frotend go to `http://IP_NUMBER:3031/mikel` with the browser and the following should appear: