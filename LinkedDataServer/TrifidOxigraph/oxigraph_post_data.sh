#!/bin/sh

# ./oxigraph_post_data.sh ../data/MetadataGenes.ttl
# curl http://localhost:7878/store?um -H 'Content-Type: text/turtle' -T $1

# ./oxigraph_post_data.sh ../data/GenesUM.nq
curl http://localhost:7878/store?um -H 'Content-Type: text/n-quads' -T $1

