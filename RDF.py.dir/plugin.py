__plugin_mainclass__ = "RDFMain"

#import derps

def color(color):
    return u'\u00A7' + color

class RDFMain(PythonPlugin):
    def onEnable(self):
        print "RDF-PyUtils enabled"

    def onDisable(self):
        print "RDF-PyUtils disabled"

# Aliases

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

    bukkit.Bukkit.dispatchCommand(bukkit.Bukkit.getConsoleSender(), "save-all")

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

# Animal Sounds
def broadcast_animal_sound(sender, message):
    bukkit.Bukkit.broadcastMessage(''.join([color("e"), sender.getName(), " ", color("f"), message]))

@hook.command("lemur")
def onCommandLemur(sender, args):
    broadcast_animal_sound(sender, "Barks and screeches like a lemur!")
    return True

@hook.command("moo")
def onCommandMoo(sender, args):
    broadcast_animal_sound(sender, "Moos like a cow!")
    return True

@hook.command("oink")
def onCommandOink(sender, args):
    broadcast_animal_sound(sender, "Oinks like a pig!")
    return True

@hook.command("cluck")
def onCommandCluck(sender, args):
    broadcast_animal_sound(sender, "Clucks like a chicken!")
    return True

@hook.command("bark")
def onCommandBark(sender, args):
    broadcast_animal_sound(sender, "Barks like a dog!")
    return True

@hook.command("baa")
def onCommandBaa(sender, args):
    broadcast_animal_sound(sender, "Baas like a sheep!")
    return True

@hook.command("brains")
def onCommandBrains(sender, args):
    broadcast_animal_sound(sender, "BRAAAAAAAAAAINS like a zombie!")
    return True

@hook.command("sss")
def onCommandSss(sender, args):
    broadcast_animal_sound(sender, "SSSSSSSSsssssssssssss-s like a creeper!")
    return True
