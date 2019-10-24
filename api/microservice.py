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
    # print(tree)
    root = tree.getroot()
    # Get the Route name
    route = root.find("route")
    routeName = route.get("name")
    #print("Route name:", routeName)
    # Extract the latitude and longitude coordinates
    for routeleg in route.findall("routeleg"):
        #print("in loop")
        latlong = routeleg.find("lnglat").text
        #print(latlong)
        temp1 = latlong.replace("(","")
        temp2 = temp1.replace(")","")
        lat, long = temp2.rsplit(", ")
        # Adding new elements to xml object
        #print("lat: ", lat, ", long: ", long)
        newlat = ET.SubElement(routeleg,"lat")
        newlat.text = lat
        newlong = ET.SubElement(routeleg,"lng")
        newlong.text = long
        routeleg.append(newlat)
        routeleg.append(newlong)

    # Store .xml file
    tree.write(routeName+".xml")
    pass


@get('/getRoute')
def getRoute_handler():
    '''Handles for getRoute query'''
    # Query string as /getRoute?route=<xml object>
    routeName = request.query.route
    #print(routeName)
    # Open the file in server
    with open(routName+".xml", 'r') as fileHandler:
        xml = fileHandler.readlines()

    response.status = 200 # Success
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
