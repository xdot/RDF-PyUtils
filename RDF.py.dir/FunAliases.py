from Helper import color

import org.bukkit as bukkit

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
