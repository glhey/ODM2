__author__ = 'Stephanie'

import sys
import os

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(this_file))))
sys.path.insert(0, directory)

from ODM2 import service_base
import ODM2.Core.model as m
from ODMconnection import SessionFactory

class delete(service_base):
    def deleteVariable(self):
        return None