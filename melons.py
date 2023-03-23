"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from"""

    # Class attribute that could be use in the subclasses
    order_type = None
    tax = 0

    # 
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        # If melon species is christmas melon base price increase 1.5 times higher
        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        # If the order type is international and qty is less than 10, total price plus 3
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon order purchased by US gov"""

    order_type = "government"
    tax = 0
    
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        print("The inspection passed")


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
   
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
