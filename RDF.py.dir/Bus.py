from Helper import sudo

import org.bukkit as bukkit

rssignal = 0

def setBlock(player, block, data, x, y, z):
    player.getWorld().getBlockAt(x, y, z).setTypeId(block)
    player.getWorld().getBlockAt(x, y, z).setData(data)

def placeBlock(player, x, y, z, block, slope, orientation):
    global rssignal

    rssignal += 1
    block_id = 55

    if rssignal > 15:
        rssignal = 0
        block_id = 93

    new_y = y - 1 if slope else y

    setBlock(player, block, 0, x, new_y, z)
    setBlock(player, block_id, orientation, x, new_y + 1, z)

def bus(x1, y1, z1, x2, y2, z2, player, block):
    global rssignal

    rssignal = 0
    
    xgt = -1 if x1 > x2 else 1
    ygt = -1 if y1 > y2 else 1
    zgt = -1 if z1 > z2 else 1
    
    while x1 != x2:
        placeBlock(player, x1, y1, z1, block, False, 0)
        
        x1 += xgt

    while y1 != y2:
        placeBlock(player, x1, y1, z1, block, True, 1)

        y1 += ygt
        z1 += zgt

    while z1 != z2:
        placeBlock(player, x1, y1, z1, block, False, 2)
        
        z1 += zgt

@hook.command("test-bus")
def onCommandTestBus(sender, args):
    bus(int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), sender, 1)
    return True
