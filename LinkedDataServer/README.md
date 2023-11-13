# Linked Data Server

## About

This is a standalone, hassle-free [Linked Data](https://www.w3.org/standards/semanticweb/data) server. It is meant for teaching purposes, so do not use in production.

The bundle comprises:

* [Blazegraph](https://github.com/blazegraph/database) as Triple Store in `/blazegraph`.
* [Pubby](https://github.com/cygri/pubby) as frontend for web browsing and content negotiation, i.e. "dereferencing", in `/pubby`.

## Dependencies

* Java. It has been tested with `OpenJDK Runtime Environment (build 11.0.20.1+1-post-Ubuntu-0ubuntu122.04)` on Ubuntu 22.04.1 LTS. Install Java with your favourite method (e.g. `sudo apt install default-jre`).

## Configuration

Blazegraph requires no further configuration.

Pubby:

* Edit `LinkedDataServer/pubby/webapps/ROOT/WEB-INF/web.xml` so that it points to the config file `blazegraph-config.ttl`:

```xml
  <context-param>
    <param-name>config-file</param-name>
    <param-value>blazegraph-config.ttl</param-value>
  </context-param>
```

* Edit the config file, with special care for:
  * `conf:webBase <http://IP_NUMBER:3031/>;`
  * `conf:sparqlEndpoint <http://IP_NUMBER:9999/blazegraph/namespace/um/sparql>;`
  * `conf:datasetBase <http://fair/data/>;` 

## Usage

* Execute Blazegraph at `/blazegraph`: `java -server -Xmx4g -jar blazegraph.jar`. To change the port in which Blazegraph will listen, use `java -server -Xmx4g -Djetty.port=8181 -jar blazegraph.jar`.
* In `http://IP_NUMBER:9999/`, in the `NAMESPACES` tab, create namespace `um` and activate (click in "use").
* Load data from file `data/update.ttl` into Blazegraph at `http://IP_NUMBER:9999/`, in the `UPDATE` tab.
* Start Pubby at `LinkedDataServer/pubby/`: `java -jar start.jar jetty.port=3031`.
* To test content negotiation, try `curl -L --header "Accept: text/turtle" http://IP_NUMBER:3031/mikel`. Some data should be returned.
* To test the web frotend go to `http://IP_NUMBER:3031/mikel` with the browser and the following should appear: