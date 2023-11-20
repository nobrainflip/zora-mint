from loguru import logger

from core.heater import Heater
from config import database_autocreate
from models.database import Database

start_message = rf'''
Zora Mint:
1: create_database        | create database
2: start_warmup           | start warm up

Generation of database is turned {"on" if database_autocreate else "off"}
'''


def main():
    logger.debug(start_message)
    module = input("Start module: ")

    if module == '1':
        Database(create_once=True)
    elif module == '2':
        heater = Heater()
        heater.warmup()
    else:
        logger.error("Invalid module.")


if __name__ == '__main__':
    main()
