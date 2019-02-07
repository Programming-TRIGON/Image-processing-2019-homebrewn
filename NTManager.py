from networktables import NetworkTables
import main


class NTManager:

    def __init__(self, table_key, robot_ip='10.59.90.2'):
        NetworkTables.initialize(robot_ip)
        self.nt = NetworkTables.getTable(table_key)
        self.nt.addEntryListener(main.nt_settings_listener)

    def put_number(self, entry_key, value):
        self.nt.putNumber(entry_key, value)

    def get_number(self, entry_key, default):
        return self.nt.getNumber(entry_key, default)

    def put_string(self, entry_key, value):
        self.nt.putString(entry_key, value)

    def get_string(self, entry_key, default):
        return self.nt.getString(entry_key, default)

