from .history import get_history

class key:
    def __init__(self,key):
        self.key = key
        
    def history(self, index, timeperiod):
        return (get_history(self.key, index, timeperiod))
