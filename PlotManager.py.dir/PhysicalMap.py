import Manager

mapCentre = (0, 100, 0)

ON  = 152 # Block to place when claimed/reserved
OFF = 1   # Block to place when free

# Transform plot coords to map coords (Offset from map's centre)
def getMapCoords(x, z):
    newX = x * 3
    newZ = z * 3

    if x < 0:
        newX -= 1
    else:
        newX += 1

    if z < 0:
        newZ -= 1
    else:
        newZ += 1

    return (newX + mapCentre[0] + 2, newZ + mapCentre[2] + 2)

# Transform map coords to plot coords
def getPlotCoords(x, z):
    newX = x - mapCentre[0]
    newZ = z - mapCentre[2]

    if newX > 0:
        newX -= 2

    if newZ > 0:
        newZ -= 2

    return (newX // 3, newZ // 3)

# Mark a plot as claimed/reserved
def claim(x, z):
    position = getMapCoords(x, z)

    world.getBlockAt(position[0], mapCentre[1], position[1]).setTypeId(ON)
    world.getBlockAt(position[0] - 1, mapCentre[1], position[1]).setTypeId(ON)
    world.getBlockAt(position[0], mapCentre[1], position[1] - 1).setTypeId(ON)
    world.getBlockAt(position[0] - 1, mapCentre[1], position[1] - 1).setTypeId(ON)

# Mark a plot as free
def unclaim(x, z):
    position = getMapCoords(x, z)

    world.getBlockAt(position[0], mapCentre[1], position[1]).setTypeId(OFF)
    world.getBlockAt(position[0] - 1, mapCentre[1], position[1]).setTypeId(OFF)
    world.getBlockAt(position[0], mapCentre[1], position[1] - 1).setTypeId(OFF)
    world.getBlockAt(position[0] - 1, mapCentre[1], position[1] - 1).setTypeId(OFF)

@hook.command("plotmap")
def onCommandPlotmap(sender, args):
    if len(args) == 0:
        showHelp(sender)

        return True

    cmd = args[0]

    plotCoords = getPlotCoords(int(sender.getLocation().getX()), int(sender.getLocation().getZ()))

    if Manager.isOutOfRange(plotCoords[0], plotCoords[1]):
        sender.sendMessage("Out of range")

        return True

    if cmd == "claim":
        if Manager.claim(sender.getName(), plotCoords[0], plotCoords[1]):
            sender.sendMessage(''.join(["You successfully claimed plot ", str(plotCoords[0]), ", ", str(plotCoords[1])]))
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), ". Make sure that this is a free plot and that you are allowed to claim plots"]))

        return True

    elif cmd == "unclaim":
        if Manager.unclaim(sender.getName(), plotCoords[0], plotCoords[1]):
            sender.sendMessage(''.join(["You successfully unclaimed plot ", str(plotCoords[0]), ", ", str(plotCoords[1])]))
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), ". Make sure that you are the owner of this plot"]))

        return True

    elif cmd == "info":
        plot = Manager.getPlot(plotCoords[0], plotCoords[1])

        sender.sendMessage(''.join(["--- Plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), " ---"]))

        if plot.status == Manager.PlotStatus.FREE:
            sender.sendMessage("Status: Free")

        elif plot.status == Manager.PlotStatus.CLAIMED:
            sender.sendMessage(''.join(["Status: Claimed by ", plot.owner]))
            sender.sendMessage(''.join(["Claimed at: ", plot.date]))

        elif plot.status == Manager.PlotStatus.TEMP:
            sender.sendMessage(''.join(["Status: Temporarily claimed by ", plot.owner]))
            sender.sendMessage(''.join(["Claimed at: ", plot.date]))

        elif plot.status == Manager.PlotStatus.RESERVED:
            sender.sendMessage("Status: Reserved")

        elif plot.status == Manager.PlotStatus.SPECIAL:
            sender.sendMessage(''.join(["Status: ", plot.description]))

        return True

    elif cmd == "tp":
        loc = sender.getLocation()

        x = Manager.getCentreX(plotCoords[0])
        z = Manager.getCentreZ(plotCoords[1])

        loc.setX(x)
        loc.setZ(z)

        sender.teleport(loc)

        return True

    elif cmd == "generate":
        if not sender.hasPermission("plotmanager.generate"):
            sender.sendMessage("You don't have enough permissions to execute this command")
            return True

        for x in xrange(-Manager.radius, Manager.radius):
            for z in xrange(-Manager.radius, Manager.radius):
                unclaim(x, z)

        return True

    elif cmd == "update":
        if not sender.hasPermission("plotmanager.generate"):
            sender.sendMessage("You don't have enough permissions to execute this command")
            return True

        for pos, plot in Manager.plots.iteritems():
            position = getMapCoords(pos[0], pos[1])

            if plot.status == Manager.PlotStatus.FREE:
                unclaim(pos[0], pos[1])
            else:
                claim(pos[0], pos[1])

    elif cmd == "reserve":
        if not sender.hasPermission("plotmanager.reserve"):
            sender.sendMessage("You don't have enough permissions to execute this command")
            return True

        if Manager.reserve(plotCoords[0], plotCoords[1]):
            sender.sendMessage(''.join(["You successfully reserved plot ", str(plotCoords[0]), ", ", str(plotCoords[1])]))
        else:
            sender.sendMessage(''.join(["Failed to reserve plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), ". Make sure that this is a free plot"]))

        return True

    elif cmd == "special":
        if not sender.hasPermission("plotmanager.reserve"):
            sender.sendMessage("You don't have enough permissions to execute this command")
            return True

        del args[0]

        if Manager.special(plotCoords[0], plotCoords[1], ' '.join(args)):
            sender.sendMessage(''.join(["You successfully reserved plot ", str(plotCoords[0]), ", ", str(plotCoords[1])]))
        else:
            sender.sendMessage(''.join(["Failed to reserve plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), ". Make sure that this is a free plot"]))

        return True

    elif cmd == "forceUnclaim":
        if not sender.hasPermission("plotmanager.admin"):
            sender.sendMessage("You don't have enough permissions to execute this command")
            return True

        Manager.forceUnclaim(plotCoords[0], plotCoords[1])

        return True

    return True

def showHelp(sender):
    sender.sendMessage("--- Plot Manager /plotmap Help ---")
    sender.sendMessage("/plotmap claim")
    sender.sendMessage("/plotmap unclaim")
    sender.sendMessage("/plotmap info")
    sender.sendMessage("/plotmap tp")
    sender.sendMessage("--- Admin commands ---")
    sender.sendMessage("/plotmap generate")
    sender.sendMessage("/plotmap update")
    sender.sendMessage("/plotmap reserve")
    sender.sendMessage("/plotmap special <description>")
    sender.sendMessage("/plotmap forceUnclaim")
