"""
Main entry point for the Splitwise application.

This module demonstrates the usage of the Splitwise expense splitting system
by creating users, groups, and expenses with different split types.
"""

from splitwise import Splitwise

def main():
    """
    Main function that initializes and demonstrates the Splitwise application.
    
    Creates a Splitwise instance and runs the demo to show how the system
    handles expense splitting between users in a group.
    """
    splitwise = Splitwise()
    splitwise.demo()

if __name__ == "__main__":
    main()
