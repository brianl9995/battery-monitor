import datetime

import rumps

import ioreg


class App(rumps.App):
    site_name = "MB"

    def __init__(self):
        super(App, self).__init__("")
        self.menu.add(rumps.MenuItem(title='Refresh Time'))

    @rumps.timer(60)
    def refresh_status(self, sender):
        """ Refresh Battery information on menu. """
        self.menu["Refresh Time"].title = (
            f"Updated: "
            f"{datetime.datetime.now().strftime('%m-%d %H:%M:%S')}"
        )
        percent = ioreg.get_ioreg_battery_percent()
        self.title = "🖱️%d%%" % percent


if __name__ == "__main__":
    myapp = App()
    myapp.run()
