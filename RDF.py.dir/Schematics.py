from org.bukkit.Bukkit import dispatchCommand

@hook.command("/save", usage="/<command> <name>")
def onCommandSave(sender, args):
    if len(args) != 1:
        return False

    dispatchCommand(sender, ''.join(["/schematic save mcedit ", sender.getName(), "/", args[0]]))

    return True

@hook.command("/load", usage="/<command> <name>")
def onCommandLoad(sender, args):
    if len(args) != 1:
        return False

    dispatchCommand(sender, ''.join(["/schematic load mcedit ", sender.getName(), "/", args[0]])) 

    return True
