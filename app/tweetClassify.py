'''
Created on Apr 15, 2014

@author: spoyler
'''
from library import TweepyAPIs
import time

class TweetClassify(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.cities = {"New York, N.Y.":{"WOEID":2459115,"GeoLocation":{"Lon":-73.95,"Lat":40.67}},"Los Angeles, Calif.":{"WOEID":2442047,"GeoLocation":{"Lon":-118.25,"Lat":34.05}},"Chicago, Ill.":{"WOEID":2379574,"GeoLocation":{"Lon":-87.63,"Lat":41.88}},"Houston, Tex.":{"WOEID":12590119,"GeoLocation":{"Lon":-95.37,"Lat":29.76}},"Philadelphia, Pa.":{"WOEID":2471217,"GeoLocation":{"Lon":-75.16,"Lat":39.95}},"Phoenix, Ariz.":{"WOEID":2471390,"GeoLocation":{"Lon":-112.08,"Lat":33.45}},
                       "San Antonio, Tex.":{"WOEID":2487796,"GeoLocation":{"Lon":-98.52,"Lat":29.46}},"San Diego, Calif.":{"WOEID":2487889,"GeoLocation":{"Lon":-117.16,"Lat":32.72}},"Dallas, Tex.":{"WOEID":2388929,"GeoLocation":{"Lon":-96.8,"Lat":32.78}},"San Jose, Calif.":{"WOEID":2488042,"GeoLocation":{"Lon":-121.84,"Lat":37.3}},"Austin, Tex.":{"WOEID":2357536,"GeoLocation":{"Lon":-97.74,"Lat":30.27}},"Jacksonville, Fla.":{"WOEID":2428344,"GeoLocation":{"Lon":-81.66,"Lat":30.33}},
                       "Indianapolis, Ind.":{"WOEID":2427032,"GeoLocation":{"Lon":-86.15,"Lat":39.77}},"San Francisco, Calif.":{"WOEID":2487956,"GeoLocation":{"Lon": -122.44,"Lat":37.75}},"Columbus, Ohio":{"WOEID":2383660,"GeoLocation":{"Lon":-83,"Lat":39.96}},"Fort Worth, Tex.":{"WOEID":2406080,"GeoLocation":{"Lon":-97.35,"Lat":32.78}},"Charlotte, N.C.":{"WOEID":2378426,"GeoLocation":{"Lon":-80.84,"Lat":35.22}},"Detroit, Mich.":{"WOEID":2391585,"GeoLocation":{"Lon":-83.05,"Lat":42.33}},
                       "El Paso, Tex.":{"WOEID":2397816,"GeoLocation":{"Lon":-106.49,"Lat":31.76}},"Memphis, Tenn.":{"WOEID":2449323,"GeoLocation":{"Lon":-90.05,"Lat":35.15}},"Boston, Mass.":{"WOEID":2367105,"GeoLocation":{"Lon":-71.06,"Lat":42.36}},"Seattle, Wash.":{"WOEID":2490383,"GeoLocation":{"Lon": -122.33,"Lat":47.6}},"Denver, Colo.":{"WOEID":2391279,"GeoLocation":{"Lon":-104.99,"Lat":39.74}},"Washington, DC":{"WOEID":2514815,"GeoLocation":{"Lon":-77.03,"Lat":38.9}},"Nashville-Davidson, Tenn.":{"WOEID":2457170,"GeoLocation":{"Lon":-86.78,"Lat":36.17}},
                       "Baltimore, Md.":{"WOEID":2358820,"GeoLocation":{"Lon":-76.61,"Lat":39.29}},"Louisville-Jefferson County, Ky.":{"WOEID":2442327,"GeoLocation":{"Lon":-76.61,"Lat":39.29}},"Portland, Ore.":{"WOEID":2475687,"GeoLocation":{"Lon":-122.68,"Lat":45.51}},"Oklahoma City, Okla.":{"WOEID":2347595,"GeoLocation":{"Lon":-98.52,"Lat":35.31}},"Milwaukee, Wis.":{"WOEID":2451822,"GeoLocation":{"Lon":-87.91,"Lat":43.04}},"Las Vegas, Nev.":{"WOEID":2436704,"GeoLocation":{"Lon":-115.14,"Lat":36.17}},
                       "Albuquerque, N.M.":{"WOEID":2352824,"GeoLocation":{"Lon":-106.65,"Lat":35.08}},"Tucson, Ariz.":{"WOEID":2508428,"GeoLocation":{"Lon":-110.97,"Lat":32.22}},"Fresno, Calif.":{"WOEID":2407517,"GeoLocation":{"Lon":-119.79,"Lat":36.74}},"Sacramento, Calif.":{"WOEID":2486340,"GeoLocation":{"Lon":-121.49,"Lat":38.58}},"Long Beach, Calif.":{"WOEID":2441472,"GeoLocation":{"Lon":-118.17,"Lat":33.8}},"Kansas City, Mo.":{"WOEID":2430683,"GeoLocation":{"Lon":-94.58,"Lat":39.1}},"Mesa, Ariz.":{"WOEID":2449808,"GeoLocation":{"Lon":-94.58,"Lat":39.1}},
                       "Virginia Beach, Va.":{"WOEID":2512636,"GeoLocation":{"Lon":-76.05,"Lat":36.77}},"Atlanta, Ga.":{"WOEID":2357024,"GeoLocation":{"Lon":-84.39,"Lat":33.75}},"Colorado Springs, Colo.":{"WOEID":2383489,"GeoLocation":{"Lon":-104.76,"Lat":38.87}},"Raleigh, N.C.":{"WOEID":2478307,"GeoLocation":{"Lon":-78.64,"Lat":35.79}},"Omaha, Nebr.":{"WOEID":2465512,"GeoLocation":{"Lon":-95.94,"Lat":41.26}},"Miami, Fla.":{"WOEID":2450022,"GeoLocation":{"Lon":-80.24,"Lat":25.73}},"Oakland, Calif.":{"WOEID":2463583,"GeoLocation":{"Lon":-122.27,"Lat":37.81}},
                       "Tulsa, Okla.":{"WOEID":2508533,"GeoLocation":{"Lon":-95.99,"Lat":36.15}},"Minneapolis, Minn.":{"WOEID":2452078,"GeoLocation":{"Lon":-93.26,"Lat":44.98}},"Cleveland, Ohio":{"WOEID":2381475,"GeoLocation":{"Lon":-81.69,"Lat":41.5}},"Wichita, Kans.":{"WOEID":2520077,"GeoLocation":{"Lon":-97.34,"Lat":37.69}},"Arlington, Tex.":{"WOEID":2355944,"GeoLocation":{"Lon":-97.11,"Lat":32.74}}}
        