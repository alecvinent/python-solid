from interface_segregation.devices.faxes.fax_device import FaxDevice
from interface_segregation.devices.printers.printer_device import PrinterDevice
from interface_segregation.devices.scanners.scanner_device import ScannerDevice


class NewPrinter(PrinterDevice, FaxDevice, ScannerDevice):
    def print(self, document):
        print(f'Printing {document} in color...')

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
