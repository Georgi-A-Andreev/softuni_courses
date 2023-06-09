from project2.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.5

    def reserve(self, number_of_people):
        price_for_reservation = PrivateBooth.PRICE_PER_PERSON * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True
