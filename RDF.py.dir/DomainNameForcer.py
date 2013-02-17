import org.bukkit as bukkit

from Helper import info

from org.bukkit.event.player import PlayerLoginEvent

# TODO:
# /checkdomain

@hook.event("player.PlayerLoginEvent", "High")
def onPlayerJoin(event):
    if event.getHostname() != "mc.redstonedev.net:25565":
        event.disallow(PlayerLoginEvent.Result.KICK_OTHER, ''.join([event.getHostname(), " has been moved: using your browser, visit rdf.jessassin.net for more info"]))

        info(''.join([event.getPlayer().getName(), " failed login, using: ", event.getHostname()]))
    
