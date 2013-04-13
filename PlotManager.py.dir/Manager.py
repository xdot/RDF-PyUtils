from collections import defaultdict

import time.ctime as ctime

from math import floor

import pickle

import PhysicalMap

# Ops

ops = []

def initOps(path):
    f = open(path, "rb")

    for line in f.xreadlines():
        ops.append(line.replace('\n', ''))

# Plot size

plotx = 256
plotz = 256

# Plots

radius = 5

# Structures

class PlotStatus:
    FREE     = 0
    
    CLAIMED  = 1
    TEMP     = 2

    RESERVED = 3

class Plot:
    def __init__(self, status = PlotStatus.FREE):
        self.status = status

    def claim(self, ownerName):
        self.status = PlotStatus.CLAIMED
        self.owner  = ownerName
        self.date   = ctime()

    def reserve(self):
        self.status = PlotStatus.RESERVED
        self.date   = ctime()

class Player:
    def __init__(self, numPlots = 1):
        self.numPlots = numPlots

plots = defaultdict(Plot)
players = defaultdict(Player)

# Claim

def claim(name, x, z):
    position = (x, z)

    plot = plots[position]

    if plot.status != PlotStatus.FREE:
        return False

    if players[name].numPlots == 0:
        return False

    players[name].numPlots -= 1

    plot.claim(name)

    PhysicalMap.claim(x, z)

    return True

def forceClaim(name, x, z):
    position = (x, z)

    plots[position].claim(name)

    PhysicalMap.claim(x, z)

def reserve(x, z):
    position = (x, z)

    plot = plots[position]

    if plot.status != PlotStatus.FREE:
        return False

    plot.reserve()

    PhysicalMap.claim(x, z)

    return True

# Unclaim

def unclaim(name, x, z):
    position = (x, z)

    plot = plots[position]

    if (plot.status != PlotStatus.CLAIMED and plot.status != PlotStatus.TEMP) or plot.owner != name:
        return False

    players[name].numPlots += 1
    
    plot.status = PlotStatus.FREE

    PhysicalMap.unclaim(x, z)

def forceUnclaim(x, z):
    position = (x, z)

    plot = plots[position]

    if plot.status == PlotStatus.CLAIMED and plot.owner in players:
        players[plot.owner].numPlots += 1

    plot.status = PlotStatus.FREE

    PhysicalMap.unclaim(x, z)

# Getters

def getPlot(x, z):
    return plots[(x, z)]

def getPlayer(name):
    return players[name]

# Coordinate transform

def getPlotX(x):
    return int(x // plotx)

def getPlotZ(z):
    return int(z // plotz)

def getCentreX(x):
    return (x * plotx) + (plotx / 2)

def getCentreZ(z):
    return (z * plotz) + (plotz / 2)

# Persistence

def save(directory):
    pickle.dump(plots, open(directory + "/PMplots.txt", "wb"))
    pickle.dump(players, open(directory + "/PMplayers.txt", "wb"))

def load(directory):
    try:
        plots = pickle.load(open(directory + "/PMplots.txt", "rb"))
        players = pickle.load(open(directory + "/PMplayers.txt", "rb"))

    except IOError, EOFError:
        print "Plot data is missing, creating new files"

        save(directory)
