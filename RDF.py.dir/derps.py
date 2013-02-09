from __future__ import with_statement

from plugin import color

import org.bukkit as bukkit

import random

def load_derps(filename):
    with open(filename) as f:
            return f.read().splitlines()

def broadcast_derp(sender, message):
    bukkit.Bukkit.broadcastMessage(''.join([color("2"), " * ", color("f"),  ender.getName(), color("l"), " DERP! ", color("r"), color("d"),  message]))

def onCommandDerp(sender, args, derps):
    if len(args) > 0:
        broadcast_derp(sender, derps[int(args[0]) - 1])
    else:
        broadcast_derp(sender, random.choice(derps))

    return True
