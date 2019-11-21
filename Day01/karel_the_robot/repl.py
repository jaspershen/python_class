#!/usr/local/bin/python
#
import re, sys, time
from   lang  import Lang
from   env   import Environment, conditions

shortCuts = {}

def shortIt (short,full) :
    shortCuts[short] = full
    shortCuts[short+";"] = full+";"

def makeShortCuts() :
    cmds = list(conditions.keys())
    for cmd in cmds :
        words = cmd.split("-")
        abbr = "".join(x[0] for x in words)
        shortCuts[abbr] = cmd
    for w in ("BEGIN","END","ITERATE","TIMES","WHILE","DO","IF","THEN",
              "ELSE", "DEFINE-NEW-INSTRUCTION","AS") :
        shortCuts[w.lower()] = w
    shortIt('tl',"turnleft")
    shortIt('mv',"move")
    shortCuts["def"] = "DEFINE-NEW-INSTRUCTION"

def getInput() :
    words = []
    while True :
        try   : line = input("Karel> ")
        except: sys.exit()
        if line and line[0] == '@' :  # file import
            line = open(line[1:].strip()).read()
        line = re.sub("#.*"," ",line)      # strip comments
        line = re.sub(";"," ",line)        # semicolons are optional
        words += line.split()
        if line == "" :
            return [shortCuts.get(x,x) for x in words]

def fatal(mesg) :
    print ("Fatal error: %s" % mesg)
    sys.exit()

def repl() :
    interval = .3
    game = sys.argv[1]
    if len(sys.argv) > 2 : interval = float(sys.argv[2])
    exec("from {} import initBoard".format(game), globals())
    env = Environment(initBoard,fatal)
    makeShortCuts()
    
    env.printBoard()
    prog = Lang(env, "")  # source supplied piecemeal
    while True :
        prog.words = getInput()     # list of words
        while True :
            inst = prog.getInstruction()
            if inst == "EOF" : break
            print ("Compiled", inst)
            prog.execInstruction(inst)
            env.printBoard()

if __name__ == "__main__" : repl()
