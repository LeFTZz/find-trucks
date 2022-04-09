from multiprocessing.dummy import Array
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import json
from model import TrucksRequest

class Trucks:
  def __init__(self):
    self._trucks = pd.read_csv('../Mobile_Food_Facility_Permit.csv')
    self.processTrucks()
  
  def removeInvalidData(self):
    self._trucks = self._trucks[self._trucks['Status']=='APPROVED']
    self._trucks = self._trucks[(self._trucks['Latitude']!=0) | (self._trucks['Longitude']!=0)]
  
  def processTrucks(self):
    self.removeInvalidData()
    self._trucks = gpd.GeoDataFrame(self._trucks, geometry=gpd.points_from_xy(self._trucks['Longitude'], self._trucks['Latitude']))

  def getNearestTrucks(self, dto: TrucksRequest):
    self._trucks['distance'] = self._trucks['geometry'].distance(Point(dto['latitude'], dto['longitude']))
    raw_result = self._trucks.sort_values('distance', ascending=True).head(dto['count'])
    return self.parsedResult(raw_result)
  
  def parsedResult(self, raw_result)-> Array:
    result = raw_result.to_json()
    parsed = json.loads(result)
    return parsed['features']