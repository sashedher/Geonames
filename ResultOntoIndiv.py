from rdflib import Graph

def load_loc_info(id,type):
    g_aBox = Graph()

    url='https://www.geonames.org/'+str(id)+'/'+type+'.rdf'
    try:
        g_aBox.parse(url)
        # print("{}:  {}".format(i,url))
    except:
        print("This feature does not have this type of rdf file or invalid id")

    return g_aBox

