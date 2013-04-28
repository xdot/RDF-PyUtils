import Manager

import PhysicalMap

from org.bukkit.Bukkit import getWorlds

directory = "plugins/PlotManager.py.dir"

@hook.enable
def onEnable():
    Manager.load(directory)
    PhysicalMap.world = getWorlds()[0]

@hook.disable
def onDisable():
    Manager.save(directory)

# Permission nodes:
# plotmanager.claim   - Claim/Auto
# plotmanager.info    - Info/PlayerInfo
# plotmanager.give    - Give
# plotmanager.admin   - ForceUnclaim
# plotmanager.reserve - Reserve/Special

##################################
# Claim a plot
##################################
def onCommandClaim(sender, args):
    if not sender.hasPermission("plotmanager.claim"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 1:
        x = Manager.getPlotX(sender.getLocation().getX())
        z = Manager.getPlotZ(sender.getLocation().getZ())

    elif len(args) == 3:
        x = int(args[1])
        z = int(args[2])

    else:
        sender.sendMessage("Usage: /plot claim [x] [z]")
        return

    if Manager.isOutOfRange(x, z):
        sender.sendMessage(''.join(["Plot ", str(x), ", ", str(z), " is out of range"]))
        return
        
    if Manager.claim(sender.getName(), x, z):
        sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
    else:
        sender.sendMessage(''.join(["Failed to unclaim plot ", str(x), ", ", str(z), ". Make sure that this is a free plot and that you are allowed to claim plots"]))

##################################
# Unclaim a plot
##################################
def onCommandUnclaim(sender, args):
    if len(args) == 1:
        x = Manager.getPlotX(sender.getLocation().getX())
        z = Manager.getPlotZ(sender.getLocation().getZ())

    elif len(args) == 3:
        x = int(args[1])
        z = int(args[2])
        
    else:
        sender.sendMessage("Usage: /plot unclaim [x] [z]")
        return 

    if Manager.isOutOfRange(x, z):
        sender.sendMessage(''.join(["Plot ", str(x), ", ", str(z), " is out of range"]))
        return

    if Manager.unclaim(sender.getName(), x, z):
        sender.sendMessage(''.join(["You successfully unclaimed plot ", str(x), ", ", str(z)]))
    else:
        sender.sendMessage(''.join(["Failed to unclaim plot ", str(x), ", ", str(z), ". Make sure that you are the owner of this plot"]))

##################################
# Print information about a plot
##################################
def onCommandInfo(sender, args):
    if not sender.hasPermission("plotmanager.info"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 1:
        x = Manager.getPlotX(sender.getLocation().getX())
        z = Manager.getPlotZ(sender.getLocation().getZ())

    elif len(args) == 3:
        x = int(args[1])
        z = int(args[2])

    else:
        sender.sendMessage("Usage: /plot info [x] [z]")
        return

    if Manager.isOutOfRange(x, z):
        sender.sendMessage(''.join(["Plot ", str(x), ", ", str(z), " is out of range"]))
        return

    plot = Manager.getPlot(x, z)

    sender.sendMessage(''.join(["--- Plot ", str(x), ", ", str(z), " ---"]))

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

##################################
# Teleport to a plot
##################################
def onCommandTp(sender, args):
    if not sender.hasPermission("plotmanager.tp"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 3:
        x = Manager.getCentreX(int(args[1]))
        z = Manager.getCentreZ(int(args[2]))

        if Manager.isOutOfRange(int(args[1]), int(args[2])):
            sender.sendMessage(''.join(["Plot ", args[1], ", ", args[2], " is out of range"]))
            return

    elif len(args) == 2:
        name = str(args[1])

        exists = False

        for pos, plot in Manager.plots.iteritems():
            if plot.status == Manager.PlotStatus.CLAIMED and plot.owner == name:
                x = Manager.getCentreX(pos[0])
                z = Manager.getCentreZ(pos[1])

                exists = True

        if not exists:
            sender.sendMessage(''.join(["Can't find player ", name]))
            return True

    else:
        sender.sendMessage("Usage: /plot tp <x> <z> OR <name>")
        return


    loc = sender.getLocation()

    loc.setX(x)
    loc.setZ(z)

    sender.teleport(loc)

##################################
# Auto-claim next free plot
##################################
def onCommandAuto(sender, args):
    if not sender.hasPermission("plotmanager.claim"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return
    
    if len(args) != 1:
        sender.sendMessage("Usage: /plot auto")
        return

    x = 0
    z = 0
    step = 1

    name = sender.getName()

    while True:
        for i in xrange(0, step):
            if Manager.claim(name, x, z):
	        sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                return

            x -= 1
           
        for i in xrange(0, step):
            if Manager.claim(name, x, z):
	        sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                return

            z -= 1

        step += 2

        for i in xrange(0, step):
            if Manager.claim(name, x, z):
	        sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                return

            x += 1

        for i in xrange(0, step):
            if Manager.claim(name, x, z):
                sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                return

            x -= 1
        
    sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))

##################################
# Print information about a player
##################################
def onCommandPlayerinfo(sender, args):
    if not sender.hasPermission("plotmanager.info"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 2:
        player = args[1]

    elif len(args) == 1:
        player = sender.getName()

    else:
        sender.sendMessage("Usage: /plot info [name]")
        return

    if player not in Manager.players:
        sender.sendMessage(''.join(["Can't find player ", player]))
        return

    sender.sendMessage(''.join(["--- Plots claimed by ", player, " ---"]))

    for pos, plot in Manager.plots.iteritems():
        if plot.status == Manager.PlotStatus.CLAIMED and plot.owner == player:
            sender.sendMessage(''.join([str(pos[0]), ", ", str(pos[1])]))

    sender.sendMessage(''.join([player, " can claim up to ", str(Manager.players[player].numPlots), " additional plots"]))

##################################
# Give a player an extra plot
##################################
def onCommandGive(sender, args):
    if not sender.hasPermission("plotmanager.give"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) != 3 or not args[2].isdigit():
        sender.sendMessage("Usage: /plot give <name> <number>")
        return

    if args[1] not in Manager.players:
        sender.sendMessage(''.join(["Can't find player ", sender.getName()]))

        return True

    player = Manager.getPlayer(args[1])

    player.numPlots += int(args[2])

    sender.sendMessage(''.join(["Player ", args[1], " can now claim up to ", str(player.numPlots), " additional plots"]))

##################################
# Forcefully unclaim a plot
##################################
def onCommandForceUnclaim(sender, args):
    if not sender.hasPermission("plotmanager.admin"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 1:
        x = Manager.getPlotX(sender.getLocation().getX())
        z = Manager.getPlotZ(sender.getLocation().getZ())

    elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
        x = int(args[1])
        z = int(args[2])
        
    else:
        sender.sendMessage("Usage: /plot forceUnclaim [x] [z]")
        return

    if Manager.isOutOfRange(x, z):
        sender.sendMessage(''.join(["Plot ", str(x), ", ", str(z), " is out of range"]))
        return

    Manager.forceUnclaim(x, z)

    sender.sendMessage(''.join(["Forcefully unclaimed plot ", str(x), ", ", str(z)]))

##################################
# Reserve a plot
##################################
def onCommandReserve(sender, args):
    if not sender.hasPermission("plotmanager.reserve"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 1:
        x = Manager.getPlotX(sender.getLocation().getX())
        z = Manager.getPlotZ(sender.getLocation().getZ())

    elif len(args) == 3:
        x = int(args[1])
        z = int(args[2])
        
    else:
        sender.sendMessage("Usage: /plot reserve [x] [z]")
        return

    if Manager.isOutOfRange(x, z):
        sender.sendMessage(''.join(["Plot ", str(x), ", ", str(z), " is out of range"]))
        return

    if Manager.reserve(x, z):
        sender.sendMessage(''.join(["You successfully reserved plot ", str(x), ", ", str(z)]))
    else:
        sender.sendMessage(''.join(["Failed to reserve plot ", str(x), ", ", str(z), ". Make sure that this is a free plot"]))

##################################
# Reserve a plot (Custom status)
##################################
def onCommandSpecial(sender, args):
    if not sender.hasPermission("plotmanager.reserve"):
        sender.sendMessage("You don't have enough permissions to execute this command")
        return

    if len(args) == 2:
        x = Manager.getPlotX(sender.getLocation().getX())
        z = Manager.getPlotZ(sender.getLocation().getZ())

    elif len(args) == 4:
        x = int(args[2])
        z = int(args[3])
        
    else:
        sender.sendMessage("Usage: /plot special [x] [z]")
        return

    if Manager.isOutOfRange(x, z):
        sender.sendMessage(''.join(["Plot ", str(x), ", ", str(z), " is out of range"]))
        return

    del args[0]

    if Manager.special(x, z, ' '.join(args)):
        sender.sendMessage(''.join(["You successfully reserved plot ", str(x), ", ", str(z)]))
    else:
        sender.sendMessage(''.join(["Failed to reserve plot ", str(x), ", ", str(z), ". Make sure that this is a free plot"]))

# Entry point
@hook.command("plot")
def onCommandPlot(sender, args):
    if len(args) == 0:
        showHelp(sender)

        return True
     
    cmd = args[0]
     
    if cmd == "claim":
        onCommandClaim(sender, args)
     
    elif cmd == "unclaim":
        onCommandUnclaim(sender, args)

    elif cmd == "info":
        onCommandInfo(sender, args)

    elif cmd == "tp":
        onCommandTp(sender, args)

    elif cmd == "auto":
        onCommandAuto(sender, args)

    elif cmd == "playerinfo":
        onCommandPlayerinfo(sender, args)

    elif cmd == "give":
        onCommandGive(sender, args)

    elif cmd == "forceUnclaim":
        onCommandForceUnclaim(sender, args)

    elif cmd == "reserve":
        onCommandReserve(sender, args)

    elif cmd == "special":
        onCommandSpecial(sender, args)

    else:
        showHelp(sender)

    return True

def showHelp(sender):
    sender.sendMessage("--- Plot Manager /plot Help ---")
    sender.sendMessage("/plot claim [x] [z]")
    sender.sendMessage("/plot unclaim [x] [z]")
    sender.sendMessage("/plot info [x] [x]")
    sender.sendMessage("/plot tp <x> <z> OR <name>")
    sender.sendMessage("/plot auto")
    sender.sendMessage("/plot playerinfo [name]")
    sender.sendMessage("--- Admin commands ---")
    sender.sendMessage("/plot give <name> <number>")
    sender.sendMessage("/plot forceUnclaim [x] [z]")
    sender.sendMessage("/plot reserve [x] [z]")
    sender.sendMessage("/plot special <description> [x] [z]")
