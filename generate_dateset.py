import os
import sys
import getopt
import json
import random
from pprint import pprint

def set_default_config():
    config = dict(
        num_records = 1
    )
    return(config)
    
def parse_args(argv):
    config = set_default_config()
    usage = 'usage: python ' + os.path.basename(__file__) + '-n <number of records to create>'
    try: opts, args = getopt.getopt(argv, "hn:",
                                    ["help",
                                     "numrecords"
                                     ])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print usage
            sys.exit(2)
        if opt in ("-n", "--numrecords"):
            config['num_records'] = arg
    return(config)

def createrecord():
    x1 = random.normalvariate(0,1)
    x2 = random.normalvariate(0,1)
    x3 = random.normalvariate(0,1)
    x4 = random.normalvariate(0,1)
    x5 = random.normalvariate(0,1)
    e = random.normalvariate(0,1)
    y1 = x1 + x2 + e
    y2 = x3 + x4 + e
    y3 = x1 + x5 + e
    record = dict(
        x1 = x1,
        x2 = x2,
        x3 = x3,
        x4 = x4,
        x5 = x5,
        y1 = y1,
        y2 = y2,
        y3 = y3
    )
    return(record)
        

def createtimeseries(config):
    random.seed()
    docs = []
    for i in range (0, int(config['num_records'])):
        docs.append(createrecord())
    return(dict(docs=docs))

def main(argv):
    config = parse_args(argv)
    timeseries = createtimeseries(config)
    print(json.dumps(timeseries))

if __name__=="__main__":
    main(sys.argv[1:])
