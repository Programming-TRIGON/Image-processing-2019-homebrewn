from networktables import NetworkTables


class NTManager:
    nt = None

    def __init__(self, table_key, robot_ip='10.59.90.2'):
        NetworkTables.initialize(robot_ip)
        self.nt = NetworkTables.getTable(table_key)

