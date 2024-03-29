class PrinterError(RuntimeError):
    pass

class Printer:
    def __init__(self, pages_per_s: float, capacity: int):
        self.pages_per_s = pages_per_s
        self._capacity = capacity
    
    def print(self, pages):
        if(pages > self._capacity):
            raise PrinterError("The printer does not have enough capacity for all of these pages.")
        
        self._capacity -= pages
    
        return f"The printer printed {pages} pages in {pages / self.pages_per_s:.2f} seconds."
