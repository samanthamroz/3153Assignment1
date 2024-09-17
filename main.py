### Data ###
from contextlib import nullcontext

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] < ingredients["bread"]:
            print("Sorry, there is not enough bread.")
            return False
        if self.machine_resources["ham"] < ingredients["ham"]:
            print("Sorry, there is not enough ham.")
            return False
        if self.machine_resources["cheese"] < ingredients["cheese"]:
            print("Sorry, there is not enough cheese.")
            return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("How many whole dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        return (dollars * 100 + half_dollars * 50 + quarters * 25 + nickels * 5)/100

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that is not enough money. Money refunded.")
            return False
        if coins > cost:
            print(f"Here is ${coins - cost:.2f} in change")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

#Function which completes the necessary steps in the transaction
def complete_transaction(size):
    if not machine.check_resources(recipes[size]["ingredients"]):
        return

    if not machine.transaction_result(machine.process_coins(), recipes[size]["cost"]):
        return

    machine.make_sandwich(size, recipes[size]["ingredients"])

user_input = None

while True:
    user_input = input("What would you like? (small/medium/large/off/report): ")
    if user_input == "small" or user_input == "medium" or user_input == "large":
        complete_transaction(user_input)
    elif user_input == "report":
        print(f"Bread: {machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {machine.machine_resources['cheese']} pound(s)")
    elif user_input == "off":
        exit()
    else:
        user_input = input("Please try again.")