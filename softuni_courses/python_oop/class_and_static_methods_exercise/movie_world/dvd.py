class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def validate_month(month):
        months = {1: "January",
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'July',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}

        return months[month]

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date = date.split('.')
        return cls(name, id, int(date[2]), DVD.validate_month(int(date[1])), age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}." \
               f" Status: {'rented' if self.is_rented else 'not rented'}"
