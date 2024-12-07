# -*- coding: utf-8 -*-
from src.QuartileRating import QuartileRating
import pytest

RatingsType = dict[str, float]


class TestQuartileRating:
    @pytest.fixture()
    def input_data(self) -> tuple[RatingsType, RatingsType]:
        data: RatingsType = {
            "Абрамов Петр Сергеевич": 70.3333,
            "Петров Игорь Владимирович": 94.0000,
            "Фёдоров Дмитрий Николаевич": 80.0000,
            "Попов Владимир Александрович": 75.0000,
            "Смирнов Алексей Викторович": 61.5000
        }

        students_Q1: RatingsType = {
            "Смирнов Алексей Викторович": 61.5000,
            "Абрамов Петр Сергеевич": 70.3333,
        }

        return data, students_Q1

    def test_init_quartile_rating(
            self, input_data: tuple[RatingsType, RatingsType]) -> None:
        quartile_rating = QuartileRating(input_data[0])
        assert input_data[0] == quartile_rating

    def test_quartile(
            self, input_data: tuple[RatingsType, RatingsType]) -> None:

        rating = QuartileRating(input_data[0])
        students_Q1 = rating.Quartile()
        assert students_Q1 == input_data[1]
