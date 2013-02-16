import org.bukkit as bukkit

@hook.event("player.PlayerLoginEvent", "High")
def onPlayerJoin(event):
    if event.getHostname() != "mc.redstonedev.net":
        event.disallow(bukkit.event.player.PlayerLoginEvent.KICK_OTHER, ''.join(event.getHostname(), " has been moved: using your browser, visit rdf.jessassin.net for more info"))

    
