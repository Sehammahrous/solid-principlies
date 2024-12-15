class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self, document):
        pass

class Fax:
    def fax_document(self, document):
        pass

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")

class SimpleScanner(Scanner):
    def scan_document(self, document):
        print(f"Scanning: {document}")

class SimpleFax(Fax):
    def fax_document(self, document):
        print(f"Faxing: {document}")
              
simple_printer = SimplePrinter()
simple_scanner = SimpleScanner()
simple_faxing = SimpleFax()


simple_printer.print_document("Document1")
simple_scanner.scan_document("Document2")
simple_faxing.fax_document("Document3")
