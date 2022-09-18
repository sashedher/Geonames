from rdflib import Graph

def load_loc_info(id):
    g_aBox = Graph()
    i=0
    url='https://www.geonames.org/'+str(id)+'/about.rdf'
    try:
        g_aBox.parse(url)
        # print("{}:  {}".format(i,url))
    except:
        print("This feature does not have about.rdf or invalid id")

    url = 'https://www.geonames.org/'+str(id)+'/nearby.rdf'
    try:
        g_aBox.parse(url)
        # print("{}:  {}".format(i,url))
    except:
        print("This feature does not have nearby.rdf or invalid id")


    url = 'https://www.geonames.org/'+str(id)+'/neighbours.rdf'
    try:
        g_aBox.parse(url)
        # print("{}:  {}".format(i,url))
    except:
        print("This feature does not have neighbour.rdf or invalid id")


    url = 'https://www.geonames.org/'+str(id)+'/contains.rdf'
    try:
        g_aBox.parse(url)
        # print("{}:  {}".format(i,url))
    except:
        print("This feature does not have contains.rdf or invalid id")
    
    return g_aBox

