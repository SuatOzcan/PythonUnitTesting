class PrinterError(RuntimeError):
    pass

class Printer:
    def __init__(self, pages_per_s: int, capacity: int):
        self.pages_per_s = pages_per_s
        self._capacity = capacity
    
    def print(self, pages):
        if(pages > self._capacity):
            raise PrinterError("The printer does not have enpugh capacity for all of these pages.")
        
        self._capacity -= pages
    
        return f"The printer {pages} pages in {pages / pages_per_s:.2f}."
    
printer = Printer(3,10)
printer.print(11)