# import pandas as pd
# import csv
# from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
# import networkx as nx
# import matplotlib.pyplot as plt
# import io
# import pydotplus
# from IPython.display import display, Image
# from rdflib.tools.rdf2dot import rdf2dot
from rdflib import Graph
import geocoder
import re


def geoid(ip):
    g = geocoder.geonames(ip, key='sashedher')
    ip_id = g.geonames_id
    print(ip_id)
    return ip_id


def load_geo_onto():
    g_aBox = Graph()
    g_aBox.parse("Dataset.ttl")
    g_aBox.parse("ontology_v3.2.rdf")
    return g_aBox


def OntoMatch1(strg) -> bool:
    Onto = re.compile(r"http://www.geonames.org/ontology")
    return Onto.match(strg) is not None


def OntoMatch2(strg) -> bool:
    Onto = re.compile(r"http://www.w3.org/2003/01/geo/wgs84_pos")
    return Onto.match(strg) is not None


def about_info(qry, grph):
    alternateName = "http://www.geonames.org/ontology#alternateName"
    officialName = "http://www.geonames.org/ontology#officialName"
    # postalCode="http://www.geonames.org/ontology#postalCode"
    namespace = "http://www.geonames.org/ontology#"
    coords = "http://www.w3.org/2003/01/geo/wgs84_pos#"
    i = 0
    result_r = grph.query(qry)
    about = dict()
    for subj, pred, obj in result_r:
        if str(pred) != alternateName and str(pred) != officialName:
            if OntoMatch1(str(pred)):
                i = i + 1
                x = str(pred)
                x = x.replace(namespace, '')
                # print("{:>20} {:>30} ".format(x,obj))
                about[x] = str(obj)
            if OntoMatch2(str(pred)):
                x = str(pred)
                x = x.replace(coords, '')
                # print("{:>20} {:>30} ".format(x,obj))
                about[x] = str(obj)

    return about


def cities_info(qry, grph):
    result_r = grph.query(qry)
    type(result_r)
    cities = dict()
    i = 0
    for s, p, o in result_r:
        i = i + 1
        # print(s, p, o)
        cities[str(p)] = str(o)

    return cities
