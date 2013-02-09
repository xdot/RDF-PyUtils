__plugin_mainclass__ = "RDFMain"

import derps

def color(color):
    return u'\u00A7' + color

class RDFMain():
    def onEnable(self):
        print "RDF-PyUtils enabled"

    def onDisable(self):
        print "RDF-PyUtils disabled"
