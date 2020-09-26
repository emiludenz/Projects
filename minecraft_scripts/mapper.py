import os
import csv
class Coordinates:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z


class Map:
  def __init__(self,seed):
    self.seed = seed
    self.name = None
    self.bases = list()
    self.home_base = None
    self.outposts = list()
    self.coordinates = None

  def set_name(self,name):
    self.name = name
  
  def set_coordiantes(self,x,y,z):
    self.coordinates = Coordinates(x,y,z)
  
  def save(self):
    file_name = ""
    if self.name == None:
      file_name = self.name
    else:
      file_name = self.seed
    file_name += ".csv"
    with open(file_name) as csvfile:
      reader = csv.reader(csvfile,delimiter="")

  def load(self):
    pass
  
  
