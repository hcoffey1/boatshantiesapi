from SignalValue import SignalValue

class Action:
    def __init__(self, rotation:float=0, drive:float=0, new_signal:SignalValue=None, sleep:int=0):
        self.rotation = rotation
        self.drive = drive
        self.new_signal = new_signal
        self.sleep = sleep

    @staticmethod
    def build_from_json(json_data:dict):
        return Action(rotation=json_data["rotation"], drive=json_data["drive"], new_signal=SignalValue.build_from_json(json_data["new_signal"]))

    def __str__(self):
        return """
rotation:   {}
drive:      {}
new_signal: {}
sleep:      {}
""".format(self.rotation, self.drive, self.new_signal, self.sleep)
