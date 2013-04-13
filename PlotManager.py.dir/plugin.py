import Manager

import PhysicalMap

directory = "/plugins/PlotManager.py.dir"

@hook.enable
def onEnable():
    # Manager.load(directory)
    pass

@hook.disable
def onDisable():
    # Manager.save(directory)
    pass

@hook.command("plot")
def onCommandPlot(sender, args):
    if len(args) == 0:
        showHelp(sender)

        return True
     
    cmd = args[0]
     
    if cmd == "claim":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])

        else:
            showHelp(sender)

            return True
        
        if Manager.claim(sender.getName(), x, z):
            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(x), ", ", str(z), ". Make sure that this is a free plot and that you are allowed to claim plots"]))
     
    elif cmd == "unclaim":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])
        
        else:
            showHelp(sender)

            return True

        if Manager.unclaim(sender.getName(), x, z):
            sender.sendMessage(''.join(["You successfully unclaimed plot ", str(x), ", ", str(z)]))
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(x), ", ", str(z), ". Make sure that you are the owner of this plot"]))

    elif cmd == "info":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])

        else:
            showHelp(sender)

            return True

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

    elif cmd == "tp":
        if len(args) == 3:
            x = Manager.getCentreX(int(args[1]))
            z = Manager.getCentreZ(int(args[2]))

        else:
            showHelp(sender)

            return True

        loc = sender.getLocation()

        loc.setX(x)
        loc.setZ(z)

        sender.teleport(loc)

        return True

    elif cmd == "auto":
        if len(args) != 1:
            showHelp(sender)

            return True

        x = 0
        z = 0

        step = 1

        name = sender.getName()

        while True:
            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                    return True

                x -= 1
            
            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                    return True

                z -= 1

            step += 2

            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                    return True

                x += 1

            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))
                    return True

                x -= 1
        
        sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))

        return True

    elif cmd == "playerinfo":
        if len(args) == 2:
            player = args[1]

        elif len(args) == 1:
            player = sender.getName()

        else:
             showHelp(sender)

             return True

        if player not in Manager.players:
             sender.sendMessage(''.join(["Can't find player ", player]))

             return True

        sender.sendMessage(''.join(["--- Plots claimed by ", player, " ---"]))

        for pos, plot in Manager.plots.iteritems():
            if plot.status == Manager.PlotStatus.CLAIMED and plot.owner == player:
                sender.sendMessage(''.join([str(pos[0]), ", ", str(pos[1])]))

        sender.sendMessage(''.join([player, " can claim up to ", str(Manager.players[player].numPlots), " additional plots"]))

        return True

    # Admin commands
    elif cmd == "give":
         if len(args) != 3 or not args[2].isdigit():
             showHelp(sender)

             return True

         if sender.getName() not in Manager.players:
             sender.sendMessage(''.join(["Can't find player ", sender.getName()]))

             return True

         player = Manager.getPlayer(sender.getName())

         player.numPlots += int(args[2])

         sender.sendMessage(''.join(["Player ", sender.getName(), " can now claim up to ", str(player.numPlots), " additional plots"]))

         return True

    elif cmd == "forceUnclaim":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])
        
        else:
            showHelp(sender)

            return True

        Manager.forceUnclaim(x, z)

        sender.sendMessage(''.join(["Unclaimed plot ", str(x), ", ", str(z)]))

        return True

    elif cmd == "reserve":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])
        
        else:
            showHelp(sender)

            return True

        if Manager.reserve(x, z):
            sender.sendMessage(''.join(["You successfully reserved plot ", str(x), ", ", str(z)]))
        else:
            sender.sendMessage(''.join(["Failed to reserve plot ", str(x), ", ", str(z), ". Make sure that this is a free plot"]))

        return True

    else:
        showHelp(sender)

    return True

def showHelp(sender):
    sender.sendMessage("--- Plot Manager /plot Help ---")
    sender.sendMessage("/plot claim [x] [z]")
    sender.sendMessage("/plot unclaim [x] [z]")
    sender.sendMessage("/plot info [x] [x]")
    sender.sendMessage("/plot tp <x> <z>")
    sender.sendMessage("/plot auto")
    sender.sendMessage("/plot playerinfo [name]")
    sender.sendMessage("--- Admin commands ---")
    sender.sendMessage("/plot give <name> <number>")
    sender.sendMessage("/plot forceUnclaim [x] [z]")
    sender.sendMessage("/plot reserve [x] [z]")
