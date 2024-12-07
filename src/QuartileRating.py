# -*- coding: utf-8 -*-
RatingType = dict[str, float]


class QuartileRating:
    def __init__(self, data: RatingType) -> None:
        self.rating: RatingType = data

    def Quartile(self) -> RatingType:

        sorted_students_and_ratings = sorted(self.rating.items(), key=lambda x: x[1])
        sorted_ratings = [rating for _, rating in sorted_students_and_ratings]
        n = len(sorted_ratings)
        Q1 = sorted_ratings[n // 4]
        students_in_Q1 = {student: rating for student, rating in sorted_students_and_ratings if rating <= Q1}
        
        return students_in_Q1
