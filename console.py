#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import models
from models.parent_model import Parentmodel
from models.Books_model import Books
from models.Category_model import Category
from models.Review_model import Reviews
from models.User_model import User


class EBookcmd(cmd.Cmd):
    
    prompt = "{ebook}"
    classes = {'User': User, 'Reviews': Reviews, 'Category': Category,
               'Books': Books, 'Parentmodel': Parentmodel}

    def do_create(self, args):
        """ Create an object of any class"""
        user_input = args.split()
        classname = user_input[0]
        if not args:
            print("** class name missing **")
            return
        elif classname not in EBookcmd.classes:
            print("** class doesn't exist **")
            return
        new_dict = {}
        keywords = user_input[1:]

        for keyword in keywords:
            word = keyword.split("=")
            key = word[0]
            value = word[1]
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('\\"', '"').replace("_", " ")
            else:
                try:
                    value = int(value)
                except Exception:
                    try:
                        value = float(value)
                    except Exception:
                        continue
            new_dict[key] = value

        new_instance = EBookcmd.classes[classname](**new_dict)
        print(new_instance.id)
        new_instance.save()


if __name__ == "__main__":
    EBookcmd().cmdloop()
