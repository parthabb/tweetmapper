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
        self.cities = ["New York, N.Y.","Los Angeles, Calif.","Chicago, Ill.","Houston, Tex.","Philadelphia, Pa.","Phoenix, Ariz.",
                       "San Antonio, Tex.","San Diego, Calif.","Dallas, Tex.","San Jose, Calif.","Austin, Tex.","Jacksonville, Fla.",
                       "Indianapolis, Ind.","San Francisco, Calif.","Columbus, Ohio","Fort Worth, Tex.","Charlotte, N.C.","Detroit, Mich.",
                       "El Paso, Tex.","Memphis, Tenn.","Boston, Mass.","Seattle, Wash.","Denver, Colo.","Washington, DC","Nashville-Davidson, Tenn.",
                       "Baltimore, Md.","Louisville-Jefferson County, Ky.","Portland, Ore.","Oklahoma City, Okla.","Milwaukee, Wis.","Las Vegas, Nev.",
                       "Albuquerque, N.M.","Tucson, Ariz.","Fresno, Calif.","Sacramento, Calif.","Long Beach, Calif.","Kansas City, Mo.","Mesa, Ariz.",
                       "Virginia Beach, Va.","Atlanta, Ga.","Colorado Springs, Colo.","Raleigh, N.C.","Omaha, Nebr.","Miami, Fla.","Oakland, Calif.",
                       "Tulsa, Okla.","Minneapolis, Minn.","Cleveland, Ohio","Wichita, Kans.","Arlington, Tex."]
        