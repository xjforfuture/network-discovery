
import nmap

class nodeHost():
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.host_name = None
        self.os_info = None

        self.__get_host_info()

    def __get_host_info(self):
        nm = nmap.PortScanner()
        try:
            nm.scan(str(self.ip), arguments="-O")

            self.host_name = nm[self.ip].hostname() if nm[self.ip].hostname() != "" else "unknown"
            if nm[self.ip].get('osclass'):
                for osclass in nm[self.ip]['osclass']:
                    self.os_info = f"Type : {osclass['type']}, Vendor : {osclass['vendor']}, " \
                                   + f"OS-Family : {osclass['osfamily']}, OS-Gen : {osclass['osgen']}"
                    break

            elif nm[self.ip].get('osmatch'):
                for osmatch in nm[self.ip]['osmatch']:
                    self.os_info = osmatch['name']

                    break

            elif nm[self.ip].get('fingerprint'):
                self.os_info = nm[self.ip]['fingerprint']

        except Exception:
            print(f"access host {self.ip} error")
