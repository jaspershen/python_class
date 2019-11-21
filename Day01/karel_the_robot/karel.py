#!/usr/local/bin/python
#
#  karel.py
#
import re, sys
from   lang import Lang
from   env  import Environment

def readProgram(karelProgram) :
    prog = open(karelProgram).read()
    prog = re.sub("#.*"," ",prog)      # strip comments
    return re.sub(";"," ",prog)        # semicolons are optional

def main() :
    game = sys.argv[1]
#    exec("from {} import initBoard".format(game), globals())
    game_import = "from " + game + " import initBoard"
    exec (game_import, globals())
    program = readProgram(sys.argv[2])
    env = Environment(initBoard,exit)
    env.printBoard()
    prog = Lang(env, program)
    while True :
        inst = prog.getInstruction()
        if inst == "EOF" : break
        if not inst : continue
        prog.execInstruction(inst)

if __name__ == "__main__" : main()
