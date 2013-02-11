from Helper import color
from Helper import sudo

import org.bukkit as bukkit

# Time Commands
@hook.command("day")
def onCommandDay(sender, args):
    bukkit.Bukkit.dispatchCommand(sender, "ptime @noon")
    return True

@hook.command("night")
def onCommandNight(sender, args):
    bukkit.Bukkit.dispatchCommand(sender, "ptime @midnight")
    return True

# Fix lag
@hook.command("fixlag")
def onCommandFixLag(sender, args):
    bukkit.Bukkit.dispatchCommand(sender, "rem items -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem arrows -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem boats -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem paintings -1")
    bukkit.Bukkit.dispatchCommand(sender, "rem xp -1")

    bukkit.Bukkit.dispatchCommand(sender, "butcher -f")

    sudo("save-all")

    sender.sendMessage("You fixed teh lags!")
    return True

# Show chat colors
@hook.command("c")
def onCommandC(sender, args):
    sender.sendMessage(''.join([color("f"), "f ", color("7"), "7 ", color("e"), "e ", color("c"), "c ", color("d"), "d ", color("9"), "9 ", color("b"), "b ", color("a"), "a\n", color("0"), "0 ", color("8"), "8 ", color("6"), "6 ", color("4"), "4 ", color("5"), "5 ", color("1"), "1 ", color("3"), "3 ", color("2"), "2"]))
    return True
    
# AFK
@hook.command("afk")
def onCommandAFK(sender, args):
    sender.sendMessage("Please do not go AFK, it wastes my bandwidth")
    sender.sendMessage("Instead, please log off the server")
    return True

# Save all
@hook.command("save")
def onCommandSave(sender, args):
    sudo("save-all")
    return True