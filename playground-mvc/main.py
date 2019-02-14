#!/usr/bin/env python3
import sys, getopt

from database import MyDatabase
from model import MyModel
from controller import MyController

def usage():
     print ("usage: ", sys.argv[0], "<view_mode>\n  -q, --qt\tLaunch program with Qt view\n  -s, --shell\tLaunch program with Shell view")
     sys.exit()

def parseOptions(argv):
    try:
      opts, args = getopt.getopt(argv[1:], "hsq", ["shell", "qt"])
    except getopt.GetoptError:
        usage()
    if (len(opts) != 1):
        usage()
    global MyView
    for opt, arg in opts:
        if (opt == '-h'):
            usage()
        elif (opt in ('-s', '--shell')):
            from viewShell import MyView
        elif (opt in ('-q', '--qt')):
            from viewQt import MyView

def run():
    view = MyView("MVC Playground", 300, 300, 800, 600)
    database = MyDatabase(42)
    model = MyModel(database)
    controller = MyController(model, view)
    controller.run()

def main(argv):
    print("__main__()")

    parseOptions(argv)
    run()

if __name__ == "__main__":
    main(sys.argv)
