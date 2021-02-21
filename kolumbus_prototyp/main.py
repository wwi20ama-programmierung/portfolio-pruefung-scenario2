from pathlib import Path
from environment import Environment
from ship import Ship

def runMap(file):
  env = Environment(str(file))
  ship = Ship(env)
  ship.run()
  return len(env.getVisitedHarbors())

def main():
  
  # Liste mit den Dateinamen aller Karten anlegen:
  mapFileNames = ["karte1.txt"]
  mapDir = Path("karten")
  mapFiles = [mapDir / fileName for fileName in mapFileNames]
  
  results = list(map(runMap, mapFiles))
  
  print(results)

  return 0

main()