from map import Map

class Environment:
  def __init__(self, filename):
    self.map = Map(filename)
    self.crashed = False
    self.visitedHarbors = []
    print(self.map)
  
  def getShipSurroundings(self):
    return self.map.getShipSurroundings(5)
  
  def printShipSurroundings(self):
    lines = [''.join(line) for line in self.getShipSurroundings()]
    print('\n'.join(lines))
  
  def moveShipNorth(self):
    self.crashed = self.crashed or not self.map.moveShip(0,-1)
    
  def moveShipSouth(self):
    self.crashed = self.crashed or not self.map.moveShip(0,1)

  def moveShipEast(self):
    self.crashed = self.crashed or not self.map.moveShip(1,0)

  def moveShipWest(self):
    self.crashed = self.crashed or not self.map.moveShip(-1,0)
  
  def visitHarbor(self, dx, dy):
    x,y = self.map.getShipPosition()
    hx = x + dx
    hy = y + dy
    if dx in [-1,0,1] and dy in [-1,0,1] and self.map.isHarbor(hx, hy):
      self.visitedHarbors += [(hx, hy)]
  
  def getVisitedHarbors(self):
    harbors = []
    for x,y in self.visitedHarbors:
      if (x,y) not in harbors:
        harbors += [(x,y)]
    return harbors