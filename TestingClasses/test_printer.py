from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):
    # setUp() will run for every method. For this reason, we don't have to type it
    # in every method.
    def setUp(self) -> None:
        self.printer = Printer(pages_per_s = 2.0, capacity =300)
    
    # If we want the setUp() method to run only once, we make it a class method.
    # I don't think this is true. The test_print_outside_capacity method returns
    # the same when I give 280 pages as an argument.
    # The setUpClass also does not come up in the intellisense.
    # @classmethod
    # def setUpClass(cls):
    #     cls.printer = Printer(pages_per_s = 2.0, capacity =300)
    
    def test_print_within_capacity(self):
        message = self.printer.print(25)
    
    # I believe the module unittest checks for the .assert methods.
    
    def test_print_outside_capacity(self):
        print(f" The printer capacity is right now {self.printer._capacity}.")
        with self.assertRaises(PrinterError):
            self.printer.print(301)
    
    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages =10
        expected = "The printer printed 10 pages in 5.00 seconds."
        result =self.printer.print(pages)
        self.assertEqual(result,expected)

    def test_print_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected ="The printer printed 11 pages in 3.67 seconds."
        result=fast_printer.print(pages)
        self.assertEqual(result,expected)

    def test_print_multiple_runs(self):
        self.printer.print(25)
        self.printer.print(75)
        self.printer.print(200)
    
    def test_printer_multuiple_runs_end_in_error(self):
        self.printer.print(25)
        self.printer.print(75)
        self.printer.print(200)

        with self.assertRaises(PrinterError):
            self.printer.print(1)