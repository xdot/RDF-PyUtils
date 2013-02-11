import org.bukkit as bukkit

def color(color):
    return u'\u00A7' + color

def sudo(command):
    bukkit.Bukkit.dispatchMessage(bukkit.Bukkit.getConsoleSender(), command)
