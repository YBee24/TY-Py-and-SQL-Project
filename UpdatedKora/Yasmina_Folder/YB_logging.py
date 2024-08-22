# YB_logging.py

# Import the logging module
import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Log to a file named 'app.log'
    filemode='w'  # Overwrite the log file each time the script runs
)

# Create a logger object
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
