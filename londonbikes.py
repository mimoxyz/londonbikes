#!/root/ansible-2-7-10/bin/python

import requests
import argparse
import sys

query_url = 'https://api.tfl.gov.uk/bikepoint'

# resp = requests.get(url=url)
# data = resp.json()
# print(data)

def usage():
  print("""Usage:
londonbikes search <search_string>
londonbikes search <latitude> <longitude> <radius_in_metres>
londonbikes id <bike_point_id>
""")

def search_by_id(bike_point_id):
    if bike_point_id:
      resp = requests.get(url=query_url+"/"+bike_point_id)
      data = resp.json()
      if resp.status_code == 404:
        print("Bike point id {0} not recognised".format(bike_point_id))
      elif resp.status_code == 200:
        print('{:30s}{:<20s}{:<20s}{:<20s}{:<20s}'.format("Name","Latitude","Longitude","Num Bikes","Empty Docks"))
        for p in data['additionalProperties']:
          if p['key'] == 'NbBikes':
            nbbike = p['value']
          if p['key'] == 'NbEmptyDocks':
            nbemptydocks = p['value']
        print('{:<30s}{:<20f}{:<20f}{:<20s}{:<20s}'.format(data['commonName'], data['lat'], data['lon'], nbbike, nbemptydocks ))
    else:
      print("Please specify a bike point id")
      sys.exit(12)

def search_by_name(search_string):
    if search_string:
      resp = requests.get(url=query_url+"/Search", params={'query':search_string})
      data = resp.json()
      if len(data) == 0:
        print("No bikepoints named {0} found".format(search_string))
      else:
        i = 0
        while i < len(data):
            if i == 0:
              print('{:<20s}{:<50s}{:<12s}{:<12s}'.format("Id","Name","Latitude","Longitude"))
            print('{:<20s}{:<50s}{:<12f}{:<12f}'.format(data[i]['id'], data[i]['commonName'], data[i]['lat'], data[i]['lon'] ))
            i += 1
    else:
      print("Please specify a search term")
      sys.exit(10)

def search_by_coordinates(latitude, longitude, radius_in_metres):
    resp = requests.get(url=query_url+"/Search?query="+search_string)
    data = resp.json()
    print(data)

def main():
  if len(sys.argv) <= 1 or len(sys.argv) > 5 or sys.argv[1] not in ('id', 'search'):
    usage()
  elif (sys.argv[1] in 'search'):
    if len(sys.argv) == 3:
      search_by_name(sys.argv[2])
    elif len(sys.argv) == 5:
      search_by_coordinates(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
      usage()
  elif (sys.argv[1] in 'id'):
    if len(sys.argv) == 3:
      search_by_id(sys.argv[2])
    else:
      usage()
  else:
    usage()

if __name__== "__main__":
  main()