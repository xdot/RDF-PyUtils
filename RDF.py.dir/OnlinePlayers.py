# TODO:
# /online

@hook.command("online", description="List online players")
def onCommandOnline(sender, args):
    return True

@hook.command("list")
def onCommandList(sender, args):
    return onCommandOnline(sender, args)

@hook.command("who")
def onCommandWho(sender, args):
    return onCommandOnline(sender, args)
