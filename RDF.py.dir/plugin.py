__plugin_mainclass__ = "RDFMain"

from Helper import color

import FunAliases
import Aliases
import Derps

class RDFMain(PythonPlugin):
    def onEnable(self):
        print "RDF-PyUtils enabled"

    def onDisable(self):
        print "RDF-PyUtils disabled"
