"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach
import datetime

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.
    
    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    NearEarthObjects = [] #Creates a list to append the rows pulled from the CSV file
    # TODO: Load NEO data from the given CSV file.
    with open('tests/test-neos-2020.csv', 'r') as infile:
        reader = csv.reader(infile)
        next(reader) #eliminates the header section
        for row in reader:
            neo = NearEarthObject()
            neo.designation = str(row[3]) #Pulls the designation       
            if str(row[4]) == '':
                neo.name = None #Pulls the name
            else:
                neo.name = str(row[4])
            if row[15] == '':
                neo.diameter = float('nan')
            else:
                neo.diameter = float(row[15]) #Pulls the diameter of the object
            if str(row[7]) == 'Y':
                neo.hazardous = True #Pulls if the NEO is designated as dangerous or not
            elif str(row[7]) == 'N':
                neo.hazardous = False
            else:
                neo.hazardous = ''
            NearEarthObjects.append(neo)
    
    return NearEarthObjects

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    CloseApproaches = []
    with open('tests/test-cad-2020.json', 'r') as infile:
        contents = json.load(infile)
        fieldslist = contents["data"]
        for field in range(len(fieldslist)):
            ca = CloseApproach()
            ca.designation = str(fieldslist[field][0]) #pulls the designation of the iterated field
            ca.time = fieldslist[field][3] #Pulls the time of the iterated field   
           
            ca.distance = float(fieldslist[field][4]) #Pulls the distance of the iterated field
            ca.velocity = float(fieldslist[field][7]) #Pulls the velocity of the iterated field
            CloseApproaches.append(ca)
        
    return CloseApproaches

csv_file = load_neos('tests/test-neos-2020.csv')
json_file = load_approaches('tests/test-cad-2020.json')