#!/usr/bin/env python3

import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')