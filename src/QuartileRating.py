# -*- coding: utf-8 -*-
from CalcRating import CalcRating

RatingType = dict[str, float]


class QuartileRating:
    def __init__(self, data: RatingType) -> None:
        self.rating: RatingType = {}

    def Quartile(self) -> RatingType:

        return self.rating
