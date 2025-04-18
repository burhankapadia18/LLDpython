# Pizza Factory - Design Pattern Implementation

## Overview
This project implements the Decorator Design Pattern to create a pizza ordering system. The system allows for the creation of a base pizza and adding various toppings dynamically, demonstrating how the Decorator pattern enables flexible object composition at runtime.

## Design Patterns Used
- **Decorator Pattern**: Allows behaviors to be added to individual objects without affecting the behavior of other objects from the same class. In this implementation, toppings decorate pizzas to add additional functionality (price and name modifications).

## Project Structure
```
pizza_factory/
├── main.py              # Entry point of the application
├── __init__.py          # Package initialization
├── pizza/               # Contains pizza base classes and concrete implementations
│   ├── base_pizza.py    # Abstract base class for all pizzas
│   └── margeritta.py    # Concrete pizza implementation
└── toppings/            # Contains topping decorator classes
    ├── base_topping.py  # Abstract base class for all toppings
    ├── extra_cheese.py  # Concrete topping implementation
    └── extra_ketchup.py # Concrete topping implementation
```

## Class Diagram

```
+-------------------------+
|      <<abstract>>      |
|       BasePizza        |
+-------------------------+
| - name: str            |
| - price: int           |
+-------------------------+
| + get_price(): int     |
| + get_name(): str      |
+-------------------------+
          ▲
          |
          |
+-------------------------+
|       Margeritta       |
+-------------------------+
| - name: "Margeritta"   |
| - price: 100           |
+-------------------------+
| + get_price(): int     |
| + get_name(): str      |
+-------------------------+

+-------------------------+
|      <<abstract>>      |
|      BaseTopping       |
+-------------------------+
| - pizza: BasePizza     |
| - price: int           |
+-------------------------+
| + get_price(): int     |
| + get_name(): str      |
+-------------------------+
          ▲
          |
     +-----------+
     |           |
+------------+  +-------------+
| ExtraCheese|  | ExtraKetchup|
+------------+  +-------------+
| - price: 10|  | - price: 5  |
+------------+  +-------------+
| + get_price(): int     | | + get_price(): int      |
| + get_name(): str      | | + get_name(): str       |
+------------------------+ +-------------------------+
```

## Class Descriptions

### Pizzas
- **BasePizza (Abstract)**: Defines the interface for all concrete pizza classes with abstract methods:
  - `get_price()`: Returns the price of the pizza
  - `get_name()`: Returns the name of the pizza

- **Margeritta**: A concrete implementation of BasePizza with:
  - Base price: 100
  - Name: "Margeritta"

### Toppings
- **BaseTopping (Abstract)**: Abstract class for all toppings, acting as a decorator:
  - Holds a reference to a decorated pizza
  - Defines abstract methods that will pass through to the decorated pizza

- **ExtraCheese**: A concrete topping that:
  - Adds 10 to the pizza's price
  - Appends " with extra cheese" to the pizza's name

- **ExtraKetchup**: A concrete topping that:
  - Adds 5 to the pizza's price
  - Appends " with extra ketchup" to the pizza's name

## Decorator Pattern Implementation

In this implementation:

- **Component**: BasePizza defines the interface that can be altered by decorators
- **Concrete Component**: Margeritta is a concrete BasePizza
- **Decorator**: BaseTopping is the abstract decorator class
- **Concrete Decorators**: ExtraCheese and ExtraKetchup are concrete decorators that add responsibilities to the pizza

The Decorator pattern creates a chain of responsibility where each topping in the chain:
1. Receives a request (get_price or get_name)
2. Adds its own behavior
3. Passes the request to the next object in the chain

For example, when `get_price()` is called on a pizza with multiple toppings:
- `ExtraKetchup → ExtraCheese → Margeritta`
- ExtraKetchup calls get_price() on ExtraCheese
- ExtraCheese calls get_price() on Margeritta
- Margeritta returns 100
- ExtraCheese adds 10 and returns 110
- ExtraKetchup adds 5 and returns 115

## Usage Examples

### Basic Usage

```python
from pizza.margeritta import Margeritta
from toppings.extra_cheese import ExtraCheese
from toppings.extra_ketchup import ExtraKetchup

# Create a basic pizza
pizza1 = Margeritta()
print(f"Price of {pizza1.get_name()} is {pizza1.get_price()}")  # Output: 100

# Add a single topping
pizza2 = ExtraCheese(Margeritta())
print(f"Price of {pizza2.get_name()} is {pizza2.get_price()}")  # Output: 110

# Add multiple toppings
pizza3 = ExtraKetchup(ExtraCheese(Margeritta()))
print(f"Price of {pizza3.get_name()} is {pizza3.get_price()}")  # Output: 115
```

### Advanced Usage

The system is designed to be easily extended:

1. **Creating a new pizza type**:
```python
from pizza.base_pizza import BasePizza

class Pepperoni(BasePizza):
    def __init__(self):
        self.name = "Pepperoni"
        self.price = 150
        
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name
```

2. **Creating a new topping**:
```python
from toppings.base_topping import BaseTopping
from pizza.base_pizza import BasePizza

class ExtraOlives(BaseTopping):
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza
        self.price = 8
        
    def get_price(self):
        return self.pizza.get_price() + self.price
    
    def get_name(self):
        return self.pizza.get_name() + " with extra olives"
```

## How to Run
```
python main.py
```

## Benefits of this Implementation

1. **Flexibility**: Toppings can be combined in any order and quantity without creating a class explosion
2. **Open/Closed Principle**: New pizzas and toppings can be added without modifying existing code
3. **Single Responsibility**: Each class has one clear responsibility
4. **Dynamic Composition**: Pizzas can be constructed at runtime with different combinations of toppings
5. **No Class Explosion**: Avoids creating separate classes for every possible pizza-topping combination 