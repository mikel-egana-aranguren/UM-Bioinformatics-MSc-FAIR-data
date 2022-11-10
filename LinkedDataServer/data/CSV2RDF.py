#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################
# https://github.com/SemanticLab/simple-csv-to-rdf
# pip install rdflib
##################################################

import csv
from rdflib import Graph, Literal, Namespace, URIRef

# Importar vocabularios (Muy util)
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD, DC, DCTERMS, VOID

# Abrir archivo CSV
input_file = csv.DictReader(open("GenesUM.csv"))

# Crear un objeto Grafo 
output_graph = Graph()

# URIs base comunes (FAIR: crear URIs como identificadores)
base_uri = 'https://um.es/data/'

# Objetos comunes (FAIR: reusar vocabularios y recursos)
taxon_human = 'http://purl.uniprot.org/taxonomy/9606'
sio_gene = 'http://semanticscience.org/resource/SIO_010035'

# Propiedades comunes (FAIR: reusar vocabularios)

# UniProt Organism
up_organism = 'http://purl.uniprot.org/core/organism' 

# SIO has_unique_identifier (https://lov.linkeddata.es/dataset/lov/vocabs/sio)
sio_has_unique_identifier = 'http://semanticscience.org/resource/SIO_000673'

# Recorrer cada linea y convertir a triples RDF
# (FAIR: normalizar los nombres de las columnas a predicados RDF con URI como SIO o UP)

for row in input_file:

	# Recoger los datos de la linea CSV

	# URI sujeto: baseURI + columna Id
	gen_uri = base_uri + row['Id']

	# Columna Nombre
	nombre = row['Nombre']

	# Columna taxon (FAIR: "Tx" nadie sabe lo que es! Lo normalizamos a una URI UniProt mediante el predicado up_organism)
	taxon = row['Tx']

	# Crear los triples

	# Normalizar los datos
	if nombre != '':
		# gen->rdfs:label->nombre
		output_graph.add( (URIRef(gen_uri), RDFS.label, Literal(nombre, lang='en')) )
		
		# gen->sio:has_unique_identifier->nombre
		output_graph.add( (URIRef(gen_uri), URIRef(sio_has_unique_identifier), Literal(nombre, datatype=XSD.string)) )

	# Normalizar los datos
	# gen->up:organism->taxon_human
	if taxon != 'Alien': 
		# gen->up_organism->taxon_human (FAIR: Estamos creando un enlace Linked Data, usando taxon_human)
		output_graph.add((URIRef(gen_uri), URIRef(up_organism), URIRef(taxon_human)) )

	# gen->rdf:type->sio_gene	
	output_graph.add( (URIRef(gen_uri), RDF.type, URIRef(sio_gene)) )

output_graph.serialize(destination='GenesUM.nt', format='nt')


