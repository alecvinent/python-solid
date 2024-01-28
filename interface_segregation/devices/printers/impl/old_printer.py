from interface_segregation.devices.printers.printer_device import PrinterDevice


class OldPrinter(PrinterDevice):
    def print(self, document):
        print(f'Printing {document}in black and white...')
