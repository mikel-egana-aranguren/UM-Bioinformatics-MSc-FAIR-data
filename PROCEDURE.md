# Procedure

`java -server -Xmx4g -jar blazegraph.jar`
`java -server -Xmx4g -Djetty.port=8181 -jar blazegraph.jar`

Create Namespace `um` (quads!), `use`

Upload data (`GenesUM.nq`), Named Graph:

```sparql
SELECT *
WHERE {
    GRAPH ?g {?s ?p ?o}
}
```

Upload metadata (`MetadataGenes.ttl`):

```sparql
SELECT *
WHERE {
    {?g ?r ?t}
    GRAPH ?g {?s ?p ?o}
}
```

`curl http://localhost:9999/blazegraph/namespace/um/sparql`

`./server.js --config=../blazegraph-config.json`

<https://um.es/data/LDD012546>
<http://localhost:8080/data/LDD012546>

`curl -H "Accept: text/turtle" http://localhost:8080/data/LDD012546`

`curl -H "Accept: application/ld+json" http://localhost:8080/data/LDD012546`

<http://localhost:8080/dataset/UMGenesDataset>

`curl -H "Accept: application/ld+json" http://localhost:8080/dataset/UMGenesDataset`

dcat:distribution <http://localhost:8080/csv/genes>

`service apache2 restart`

`cd /var/www/html`

`ln -s /home/mikel/EHU-LSI/Docencia/2021-2022/MSc-UM/MSc-UM-2021-2022-FAIR/LinkedDataServer/data/GenesUM.csv GenesUM.csv`
