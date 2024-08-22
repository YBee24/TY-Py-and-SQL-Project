# YB_app.py

# Import Flask and logging modules
from flask import Flask, request
import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log format
    filename='YB_app.log',  # Log to a file named 'app.log'
    filemode='w'  # Overwrite the log file each time the script runs
)

# Create a logger object
logger = logging.getLogger(__name__)

# Create a Flask application
app = Flask(__name__)

# Define a route to handle API requests
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    # Log the incoming request
    logger.info(f'Received {request.method} request to /api/data')

    # Handle GET request
    if request.method == 'GET':
        logger.debug('Handling GET request')
        return {'message': 'This is a GET request'}

    # Handle POST request
    elif request.method == 'POST':
        logger.debug('Handling POST request')
        data = request.json
        logger.info(f'Received data: {data}')
        return {'message': 'Data received', 'data': data}

# Define a route to simulate an error
@app.route('/api/error', methods=['GET'])
def simulate_error():
    try:
        # Simulate an error
        raise ValueError('An example error')
    except ValueError as e:
        # Log the error
        logger.error(f'Error occurred: {e}')
        return {'error': str(e)}, 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

