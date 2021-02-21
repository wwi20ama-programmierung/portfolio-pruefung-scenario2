class Ship:
  def __init__(self, env):
    self.env = env
  
  def run(self):
    # Beispiel: Fährt von der Startposition aus nach rechts,
    # bis ein Hafen gefunden ist und besucht diesen.
    while self.env.getShipSurroundings()[5][6] != 'H':
      self.env.printShipSurroundings()
      self.env.moveShipEast()
    self.env.visitHarbor(1,0)
    self.env.printShipSurroundings()