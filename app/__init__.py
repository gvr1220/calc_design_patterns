import pkgutil
import importlib
import logging
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Check if it's a subclass of Command
                            self.command_handler.register_command(plugin_name, item())
                            logging.info(f"Command '{item.__name__}' from plugin '{plugin_name}' registered.")
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logging.info("Logging configured.")
        logging.info("Environment variables loaded.")

        # Dynamically load all command plugins
        self.load_plugins()

        # Explicitly register MenuCommand with command_handler
        menu_command = MenuCommand()
        self.command_handler.register_command("menu", menu_command)

        logging.info("Application started. Type 'exit' to exit.")
        print("Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip()
            if command_input.lower() == 'exit':
                break
            self.command_handler.execute_command(command_input)


if __name__ == "__main__":
    app = App()
    app.start()
