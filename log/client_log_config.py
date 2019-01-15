import logging
import sys      

logger = logging.getLogger('client')

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

fh = logging.FileHandler("log/client.log", encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.INFO)

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)





