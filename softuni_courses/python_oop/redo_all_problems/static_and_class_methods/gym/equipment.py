class Equipment:
    ID = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.generate_it() - 1

    @staticmethod
    def generate_it():
        Equipment.ID += 1
        return Equipment.ID

    @staticmethod
    def get_next_id():
        return Equipment.ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
