from Helper import color

import FunAliases
import Aliases

import Derps

import NameSystem
import OnlinePlayers
import Schematics
import DomainNameForcer

import PlayerIPRelationships

import Bus

@hook.enable
def onEnable():
    Derps.load_derps("plugins/RDF.py.dir/derps.txt")
    PlayerIPRelationships.init("plugins/RDF.py.dir/IP")

@hook.disable
def onDisable():
    PlayerIPRelationships.saveData()

