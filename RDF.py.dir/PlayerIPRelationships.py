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

def backup(directory):
    global path

    oldPath = path
    path = directory
    saveData()
    path = oldPath

@hook.command("playerinfo", usage="/<command> <playerName>")
def onCommandPlayerInfo(sender, args):
    if len(args) != 1:
        return False

    name = args[0]

    if name not in latest_ip or name not in known_ips:
        sender.sendMessage(''.join(["No IP information for: ", name]))

        return True

    sender.sendMessage(''.join(["Showing IP Information for: ", name]))

    sender.sendMessage(''.join(["Latest IP: ", latest_ip[name]]))
    sender.sendMessage(''.join(["Known IPs: ", ', '.join(known_ips[name])]))

    return True

@hook.command("ipinfo", usage="/<command> <ip>")
def onCommandIPInfo(sender, args):
    if len(args) != 1:
        return False

    ip = args[0]

    if ip not in latest_player or ip not in known_players:
        sender.sendMessage(''.join(["No Player information for: ", ip]))

        return True

    sender.sendMessage(''.join(["Showing Player Information for: ", ip]))

    sender.sendMessage(''.join(["Latest Player: ", latest_player[ip]]))
    sender.sendMessage(''.join(["Known Players: ", ', '.join(known_players[ip])]))
    
    return True

def registerIP(playerName, ip):
    global latest_ip
    global latest_player
    global known_ips
    global known_players
    
    latest_ip[playerName] = ip
    latest_player[ip] = playerName

    if ip not in known_ips[playerName]:
        known_ips[playerName].append(ip)

    if ip not in known_players[ip]:
        known_players[ip].append(playerName)

@hook.event("player.PlayerJoinEvent", "Monitor")
def onPlayerJoin(event):
    player = event.getPlayer()

    registerIP(player.getName(), player.getAddress().getHostName())
