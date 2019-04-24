from SignalValue import SignalValue

class SignalSet:
    def __init__(self, forward:SignalValue=None, right:SignalValue=None, back:SignalValue=None, left:SignalValue=None):
        self.forward = forward if forward else SignalValue()
        self.right = right if right else SignalValue()
        self.back = back if back else SignalValue()
        self.left = left if left else SignalValue()

    @staticmethod
    def build_from_json(json_data:dict):
        forward = SignalValue.build_from_json(json_data["forward"])
        right = SignalValue.build_from_json(json_data["right"])
        back = SignalValue.build_from_json(json_data["back"])
        left = SignalValue.build_from_json(json_data["left"])
        return SignalSet(forward=forward, right=right, back=back, left=left)

    @staticmethod
    def distance(a, b):
        distance_val = 0
        distance_val += SignalValue.distance(a.forward, b.forward) ** 2
        distance_val += SignalValue.distance(a.right, b.right) ** 2
        distance_val += SignalValue.distance(a.back, b.back) ** 2
        distance_val += SignalValue.distance(a.left, b.left) ** 2
        return distance_val ** 0.5

    def __str__(self):
        return """
f:{}
r:{}
b:{}
l:{}
            """.format(self.forward, self.right, self.back, self.left)
