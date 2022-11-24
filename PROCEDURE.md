# Procedure to publish FAIR Data

## Blazegraph

Blazegraph provides interfaces to both humans and agents to perform SPARQL queries.

Start server at `LinkedDataServer/blazegraph`, execute `java -server -Xmx4g -jar blazegraph.jar` (Or `java -server -Xmx4g -Djetty.port=8181 -jar blazegraph.jar` to change the port).

Go to http://localhost:9999; `NAMESPACES` tab; Create namespace `um` (mode ``quads); `use`.

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

Check the service description of the SPARQL endpoint for agents by executing `curl` in another terminal: `curl http://localhost:9999/blazegraph/namespace/um/sparql`

## Trifid

Trifid provides interfaces to both humans and agents to explore RDF data and discover new data through predicates.

In another terminal, go to `LinkedDataServer/trifid` and execute `./server.js --config=../blazegraph-config.json`. Or, if you use Docker:  `docker run -p 3031:8080 -e "SPARQL_ENDPOINT_URL=http://dayhoff.inf.um.es:3030/blazegraph/namespace/um/sparql" -e "DATASET_BASE_URL=https://um.es/" ghcr.io/zazuko/trifid`

Visit http://localhost:8080/data/LDD012546 to make sure it renders data, originating from the following query exceuted against Blazegraph (Trifid does the URI mapping):

```sparql
DESCRIBE <https://um.es/data/LDD012546>
```

To check content negotiation by an agent:

* `curl -H "Accept: text/turtle" http://localhost:8080/data/LDD012546`
* `curl -H "Accept: application/ld+json" http://localhost:8080/data/LDD012546`

Visit http://localhost:8080/dataset/UMGenesDataset to see the metadata (Related to the data with a Named Graph). Simulate to be an agent: `curl -H "Accept: application/ld+json" http://localhost:8080/dataset/UMGenesDataset`.

## Apache

Apache is used in this case to provide the original CSV file. The predicate for the discovery is `dcat:distribution <http://localhost:8080/csv/genes>`.

Restart Apache2 with (Or install if necessary): `service apache2 restart`.

Add a symbolic link to actual CSV file from `www` directory to this repo:

* `cd /var/www/html`
* `ln -s LinkedDataServer/data/GenesUM.csv GenesUM.csv`
