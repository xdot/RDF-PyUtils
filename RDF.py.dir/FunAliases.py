from Helper import color

from org.bukkit import Effect

import org.bukkit as bukkit

# Animal Sounds
def broadcast_animal_sound(sender, message):
    bukkit.Bukkit.broadcastMessage(''.join([color("e"), sender.getName(), " ", color("f"), message]))

@hook.command("lemur", description="Bark like a lemur!")
def onCommandLemur(sender, args):
    broadcast_animal_sound(sender, "Barks and screeches like a lemur!")
    return True

@hook.command("moo", description="Moo like a cow!")
def onCommandMoo(sender, args):
    broadcast_animal_sound(sender, "Moos like a cow!")
    return True

@hook.command("oink", description="Oink like a pig!")
def onCommandOink(sender, args):
    broadcast_animal_sound(sender, "Oinks like a pig!")
    return True

@hook.command("cluck", description="Cluck like a chicken!")
def onCommandCluck(sender, args):
    broadcast_animal_sound(sender, "Clucks like a chicken!")
    return True

@hook.command("bark", description="Bark like a dog!")
def onCommandBark(sender, args):
    broadcast_animal_sound(sender, "Barks like a dog!")
    return True

@hook.command("baa", description="Baa like a sheep!")
def onCommandBaa(sender, args):
    broadcast_animal_sound(sender, "Baas like a sheep!")
    return True

@hook.command("brains", description="Brains like a zombie!")
def onCommandBrains(sender, args):
    broadcast_animal_sound(sender, "BRAAAAAAAAAAINS like a zombie!")
    return True

@hook.command("sss", description="SSS like a creeper!")
def onCommandSss(sender, args):
    broadcast_animal_sound(sender, "SSSSSSSSsssssssssssss-s like a creeper!")
    return True

# General
@hook.command("confused", description="Have ALL the confusion!")
def onCommandConfused(sender, args):
    broadcast_animal_sound(sender, "has ALL THE CONFUSION!")
    return True

@hook.command("nope", description="Don't you dare!")
def onCommandNope(sender, args):
    sender.sendMessage("Chuck Testa!")
    return True

@hook.command("lag", description="Fix the server's lag!")
def onCommandLag(sender, args):
    sender.kickPlayer("I FIXED YOUR LAG! :D <3 Jessassin :P")
    return True

@hook.command("join", description="Make someone join the server!", usage="/<command> <player> [location]")
def onCommandJoin(sender, args):
    if len(args) < 1:
        return False
    
    bukkit.Bukkit.broadcastMessage(''.join([color("e"), args[0], " joined the game"]))
    
    if len(args) > 1:
        bukkit.Bukkit.broadcastMessage(''.join(["Player ", args[0], " comes from ", args[1]]))

    return True

@hook.command("hat", description="Get the most fashionable hat!")
def onCommandHat(sender, args):
    sender.getInventory().setHelmet(sender.getItemInHand())
    sender.getInventory().removeItem(sender.getItemInHand())

    sender.sendMessage("Look at your hat, your hat is amazing!")

    return True

@hook.command("huzza")
def onCommandHuzza(sender, args):
    # TODO: Add support for custom name colors
    
    bukkit.Bukkit.broadcastMessage(''.join([sender.getName(), color("f"), " Yells: HUZZA!"]))
    bukkit.Bukkit.dispatchCommand(sender, "suicide")

    return True

@hook.command("sound")
def onCommandSound(sender, args):
    location = sender.getLocation()
    world = sender.getWorld()

    world.playEffect(location, Effect.BOW_FIRE, 1, 0)
    world.playEffect(location, Effect.EXTINGUISH, 1, 0)
    world.playEffect(location, Effect.GHAST_SHRIEK, 1, 0)
    world.playEffect(location, Effect.CLICK1, 1, 0)
    world.playEffect(location, Effect.CLICK2, 1, 0)
    world.playEffect(location, Effect.GHAST_SHOOT, 1, 0)
    world.playEffect(location, Effect.POTION_BREAK, 1, 0)
    world.playEffect(location, Effect.ZOMBIE_CHEW_WOODEN_DOOR, 1, 0)
    world.playEffect(location, Effect.ZOMBIE_CHEW_IRON_DOOR, 1, 0)
    world.playEffect(location, Effect.ZOMBIE_DESTROY_DOOR, 1, 0)
    world.playEffect(location, Effect.MOBSPAWNER_FLAMES, 1, 0)

    return True
