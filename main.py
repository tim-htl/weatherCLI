import argparse
import server
    
parser = argparse.ArgumentParser()
parser.add_argument("city")
args = parser.parse_args()

server.getTemperature(args.city)

