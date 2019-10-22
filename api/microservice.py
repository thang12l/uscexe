from bottle import request, response
from bottle import post, get, put, delete
import xml.etree.ElementTree as ET

_names = set()  # the set of names

@post('/saveRoute')
def saveRoute_handler():
    '''Handles for saveRoute query'''
    # Query string as /saveRoute?route=<xml object>
    # parsing the xml object
    tree = ET.parse(request.body)
    print(tree)
    root = tree.getroot()
    # Get the Route name
    routeName = root.get("route name")
    print("Route name:", routeName)
    # Extract the latitude and longitude coordinates
    for routeleg in root.findall("routeleg"):
        lat, long = routeleg.findall("lnglat").attrib
        # Adding new elements to xml object
        root.append("<lat>",lat,"</lat>")
        root.append("/lng>",long,"</lng>")

    # Store .xml file
    tree.write(routeName+".xml")
    pass


@get('/getRoute')
def getRoute_handler():
    '''Handles for getRoute query'''
    # Query string as /getRoute?route=<xml object>
    xmlobj = request.query.route
    pass

# Not use in this exe, just for future reference

@put('/names/<name>')
def update_handler(name):
    '''Handles name updates'''
    pass


@delete('/names/<name>')
def delete_handler(name):
    '''Handles name deletions'''
    pass
