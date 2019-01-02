
from .node_host import nodeHost

class nodeSubNet():
    def __init__(self, node, ip, mask, ifindex, ifname, hosts):
        self.node = node
        self.ip = ip
        self.mask = mask
        self.ifindex = ifindex
        self.ifname = ifname
        self.hosts = []

        self.__add_host(hosts)

    def __add_host(self, hosts):
        for ip, mac in hosts:
            self.hosts.append(nodeHost(ip, mac))
