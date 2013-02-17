@hook.command("playerinfo")
def onCommandPlayerInfo(sender, args):
    if len(args) == 0:
        return False

    sender.sendMessage(''.join("Showing IP Information for: ", args[0]))

    # WIP

    return True

@hook.command("ipinfo")
def onCommandIPInfo(sender, args):

    # WIP
    
    return True
