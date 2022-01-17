#!/bin/python3

PLAYER_1_LOGO = "\u001b[31m⬤ \u001b[0m"
PLAYER_2_LOGO = "\u001b[33m⬤ \u001b[0m"

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
        The user 1 's logo is PLAYER_1_LOGO
        The user 2 's logo is PLAYER_2_LOGO
        """
        return (PLAYER_1_LOGO, PLAYER_2_LOGO)[self.__current - 1]
