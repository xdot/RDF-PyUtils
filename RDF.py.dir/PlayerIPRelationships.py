from collections import defaultdict

latest_ip = {}
latest_player = {}
known_ips = defaultdict(list)
known_players = defaultdict(list)

path = ""

# Using pickle for now, subject to change
import pickle

def loadData():
    global latest_ip
    global latest_player
    global known_ips
    global known_players
    
    latest_ip = pickle.load(open(path + "/latest_ip.txt", "rb"))
    latest_player = pickle.load(open(path + "/latest_player.txt", "rb"))
    known_ips = pickle.load(open(path + "/known_ips.txt", "rb"))
    known_players = pickle.load(open(path + "/known_players.txt", "rb"))

def saveData():
    pickle.dump(latest_ip, open(path + "/latest_ip.txt", "wb"))
    pickle.dump(latest_player, open(path + "/latest_player.txt", "wb"))
    pickle.dump(known_ips, open(path + "/known_ips.txt", "wb"))
    pickle.dump(known_players, open(path + "/known_players.txt", "wb"))

def init(directory):
    global path

    path = directory

    loadData()

@hook.command("playerinfo", usage="/<command> <playerName>")
def onCommandPlayerInfo(sender, args):
    if len(args) != 1:
        return False

    name = args[0]

    if name not in latest_ip or name not in known_ips:
        sender.sendMessage(''.join("No IP information for: ", name))

        return True

    sender.sendMessage(''.join("Showing IP Information for: ", name))

    sender.sendMessage(''.join("Latest IP: ", latest_ip[name]))
    sender.sendMessage(''.join("Known IPs: ", ', '.join(known_ips[name])))

    # WIP

    return True

@hook.command("ipinfo")
def onCommandIPInfo(sender, args):

    # WIP
    
    return True

def registerIP(playerName, ip):
    global latest_ip
    global latest_player
    global known_ips
    global known_players
    
    latest_ip[playerName] = ip
    latest_player[ip] = playerName

    known_ips[playerName].append(ip)
    known_players[ip].append(playerName)

# TEST
@hook.command("_registerIP")
def onCommand_RegisterIP(sender, args):
    if len(args) != 2:
        return False

    registerIP(args[0], args[1])

    info(''.join(["Registered Player ", args[0], " with IP ", args[1]]))

    onCommandPlayerInfo(sender, args)

    return True
