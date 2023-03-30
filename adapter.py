class UsbCable:

    def __init__(self) -> None:
        self.is_plugged = False

    def plug_usb(self):
        self.is_plugged = True


class UsbPort:

    def __init__(self) -> None:
        self.port_available = True

    def plug(self, usb_cable):
        if self.port_available:
            usb_cable.plug_usb()
            self.port_available = False


class MicroUsbCable:

    def __init__(self) -> None:
        self.is_plugged = False

    def plug_micro_usb(self):
        self.is_plugged = True


class MicroToUsbAdapter(UsbCable):

    def __init__(self, micro_usb_cable) -> None:
        super().__init__()
        self.micro_usb_cable = micro_usb_cable

    def plug_usb(self):
        super().plug_usb()
        self.micro_usb_cable.plug_micro_usb()


if __name__ == '__main__':
    usb_cable_test = UsbCable()
    usb_port = UsbPort()
    usb_port.plug(usb_cable_test)

    micro_to_usb_adapter = MicroToUsbAdapter(MicroUsbCable())
    usb_port.plug(micro_to_usb_adapter)
