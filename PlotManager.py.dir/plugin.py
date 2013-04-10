import Manager

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

            # Manager.save(directory)
        else:
            sender.sendMessage(''.join(["Failed to unclaim plot ", str(x), ", ", str(z), ". Make sure that this is a free plot"]))
     
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

            # Manager.save(directory)
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

	            # Manager.save(directory)

                    return True

                x -= 1
            
            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))

	            # Manager.save(directory)

                    return True

                z -= 1

            step += 2

            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))

	            # Manager.save(directory)

                    return True

                x += 1

            for i in xrange(0, step):
                if Manager.claim(name, x, z):
	            sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))

	            # Manager.save(directory)

                    return True

                x -= 1
        
        sender.sendMessage(''.join(["You successfully claimed plot ", str(x), ", ", str(z)]))

        # Manager.save(directory)

        return True

    elif cmd == "playerinfo":
        return True

    elif cmd == "member":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])

        else:
            showHelp(sender)

            return True

    elif cmd == "guest":
        if len(args) == 1:
            x = Manager.getPlotX(sender.getLocation().getX())
            z = Manager.getPlotZ(sender.getLocation().getZ())

        elif len(args) == 3 and args[1].isdigit() and args[2].isdigit():
            x = int(args[1])
            z = int(args[2])

        else:
            showHelp(sender)

            return True

    else:
        showHelp(sender)

    return True

def showHelp(sender):
    sender.sendMessage("--- Plot Manager Help ---")
    sender.sendMessage("/plot claim [x] [z]")
    sender.sendMessage("/plot unclaim [x] [z]")
    sender.sendMessage("/plot info [x] [x]")
    sender.sendMessage("/plot tp <x> <z>")
    sender.sendMessage("/plot auto")
    sender.sendMessage("/plot playerinfo <name>")
    sender.sendMessage("/plot member <add/remove> <name>")
    sender.sendMessage("/plot guest <add/remove> <name>")
