# Procedure to publish FAIR Data

## Apache

Install apache with `sudo apt install apache2`.

Copy `GenesUM.csv` to `/var/www/html`: `sudo cp UM-Bioinformatics-MSc-FAIR-data/LinkedDataServer/data/GenesUM.csv /var/www/html/`.

## Blazegraph

Blazegraph provides interfaces to both humans and agents to perform SPARQL queries.

Start server at `LinkedDataServer/blazegraph`, execute `java -server -Xmx4g -jar blazegraph.jar` (Or `java -server -Xmx4g -Djetty.port=8181 -jar blazegraph.jar` to change the port).

Go to http://IP:9999; `NAMESPACES` tab; Create namespace `um` (mode `quads`); `use`.

Go to `UPDATE` tab. Choose file `GenesUM.nq`, `Update`. Make sure the data has been uploaded with the following query:

```sparql
SELECT *
WHERE {
    GRAPH ?g {
        ?s ?p ?o
    }
}
```

Upload metadata (`MetadataGenes.ttl`) with the same procedure and check with the following query:

```sparql
SELECT *
WHERE {
    ?g ?r ?t
    GRAPH ?g {
        ?s ?p ?o
    }
}
```

Check the service description of the SPARQL endpoint for agents by executing `curl` in another terminal: `curl http://IP:9999/blazegraph/namespace/um/sparql`

## Pubby

Pubby provides interfaces to both humans and agents to explore RDF data and discover new data through predicates.

Configure Pubby by:

* Adding the IP of your server in "IP_NUMBER", in `fair-config.ttl`.
* Adding the value `fair-config.ttl` in file `pubby/webapps/ROOT/WEB-INF/web.xml`, in section `<context-param> <param-name>config-file</param-name>`.

Start Pubby at `LinkedDataServer/pubby/`: `java -jar start.jar jetty.port=3031`.

Visit http://IP:3031/LDD012546 to make sure it renders data, originating from the following query executed against Blazegraph (Pubby does the URI mapping):

```sparql
DESCRIBE <https://um.es/data/LDD012546>
```

To check content negotiation by an agent:

* `curl -L -H "Accept: text/turtle" http://IP:3031/LDD012546`
* `curl -L -H "Accept: application/ld+json" http://IP:3031/LDD012546`

Visit http://IP:3031/UMGenesDataset to see the metadata (Related to the data with a Named Graph). Simulate to be an agent: `curl -H "Accept: application/ld+json" http://IP:3031/UMGenesDataset`.

## Apache

Apache is used in this case to provide the original CSV file. The predicate for the discovery is `dcat:distribution <https://um.es/data/csvgenes>`.

Restart Apache2 with (Or install if necessary with `sudo apt install apache2`): `service apache2 restart`.

Copy `GenesUM.csv` to `/var/www/html`: `sudo cp UM-Bioinformatics-MSc-FAIR-data/LinkedDataServer/data/GenesUM.csv /var/www/html/`.
