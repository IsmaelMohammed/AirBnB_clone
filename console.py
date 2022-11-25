#!/usr/bin/python3
"""command interpreter"""

import cmd
import shlex
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """commandLine Class"""
    my_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity",
                  "Review"]
    my_args = ['all', 'count', 'show', 'destroy', 'update']

    def emptyline(self):
        """emptyline"""
        pass

    def do_EOF(self, args):
        """ctrl+d"""
        print()
        return True

    def do_quit(self, args):
        """ctrl+z"""
        quit()
        return True

    if sys.stdin.isatty():
        prompt = "(hbnb)"
    else:
        prompt = "(hbnb)\n"

    def main():
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()