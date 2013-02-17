import org.bukkit as bukkit

from java.util.logging import Level

def color(color):
    return u'\u00A7' + color

# Execute a command with root permissions
def sudo(command):
    bukkit.Bukkit.dispatchCommand(bukkit.Bukkit.getConsoleSender(), command)

def info(message):
    bukkit.Bukkit.getServer().getLogger().log(Level.INFO, message)

def severe(message):
    bukkit.Bukkit.getServer().getLogger().log(Level.SEVERE, message)
