import Manager

mapCentre = (0, 100, 0)

ON  = 152
OFF = 1

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

    return (newX + mapCentre[0] + 2, newZ + mapCentre[1] + 2)

def getPlotCoords(x, z):
    newX = x - mapCentre[0]
    newZ = z - mapCentre[1]

    if newX > 0:
        newX -= 2

    if newZ > 0:
        newZ -= 2

    return (newX // 3, newZ // 3)

def claim(world, x, z):
    position = getMapCoords(x, z)

    world.getBlockAt(position[0], mapCentre[1], position[1]).setTypeId(ON)
    world.getBlockAt(position[0] - 1, mapCentre[1], position[1]).setTypeId(ON)
    world.getBlockAt(position[0], mapCentre[1], position[1] - 1).setTypeId(ON)
    world.getBlockAt(position[0] - 1, mapCentre[1], position[1] - 1).setTypeId(ON)

def unclaim(world, x, z):
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

    global world

    world = sender.getLocation().getWorld()

    cmd = args[0]

    plotCoords = getPlotCoords(int(sender.getLocation().getX()), int(sender.getLocation().getZ()))

    if cmd == "claim":
        if len(args) != 1:
            showHelp(sender)

            return True

        if Manager.claim(sender.getName(), plotCoords[0], plotCoords[1]):
            sender.sendMessage(''.join(["You successfully claimed plot ", str(plotCoords[0]), ", ", str(plotCoords[1])]))
            claim(sender.getLocation().getWorld(), plotCoords[0], plotCoords[1])
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), ". Make sure that this is a free plot and that you are allowed to claim plots"]))

        return True

    elif cmd == "unclaim":
        if len(args) != 1:
            showHelp(sender)

            return True

        if Manager.unclaim(sender.getName(), plotCoords[0], plotCoords[1]):
            sender.sendMessage(''.join(["You successfully unclaimed plot ", str(plotCoords[0]), ", ", str(plotCoords[1])]))
            unclaim(sender.getLocation().getWorld(), plotCoords[0], plotCoords[1])
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(plotCoords[0]), ", ", str(plotCoords[1]), ". Make sure that you are the owner of this plot"]))

        return True

    elif cmd == "info":
        if len(args) != 1:
            showHelp(sender)

            return True

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

        return True

    elif cmd == "generate":
        if len(args) != 2 or not args[1].isdigit():
            showHelp(sender)

            return True
        
        radius = int(args[1])

        for x in xrange(radius):
            for z in xrange(radius):
                y = 0

        return True

    return True

def showHelp(sender):
    sender.sendMessage("--- Plot Manager /plotmap Help ---")
    sender.sendMessage("/plotmap claim")
    sender.sendMessage("/plotmap unclaim")
    sender.sendMessage("/plotmap info")
    sender.sendMessage("/plotmap generate <radius>")
