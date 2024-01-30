# TEC Fashion Inventory System

This repository contains a Python script (`ropaMenu.py`) for managing a clothing inventory system. The script utilizes classes (`Ropa`, `Camisa`, `Pantalon`, `Sueter`), functions (`menu()`, `menuSecundario()`), and file handling (`archivos.py`) to allow users to register, delete, update prices, and display information about clothing items.

## File: `ropaMenu.py`
### Main Menu Options:
1. **Shirt Registration:**
   Register a new shirt in the inventory.

3. **Pants Registration:**
   Register a new pair of pants in the inventory.

5. **Sweater Registration:**
   Register a new sweater in the inventory.

6. **Delete Product:**
   Remove a product from the inventory.

7. **Change Price:**
   Modify the price of a product.

8. **Show Full Inventory:**
   Display information about all items in the inventory.

9. **Show Product Inventory:**
   Display information about a specific type of product.

10. **Exit:**
Save changes and exit the program.

### Additional Menu Options:
- **Secondary Menu:**
  Access additional information about specific types of clothing.

### File Handling:
Data is stored and retrieved using the `lee` and `grabar` functions from `archivos.py`.

### Classes:
- **Ropa (Clothing):**
  Base class containing general attributes for all clothing items.

- **Camisa (Shirt):**
  Derived class from `Ropa` with additional attributes for shirts.

- **Pantalon (Pants):**
  Derived class from `Ropa` with additional attributes for pants.

- **Sueter (Sweater):**
  Derived class from `Ropa` with additional attributes for sweaters.
