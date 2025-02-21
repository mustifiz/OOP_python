# Python OOP Examples

This repository contains examples demonstrating Object-Oriented Programming (OOP) concepts in Python, specifically focusing on inheritance and polymorphism. 

## Project Structure

```
python-oop-examples
├── src
│   └── examples
│       ├── inheritance.py
│       ├── polymorphism.py
│       └── vehicle.py
├── tests
│   └── test_vehicle.py
├── requirements.txt
└── README.md
```

## Examples

### Inheritance

The `inheritance.py` file demonstrates the concept of inheritance in Python by defining a base class and derived classes that inherit from it.

### Polymorphism

The `polymorphism.py` file showcases polymorphism by using methods in derived classes that override methods in the base class.

### Vehicle Example

The `vehicle.py` file contains the implementation of the `Vehicle`, `Car`, `Boat`, and `Plane` classes, illustrating both inheritance and polymorphism. Below is an example of how to use these classes:

```python
# Example usage of Vehicle classes

# Create instances of each class
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Display their brands and models
for vehicle in (car1, boat1, plane1):
    print(vehicle.brand)
    print(vehicle.model)
    vehicle.move()
```

### Running Tests

The `test_vehicle.py` file contains unit tests for the `Vehicle` class and its derived classes to ensure they behave as expected. You can run the tests using the following command:

```bash
pytest tests/test_vehicle.py
```

## License

This project is licensed under the MIT License.
