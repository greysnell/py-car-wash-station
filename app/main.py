from typing import List

class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: "Car") -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: "Car") -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0

    def serve_cars(self, cars: List["Car"]) -> float:
        total_price = sum(self.wash_single_car(car) for car in cars)
        return round(total_price, 1)

    def rate_service(self, rating: float) -> None:
        new_count = self.count_of_ratings + 1
        new_average = (
            self.average_rating * self.count_of_ratings + rating
        ) / new_count
        self.count_of_ratings = new_count
        self.average_rating = round(new_average, 1)

def test_car_wash_station(cars, wash_station, total_cost):
    income = wash_station.serve_cars(cars)
    assert round(income, 1) == total_cost, f"Income should equal to {total_cost}"

def test_rate_service(
    init_avg_rating, init_num_ratings, mark, result_avg_rating, result_num_ratings
):
    ws = CarWashStation(2, 9, init_avg_rating, init_num_ratings)
    ws.rate_service(mark)
    assert round(ws.average_rating, 1) == result_avg_rating, (
        f"'average_rating' should equal to {result_avg_rating}, "
        f"when initial 'average_rating' was {init_avg_rating}, "
        f"and initial 'count_of_ratings' was {init_num_ratings}"
    )

