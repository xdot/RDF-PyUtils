from __future__ import with_statement

import random

from Helper import color

import org.bukkit as bukkit

derps = []

def load_derps(filename):
    global derps
    
    with open(filename) as f:
            derps = f.read().splitlines()

def broadcast_derp(sender, message):
    bukkit.Bukkit.broadcastMessage(''.join([color("2"), " * ", color("f"), sender.getName(), color("l"), " DERP! ", color("r"), color("d"),  message]))

@hook.command("derp")
def onCommandDerp(sender, args):
    if len(args) > 0:
        broadcast_derp(sender, derps[int(args[0]) - 1])
    else:
        broadcast_derp(sender, random.choice(derps))

    return True
