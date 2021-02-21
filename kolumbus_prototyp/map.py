class Map:
  symbols = {
    'water': ' ',
    'harbor': 'H',
    'land': '#',
    'ship': 'S' 
  }

  def __init__(self, fileName):
    with open(fileName, 'r') as file:
      self.tiles = [list(line.strip()) for line in file.readlines()]
  
  def isWater(self, x, y):
    return self.isValidPosition(x,y) and self.tiles[y][x] == Map.symbols['water']
  
  def isHarbor(self, x, y):
    return self.isValidPosition(x,y) and self.tiles[y][x] == Map.symbols['harbor']
  
  def isLand(self, x, y):
    return self.isValidPosition(x,y) and self.tiles[y][x] == Map.symbols['land']

  def isShip(self, x, y):
    return self.isValidPosition(x,y) and self.tiles[y][x] == Map.symbols['ship']
  
  def isValidPosition(self, x, y):
    if y < 0 or y >= len(self.tiles):
      return False
    return x >= 0 and x < len(self.tiles[y])

  def getShipPosition(self):
    for y in range(len(self.tiles)):
      for x in range(len(self.tiles[y])):
        if self.isShip(x,y):
          return x,y
    return -1,-1

  def getSurroundings(self, x, y, radius):
    minx = max(0, x-radius);
    maxx = min(len(self.tiles[0]), x + radius)
    miny = max(0, y-radius);
    maxy = min(len(self.tiles[0]), y + radius)
    return [line[minx : maxx+1] for line in self.tiles[miny : maxy+1]]
  
  def getShipSurroundings(self, radius):
    x,y = self.getShipPosition()
    return self.getSurroundings(x,y,radius)
  
  def canMoveShip(self, dx, dy):
    x,y = self.getShipPosition()
    return dx in [-1,0,1] and dy in [-1,0,1] and self.isWater(x+dx, y+dy)
  
  def moveShip(self, dx, dy):
    if not self.canMoveShip(dx, dy):
      return False
    x,y = self.getShipPosition()
    self.tiles[y][x] = Map.symbols['water']
    self.tiles[y+dy][x+dx] = Map.symbols['ship']
    return True


  def __str__(self):
    lines = [''.join(line) for line in self.tiles]
    return '\n'.join(lines)

