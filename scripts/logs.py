#!/usr/bin/env python3

import logging
from colorama import Fore, Back, Style

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
