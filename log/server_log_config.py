import logging
from logging import handlers
import sys  
import os    

logger = logging.getLogger('server')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

fname = "log/server.log"
mbytes = 4000

rh = handlers.RotatingFileHandler(
  filename=fname,
  maxBytes = mbytes,
  backupCount = 3
)
rh.setFormatter(formatter)

logger.addHandler(rh)
logger.setLevel(logging.DEBUG) 

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logger.addHandler(console)





