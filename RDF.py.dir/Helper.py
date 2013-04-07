import org.bukkit.Bukkit as bukkit

from java.util.logging import Level

def color(color):
    return u'\u00A7' + color

# Execute a command with root permissions
def sudo(command):
    bukkit.dispatchCommand(bukkit.getConsoleSender(), command)

def info(message):
    bukkit.getServer().getLogger().log(Level.INFO, message)

def severe(message):
    bukkit.getServer().getLogger().log(Level.SEVERE, message)
