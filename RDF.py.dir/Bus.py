from Helper import sudo

import org.bukkit as bukkit

def setBlock(player, block, x, y, z):
    player.getWorld().getBlockAt(x, y, z).setTypeId(block)

def bus(x1, y1, z1, x2, y2, z2, player, block):
    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    if z1 > z2:
        z1, z2 = z2, z1

    while x1 != x2:
        setBlock(player, block, x1, y1, z1)
        x1 += 1

    while y1 != y2:
        setBlock(player, block, x1, y1, z1)
        y1 += 1

    while z1 != z2:
        setBlock(player, block, x1, y1, z1)
        z1 += 1

@hook.command("test-bus")
def onCommandTestBus(sender, args):
    bus(args[0], args[1], args[2], args[3], args[4], args[5], sender, 1)
    return True
