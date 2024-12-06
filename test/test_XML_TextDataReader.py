# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XML_TextDataReader import XML_TextDataReader


class TestXMLTextDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '''<?xml version="1.0" encoding="UTF-8" ?>
                <root>
                    <Валентин_Иван_Фёдорович>
                        <программирование>73</программирование>
                        <география>81</география>
                    </Валентин_Иван_Фёдорович>
                    <Семёнов_Петр_Петрович>
                        <английский_язык>93</английский_язык>
                        <физика>91</физика>
                    </Семёнов_Петр_Петрович>
                </root>'''
        data = {
            "Валентин_Иван_Фёдорович": [
                ("программирование", 73), ("география", 81),
            ],
            "Семёнов_Петр_Петрович": [
                ("русский_язык", 93), ("литература", 91)
            ],
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(
        self, file_and_data_content: tuple[str, DataType], tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding="utf-8")
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XML_TextDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
