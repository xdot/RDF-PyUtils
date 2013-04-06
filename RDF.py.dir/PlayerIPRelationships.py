import collections

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
    known_players = pickle.load(open(directory + "/known_players.txt", "rb"))

def saveData():
    pickle.dump(latest_ip, open(path + "/latest_ip.txt", "wb"))
    pickle.dump(latest_player, open(path + "/latest_player.txt", "wb"))
    pickle.dump(known_ips, open(path + "/known_ips.txt", "wb"))
    pickle.dump(known_players, open(path + "/knwon_players", "wb"))

def init(directory):
    path = directory
    loadData()
    
@hook.command("playerinfo")
def onCommandPlayerInfo(sender, args):
    if len(args) == 0:
        return False

    sender.sendMessage(''.join("Showing IP Information for: ", args[0]))

    # WIP

    return True

@hook.command("ipinfo")
def onCommandIPInfo(sender, args):

    # WIP
    
    return True
