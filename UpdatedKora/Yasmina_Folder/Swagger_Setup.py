# Swagger_Setup.py

# Import Flask and Flasgger modules
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

# Create a Flask application
app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)

# Define a route to handle API requests
@app.route('/api/data', methods=['GET', 'POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'A successful response',
            'examples': {
                'application/json': {
                    'message': 'This is a GET request'
                }
            }
        }
    }
})
def handle_data():
    """
    A simple endpoint to handle GET and POST requests.
    ---
    tags:
      - Data API
    parameters:
      - name: body
        in: body
        required: false
        schema:
          type: object
          properties:
            name:
              type: string
              description: The name of the person.
              example: John Doe
            age:
              type: integer
              description: The age of the person.
              example: 30
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            message:
              type: string
              description: The response message.
              example: This is a GET request
    """
    # Log the incoming request
    app.logger.info(f'Received {request.method} request to /api/data')

    # Handle GET request
    if request.method == 'GET':
        app.logger.debug('Handling GET request')
        return jsonify({'message': 'This is a GET request'})

    # Handle POST request
    elif request.method == 'POST':
        app.logger.debug('Handling POST request')
        data = request.json
        app.logger.info(f'Received data: {data}')
        return jsonify({'message': 'Data received', 'data': data})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True) # 'True' when in Development Stages, but 'False' when in Production Env. I.e. I'll disable debugging to enhance security and performance when the App is eventually open to end-users

# Create a Flask application
app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)
