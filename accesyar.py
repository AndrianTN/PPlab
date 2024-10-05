class Accessory:
    def __init__(self, accessorytype="Unknown"):
        self._accessorytype = accessorytype
    
    def description(self):
        return f"Accessory type: {self._accessorytype}"
