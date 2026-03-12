import logging
import os
from datetime import datetime

# create logs folder
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# create log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# create logger
logger = logging.getLogger(__name__)

logger.info("Logging system initialized")