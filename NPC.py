class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def interact(self):
        pass  # Override this method in subclasses

    def offer_quest(self):
        pass  # Override this method in subclasses

    def sell_items(self):
        pass  # Override this method in subclasses

    def buy_items(self):
        pass  # Override this method in subclasses

    def talk(self):
        pass  # Override this method in subclasses
