# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ElementTree


class XML_TextDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ElementTree.parse(path)
        root = tree.getroot()

        return self.students
