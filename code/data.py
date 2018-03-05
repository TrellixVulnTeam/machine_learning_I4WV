import pandas
import os

from enum import Enum

DATA_DIR = os.path.join('..','data')

#######################################################################
class DataSets(Enum):
    EX0 = 'ex0'
    EX1 = 'ex1'

#######################################################################
def data_dir():
    return DATA_DIR
