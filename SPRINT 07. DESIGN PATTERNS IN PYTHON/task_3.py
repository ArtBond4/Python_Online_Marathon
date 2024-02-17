class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"
    # pass

class Adapter:
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.objects_dict = {'name': obj, 'wheels': adapted_methods}

    def __getattr__(self, attr):
        if attr == 'name':
            return getattr(self.objects_dict[attr], attr)
        else:
            return self.objects_dict[attr][attr]

    def original_dict(self):
        print(self.objects_dict)
