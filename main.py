# main.py
import logging.config
from app import App

# Configure logging
logging.config.fileConfig('login.conf')

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App