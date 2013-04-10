from collections import defaultdict

import time.ctime as ctime

from math import floor

import pickle

# Plot size

plotx = 256
plotz = 256

# Structures

class PlotStatus:
    FREE     = 0
    
    CLAIMED  = 1
    TEMP     = 2

    RESERVED = 3
    SPECIAL  = 4

class Plot:
    def __init__(self, status = PlotStatus.FREE):
        self.status = status

    def claim(self, ownerName):
        self.status = PlotStatus.CLAIMED
        self.owner  = ownerName
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

    plot.claim(name)

    return True

def forceClaim(name, x, z):
    position = (x, z)

    plots[position].claim(name)

# Unclaim

def unclaim(name, x, z):
    position = (x, z)

    plot = plots[position]

    if plot.status != PlotStatus.CLAIMED or plot.owner != name:
        return False
    
    plot.status = PlotStatus.FREE

def forceUnclaim(x, z):
    position = (x, z)

    plots[position].status = PlotStatus.FREE

def getPlot(x, z):
    return plots[(x, z)]

# Coordinate transform

def getPlotX(x):
    return int(floor(x / plotx))

def getPlotZ(z):
    return int(floor(z / plotz))

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
