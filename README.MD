# Small Business Inventory Tracker

#### 

#### Description:

The Small Business Inventory Tracker is a Python program designed to help small businesses organize and manage their products. Many small businesses need a simple and affordable way to keep track of inventory, monitor stock levels, and record sales. This project provides a menu-driven solution that runs in the Python console and allows users to manage items efficiently.

The program includes several important features. First, users can add new inventory items by entering the product name, quantity available, price, and reorder level. This allows businesses to create a list of products currently in stock.

Second, users can view the inventory at any time. The program displays each product with its quantity, price, and reorder level. This helps the user understand what items are available and which products may need restocking soon.

Third, the program allows stock updates. When new shipments arrive, the user can choose the update stock option and add more quantity to an existing item. This keeps inventory numbers accurate and current.

Fourth, users can record sales. When an item is sold, the user enters the item name and quantity sold. The program subtracts the amount sold from the inventory total. This feature is important because it keeps stock counts accurate after purchases.

This project was created using Python dictionaries and functions. A dictionary was chosen because it stores item names as keys and related information such as quantity, price, and reorder level as values. This makes data easy to organize and retrieve.

Functions were used to separate each major task, including add_item(), view_inventory(), update_stock(), and record_sale(). This design decision keeps the code organized, easier to read, and easier to maintain.

The files included in this project are:

- TermProject.py – Main Python program containing all code.
- README.md – Documentation file explaining the project.
- requirements.txt – Indicates that no external libraries are required.

One important design decision was keeping the program menu-driven and simple. Small business owners may not have technical experience, so the interface was designed to be easy to understand. Users simply choose a numbered option and follow prompts.

Another design choice was using built-in Python features only. No external libraries are needed, which means the project can run on nearly any computer with Python installed.

If expanded in the future, this project could include saving data to files, loading inventory automatically, generating reports, or adding a graphical user interface.

This project demonstrates how Python can be used to solve real-world business problems in a practical and user-friendly way.