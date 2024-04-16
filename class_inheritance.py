# class_inheritance


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")

printer = Device("printer","usb")
print(printer)
printer.disconnect()

class printer(Device):
    def __init__(self,name, connected_by, capacity):
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remainig_pages = capacity
        
    def __str__(self,pages):
        return f"{super().__str__()} ({self.remaing_pages} pages remaninging)"
    
    def print(self, pages):
        if not self.connected:
            print("your printers is not connected:")
            return
        print(f"printing {pages} pages.")
        self.remaining_pages -= pages


printer = printer("printer", "usb", 500)
printer.print(20)
print(printer)

printer.disconnect()
printer.print(30)