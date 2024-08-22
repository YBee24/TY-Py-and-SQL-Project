# Import BaseModel and validator from pydantic
from pydantic import BaseModel, ValidationError, validator

# Define a data model using Pydantic's BaseModel
class User(BaseModel):
    # Define fields with their types
    id: int
    name: str
    email: str
    age: int

    # Define a custom validator for the age field
    @validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Age must be at least 18')
        return value

# Example usage
try:
    # Create an instance of the User model with valid data
    user = User(id=1, name='John Doe', email='john.doe@example.com', age=25)
    print(user)
except ValidationError as e:
    # Handle validation errors
    print(e.json())
