# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import abc

class Template(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def key(self):
        pass

    @abc.abstractmethod
    def hash(self):
        pass

class HashTable(object):
    class ElementStatus(object):
        Empty = 0
        Deleted = 1
        Full = 2
    def __init__(self, size=16, hash_method=None):
        self.size = size
        self.array_data = [None] * size
        self.array_status = [0] * size
        self.hash_method = hash_method
    
    def insert(self, t):
        i = 0
        while i < self.size:
            j = self.hash_method(self.size, t, i)
            if self.array_status[j] != self.ElementStatus.Full:
                self.array_data[j] = t
                self.array_status[j] = self.ElementStatus.Full
                return j
            i += 1
        return -1

    def search(self, t):
        i = 0
        while i < self.size:
            j = self.hash_method(self.size, t, i)
            if self.array_status[j] == self.ElementStatus.Empty:
                return -1
            elif self.array_status[j] == self.ElementStatus.Full:
                if self.array_data[j].key() == t.key():
                    return j
            i += 1
        return -1

    def delete(self, t):
        i = 0
        while i < self.size:
            j = self.hash_method(self.size, t, i)
            if self.array_status[j] == self.ElementStatus.Empty:
                return -1
            elif self.array_status[j] == self.ElementStatus.Full:
                if self.array_data[j].key() == t.key():
                    return j
            i += 1
        return -1

def linear_probe(size, t, i):
    return (t.hash()+i)%size

def quadratic_probe(size, t, i):
    return (t.hash()%size + i * i)%size

def double_probe_1(size, t, i):
    """
    size为素数，
    """
    pass

def double_probe_2(size, t, i):
    pass

class StringTemplate(Template):
    def __init__(self, text):
        self.text = text

    def key(self):
        return self.text

    def hash(self):
        return hash(self.text)

def test_linear_hash():
    print("test linear hash")
    s1 = StringTemplate(text="abc")
    s2 = StringTemplate(text="abc")
    s3 = StringTemplate(text="abc")
    
    table = HashTable(hash_method=linear_probe)
    i1 = table.insert(s1)
    print(i1)
    i2 = table.insert(s2)
    print(i2)
    i3 = table.insert(s3)
    print(i3)

    for i in range(0, len(table.array_data)):
        print("index: %d, data: %s" % (i, table.array_data[i]))

def test_quadratic_hash():
    print("test linear hash")
    s1 = StringTemplate(text="abc")
    s2 = StringTemplate(text="abc")
    s3 = StringTemplate(text="abc")
    
    table = HashTable(hash_method=quadratic_probe)
    i1 = table.insert(s1)
    print(i1)
    i2 = table.insert(s2)
    print(i2)
    i3 = table.insert(s3)
    print(i3)

    for i in range(0, len(table.array_data)):
        print("index: %d, data: %s" % (i, table.array_data[i]))
if __name__ == "__main__":
    test_linear_hash()
    test_quadratic_hash()
    