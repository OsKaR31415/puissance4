#!/bin/python3

class Users:
    """
    Simple class to manipulate 2 users.
    The class cas simply switch between users, and show the current one.
    Users are represented as integers, 1 or 2.
    The default user is 1.
    """

    def __init__(self):
        self.__current = 1

    def switch(self):
        """Switch to the next user (the only other since there are only 2)"""
        if self.__current == 1:
            self.__current = 2
        else:
            self.__current = 1

    def current(self):
        """Return the current user's index (1 or 2)"""
        return self.__current

    def current_logo(self):
        """Return the logo of the current user.
        The user 1 's logo is 'O'.
        The user 2 's logo is 'X'.
        """
        return 'OX'[self.__current - 1]
