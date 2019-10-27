from pathlib import Path
from sqlalchemy import create_engine
import sys

from db_management import Database
from pkg_installation import install_packages
from pkg_updation import update_packages
from pkg_uninstallation import uninstall_packages


if __name__ == "__main__":
    dbfile = Path("packages.db")
    database = Database()
    engine = database.engine
    db = database.packages
    
    if not dbfile.is_file():
        db, engine = database.initiate_engine()


    command = sys.argv[1]
    packages = sys.argv[2:]

    if command == "install" or command == "i":
        install_packages(packages, db, engine)
    
    elif command == "uninstall" or command == "un":
        uninstall_packages(packages, db, engine)
    
    elif command == "update" or command == "up":
        update_packages(packages, db, engine)
    
    elif command == "help" or command == "h" or command == "?":
        print("[+] Usage instructions:")

        # TODO: add usage instructions
    
    else:
        print('[-] %s is not a command. Please use "help" to look at usage instructions.' % command)
