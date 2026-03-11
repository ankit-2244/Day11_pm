import logging

# Configure logging to a file
logging.basicConfig(
    filename='inventory_errors.log', 
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class InsufficientStockError(Exception):
    """Raised when trying to purchase more items than available in stock."""
    pass

def process_order():
    """Processes a simple order from a predefined inventory dictionary."""
    inventory = {
        'laptop': 5,
        'mouse': 15,
        'keyboard': 0
    }
    
    print("--- Inventory order system ---")
    print(f"Available items: {', '.join(inventory.keys())}")
    
    try:
        item = input("Enter the item you want to order: ").lower().strip()
        
        # Check if item exists (will raise KeyError if not carefully handled, but we'll use dict lookup explicitly to demo exception handling)
        if item not in inventory:
            raise KeyError(f"Item '{item}' is not recognized in our database.")
            
        quantity_str = input(f"How many '{item}'s would you like to buy?: ")
        quantity = int(quantity_str)
        
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
            
        if quantity > inventory[item]:
            raise InsufficientStockError(f"Requested {quantity}, but only {inventory[item]} '{item}'s are available.")
            
    except KeyError as ke:
        logging.error(f"Invalid item lookup: {ke}")
        print(f"We could not find that item in our catalog. {ke}")
    except ValueError as ve:
        logging.error(f"Invalid quantity format/value entered. User entered: {quantity_str}")
        print(f"Invalid quantity specified. {ve} Please enter a valid positive number.")
    except InsufficientStockError as ise:
        logging.error(f"Order failed due to stock limits: {ise}")
        print(f"Sorry, we cannot fulfill your order. {ise}")
    else:
        inventory[item] -= quantity
        print(f"Order successful! You bought {quantity} {item}(s).")
        print(f"Remaining stock for {item}: {inventory[item]}")
    finally:
        print("Thank you for using the inventory system.\n")

if __name__ == "__main__":
    process_order()
