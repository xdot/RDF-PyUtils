from math import *

funcList = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
funcDict = dict([ (k, locals().get(k, None)) for k in funcList ])

# Temperature convertion
@hook.command("temp", usage="/<command> <temperature> <F,C>")
def onCommandTemp(sender, args):
    if len(args) < 2:
        return False

    temp = int(args[0])
        
    if args[1] == "C":
        result = ((temp * 9) / 5) + 32
        
        sender.sendMessage(''.join([args[0], " Degrees Celsius Is ", str(result), " Degrees Farenheit"])) 
        return True

    elif args[1] == "F":
        result = ((temp - 32) * 5) / 9

        sender.sendMessage(''.join([args[0], " Degrees Farenheit Is ", str(result), " Degrees Celsius"]))
        return True

    return False

# Expression
@hook.command("expr")
def onCommandExpr(sender, args):
    if len(args) == 0:
        return False

    expr = ''.join(args)

    # WIP

    return True
