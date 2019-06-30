from collections import defaultdict
from datetime import datetime


class Node(object):
    value = None
    ttl = None

    def __init__(self, value):
        self.value = value
        self.ttl = datetime.now()


class LRUCache(object):
    dwcache = None
    capacity = -1
    ddlist = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.dwcache = defaultdict(str)
        self.ddlist = list()

    def get(self, key):
        if key not in self.dwcache:
            return None

        node = self.dwcache.get(key=key)

        self.ddlist.remove(node)
        node.ttl = datetime.now()
        self.ddlist.append(node)

        return node.value

    def set(self, key, value):
        if key in self.dwcache:
            node = self.dwcache.get(key=key)
            self.ddlist.remove(node)
            node.ttl = datetime.now()
            self.ddlist.append(node)
        else:
            if len(self.dwcache) >= self.capacity:
                self.ddlist.remove(self.ddlist.pop(0))

            node = Node(value)
            self.dwcache[key] = node
            self.ddlist.append(node)

    def save(self, filepath):
        filename = filepath + '/dump' + '_' + str(datetime.datetie.now()) + '.rdb'
        with open(filename, 'w') as fd:
            for key, value in self.dwcache:
                fd.write("{key}=>{value}\n".format(key=key, value=value))

    def restore(self, filepath):
        with open(filepath, 'r') as fd:
            lines = fd.read()
            for line in lines:
                key, value = line.split('=>')
                self.set(key=key, value=eval(value))

