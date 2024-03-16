import logging
import os


logger = logging.getLogger("app_logger")
logging.basicConfig(
    level=logging.__dict__[os.environ.get('LOGLEVEL', 'INFO')],
    format='%(asctime)s %(levelname)s: %(message)s')
