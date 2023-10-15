class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


logo = r"""

  ,ad8888ba,                   ad88     ad88                                        88b           d88                          88           88                           
 d8"'    `"8b                 d8"      d8"                                          888b         d888                          88           ""                           
d8'                           88       88                                           88`8b       d8'88                          88                                        
88              ,adPPYba,   MM88MMM  MM88MMM   ,adPPYba,   ,adPPYba,                88 `8b     d8' 88  ,adPPYYba,   ,adPPYba,  88,dPPYba,   88  8b,dPPYba,    ,adPPYba,  
88             a8"     "8a    88       88     a8P_____88  a8P_____88                88  `8b   d8'  88  ""     `Y8  a8"     ""  88P'    "8a  88  88P'   `"8a  a8P_____88  
Y8,            8b       d8    88       88     8PP"""""""  8PP"""""""                88   `8b d8'   88  ,adPPPPP88  8b          88       88  88  88       88  8PP"""""""  
 Y8a.    .a8P  "8a,   ,a8"    88       88     "8b,   ,aa  "8b,   ,aa                88    `888'    88  88,    ,88  "8a,   ,aa  88       88  88  88       88  "8b,   ,aa  
  `"Y8888Y"'    `"YbbdP"'     88       88      `"Ybbd8"'   `"Ybbd8"'                88     `8'     88  `"8bbdP"Y8   `"Ybbd8"'  88       88  88  88       88   `"Ybbd8"'  

                                                                      888888888888                                                                                       
"""