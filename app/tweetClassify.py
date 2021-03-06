'''
Created on Apr 15, 2014

@author, spoyler
'''

import json
import cjson
from collections import OrderedDict


'''Cities in order of their rank with geocode and WOEID'''
cities = (("New York, N.Y.", 2459115 ,(-73.95, 40.67)),
          ("Los Angeles, Calif.", 2442047, (-118.25, 34.05)),
          ("Chicago, Ill.",2379574,(-87.63,41.88)),
          ("Houston, Tex.",12590119,(-95.37,29.76)),
          ("Philadelphia, Pa.",2471217,(-75.16,39.95)),
          ("Phoenix, Ariz.",2471390,(-112.08,33.45)),
          ("San Antonio, Tex.",2487796,(-98.52,29.46)),
          ("San Diego, Calif.",2487889,(-117.16,32.72)),
          ("Dallas, Tex.",2388929,(-96.8,32.78)),
          ("San Jose, Calif.",2488042,(-121.84,37.3)),
          ("Austin, Tex.",2357536,(-97.74,30.27)),
          ("Jacksonville, Fla.",2428344,(-81.66,30.33)),
          ("Indianapolis, Ind.",2427032,(-86.15,39.77)),
          ("San Francisco, Calif.",2487956,(-122.44,37.75)),
          ("Columbus, Ohio",2383660,(-83,39.96)),
          ("Fort Worth, Tex.",2406080,(-97.35,32.78)),
          ("Charlotte, N.C.",2378426,(-80.84,35.22)),
          ("Detroit, Mich.",2391585,(-83.05,42.33)),
          ("El Paso, Tex.",2397816,(-106.49,31.76)),
          ("Memphis, Tenn.",2449323,(-90.05,35.15)),
          ("Boston, Mass.",2367105,(-71.06,42.36)),
          ("Seattle, Wash.",2490383,(-122.33,47.6)),
          ("Denver, Colo.",2391279,(-104.99,39.74)),
          ("Washington, DC",2514815,(-77.03,38.9)),
          ("Nashville-Davidson, Tenn.",2457170,(-86.78,36.17)),
          ("Baltimore, Md.",2358820,(-76.61,39.29)),
          ("Louisville-Jefferson County, Ky.",2442327,(-76.61,39.29)),
          ("Portland, Ore.",2475687,(-122.68,45.51)),
          ("Oklahoma City, Okla.",2347595,(-98.52,35.31)),
          ("Milwaukee, Wis.",2451822,(-87.91,43.04)),
          ("Las Vegas, Nev.",2436704,(-115.14,36.17)),
          ("Albuquerque, N.M.",2352824,(-106.65,35.08)),
          ("Tucson, Ariz.",2508428,(-110.97,32.22)),
          ("Fresno, Calif.",2407517,(-119.79,36.74)),
          ("Sacramento, Calif.",2486340,(-121.49,38.58)),
          ("Long Beach, Calif.",2441472,(-118.17,33.8)),
          ("Kansas City, Mo.",2430683,(-94.58,39.1)),
          ("Mesa, Ariz.",2449808,(-94.58,39.1)),
          ("Virginia Beach, Va.",2512636,(-76.05,36.77)),
          ("Atlanta, Ga.",2357024,(-84.39,33.75)),
          ("Colorado Springs, Colo.",2383489,(-104.76,38.87)),
          ("Raleigh, N.C.",2478307,(-78.64,35.79)),
          ("Omaha, Nebr.",2465512,(-95.94,41.26)),
          ("Miami, Fla.",2450022,(-80.24,25.73)),
          ("Oakland, Calif.",2463583,(-122.27,37.81)),
          ("Tulsa, Okla.",2508533,(-95.99,36.15)),
          ("Minneapolis, Minn.",2452078,(-93.26,44.98)),
          ("Cleveland, Ohio",2381475,(-81.69,41.5)),
          ("Wichita, Kans.",2520077,(-97.34,37.69)),
          ("Arlington, Tex.",2355944,(-97.11,32.74))
)


'''Processing scores to get an ordered file with the mapping to cities'''
def processforUI():
    UI = {}
    f = open("result.json","r")
    result = cjson.decode(f.read())
    for line in result:
        print result[line]
        UI[line] = {}
        UI[line]["tfidf"] = {}
        for predcity in result[line]["tfidf"]:
             print predcity
             #print  cities[predcity[0]]
             UI[line]["tfidf"][predcity[0]] = {}
             UI[line]["tfidf"][predcity[0]]["geolocation"] = cities[predcity[0]]
             UI[line]["tfidf"][predcity[0]]["score"] = predcity[1]
        UI[line]["tfidf"] = OrderedDict(sorted(UI[line]['tfidf'].iteritems(),
                  key=lambda x: x[1]['score'],
                  reverse=True
                 ))
        UI[line]["PureVal"] = {}
        for actualCity in result[line]["PureVal"]:
             print actualCity
             #print  cities[int(actualCity[0])]
             UI[line]["PureVal"][actualCity[0]] = {}
             UI[line]["PureVal"][actualCity[0]]["geolocation"] = cities[int(actualCity[0])]
             UI[line]["PureVal"][actualCity[0]]["hits"] = [actualCity[1]]
        UI[line]["PureVal"] = OrderedDict(sorted(UI[line]['PureVal'].iteritems(),
                  key=lambda x: x[1]['hits'],
                  reverse=True
                 ))
    f.close()
    f = open("UIResults.json","w")
    f.write(json.dumps(UI))
    f.close()
if __name__ == '__main__':
  #test_get_all_file_names()
  processforUI()
