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

        for student in root:
            fio = student.tag
            score = []
            for subject in student:
                name_subject = subject.tag
                score_subject = int(subject.text)
                score.append((name_subject, score_subject))
            self.students[fio] = score

        return self.students
