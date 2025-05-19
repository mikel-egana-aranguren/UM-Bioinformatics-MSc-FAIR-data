# Procedure to publish FAIR Data

## Blazegraph and Trifid

Change the following parameter at `TrifidBlazegraph/docker-compose.yml`:

```yaml
DATASET_BASE_URL: "https://um.es/data/"
```

Blazegraph provides interfaces to both humans and agents to perform SPARQL queries. In `TrifidBlazegraph/blazegraph`, build image with `docker build -t="blazegraph" .`.

In `TrifidBlazegraph`, `docker-compose up -d`.

Go to http://localhost:9999; `NAMESPACES` tab; Create namespace `um` (mode `quads`); `use`.

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

Visit http://localhost:8081/LDD012546 to make sure it renders data, originating from the following query executed against Blazegraph (Trifid does the URI mapping):

```sparql
DESCRIBE <https://um.es/data/LDD012546>
```

To check content negotiation by an agent:

* `curl -L -H "Accept: text/turtle" http://localhost:8081/LDD012546`
* `curl -L -H "Accept: application/ld+json" http://localhost:8081/LDD012546`

Visit http://localhost:8081/UMGenesDataset to see the metadata (Related to the data with a Named Graph). Simulate to be an agent: `curl -H "Accept: application/ld+json" http://localhost:8081/UMGenesDataset`.

## Apache

Apache is used in this case to provide the original CSV file. The predicates for the discovery are `<http://localhost:8081/UMGenesDataset> dcat:distribution <https://um.es/data/csvgenes>` and then `<https://um.es/data/csvgenes> dcat:downloadURL <http://localhost/GenesUM.csv>`.

Restart Apache2 with (Or install if necessary with `sudo apt install apache2`): `service apache2 restart`.

Copy `GenesUM.csv` to `/var/www/html`: `sudo cp UM-Bioinformatics-MSc-FAIR-data/LinkedDataServer/data/GenesUM.csv /var/www/html/`.
