from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):
    # setUp() will run for every method. For thos reason, we don't have to type it
    # in every method.
    def setUp(self) -> None:
        self.printer = Printer(pages_per_s = 2.0, capacity =300)
    
    # If we want the setUp() method to run only once, we make it a class method.
    @classmethod
    def setUpClass(cls):
        cls.printer = Printer(pages_per_s = 2.0, capacity =300)
    
    def test_print_within_capacity(self):
        message = self.printer.print(25)
        self.assertEqual("The printer printed 25 pages in 12.50 seconds.", message)
    
    # I believe the module unittest cheks for the .assert methods.