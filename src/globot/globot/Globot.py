import json

from copy import deepcopy
from random import random, choice
from typing import List

from Rule import Rule
from SignalSet import SignalSet

class Globot:
    def __init__(self, rules:List[Rule]=None, probabilistic=False, bottype=None, noise_pr=None, noise_int=0):
        self.noise_pr = noise_pr
        self.noise_int = noise_int
        self.rules = rules if rules else []
        self.bottype = bottype if bottype else "anonymous"

    @staticmethod
    def build_from_file(filename:str):
        rules = []
        with open(filename) as rule_file:
            data = json.load(rule_file)
            raw_rules = data["ruleset"]
            if "probabilistic" in data:
                probabilistic = data["probabilistic"]
            else:
                probabilistic = False
            for raw_rule in raw_rules:
                rules.append(Rule.build_from_json(json_data=raw_rule))
            if "bottype" in data:
                bottype = data["bottype"]
            else:
                bottype = None
        return Globot(rules=rules, probabilistic=probabilistic, bottype=bottype)

    def get_action(self, signal_set:SignalSet=None):
        min_dist = None
        closest_rule = None
        for rule in self.rules:
            dist = SignalSet.distance(rule.signal_set, signal_set)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                closest_rule = rule
        action = deepcopy(closest_rule.action)
        if self.noise_pr is not None:
            if random() < self.noise_pr:
                action.drive += choice(list(range(0, self.noise_int)))
                action.rotation += 90
        return action

    def __str__(self):
        globot_str = ""
        for rule in self.rules:
            globot_str += str(rule) + "\n"
        return globot_str
