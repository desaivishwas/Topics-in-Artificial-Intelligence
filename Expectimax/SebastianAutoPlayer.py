# Automatic Sebastian game player
# B551 Spring 2021
# Ayush Sanghavi - sanghavi@iu.edu
# Vighnesh Kolhatkar - vkolhatk@iu.edu
# Vishwas Desai - visdesai@iu.edu
#
# Based on skeleton code by D. Crandall
##
#
# This is the file you should modify to create your new smart player.
# The main program calls this program three times for each turn.
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list
#      of dice indices that should be re-rolled.
#
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#
from re import search

from SebastianState import Dice
from SebastianState import Scorecard
import random


class SebastianAutoPlayer:

    def __init__(self):
        # initializing numbers and categories from SebastianState.py
        self.numbers = {"primis": 1, "secundus": 2, "tertium": 3, "quartus": 4, "quintus": 5, "sextus": 6}
        self.category1_6 = ["primis", "secundus", "tertium", "quartus", "quintus", "sextus"]
        self.category7_13 = ["company", "prattle", "squadron", "triplex", "quadrupla", "quintuplicatam", "pandemonium"]

    # Combo function referred from combos3 function given in Discussion 8 walk through : A mini game of Chance
    # This function takes in a list parameter and returns a list of the die combinations.
    def combo(self, lists):
        return [(d1, d2, d3, d4, d5) for d1 in lists[0] for d2 in lists[1] for d3 in lists[2] for d4 in lists[3] \
                for d5 in lists[4]]


    # This function will assign the category to the dies based on the condition given to us
    # As an when the dies roll, if it encounters and satisfies the condition of any category, it will choose the same.

    
    # The following function has been taken from Sebastian State python file, which was given to us as the starter code.
    # -----Function starts here-----
    
    def score_roll(self, dice, category, bonus):
        # dice = roll.dice
        counts = [dice.count(i) for i in range(1, 7)]
        # score = 0
        if category in self.numbers:
            score = counts[self.numbers[category] - 1] * self.numbers[category]
        elif category == "company":
            score = 40 if sorted(dice) == [1, 2, 3, 4, 5] or sorted(dice) == [2, 3, 4, 5, 6] else 0
        elif category == "prattle":
            score = 30 if (len(set([1, 2, 3, 4]) - set(dice)) == 0 or len(set([2, 3, 4, 5]) - set(dice)) == 0 or len(set([3, 4, 5, 6]) - set(dice)) == 0) else 0
        elif category == "squadron":
            score = 25 if (2 in counts) and (3 in counts) else 0
        elif category == "triplex":
            score = sum(dice) if max(counts) >= 3 else 0
        elif category == "quadrupla":
            score = sum(dice) if max(counts) >= 4 else 0
        elif category == "quintuplicatam":
            score = 50 if max(counts) == 5 else 0
        elif category == "pandemonium":
            score = sum(dice)
        # print(score)
        return score
#------------------------------------------------ Referred code taken from SebastianState.py ends here----------------------



    # There maybe instances where combination of 5 dies may satisfy more than one category, this function will
    # allow us to maximize and select our score from the all the categories that satisfy a single roll of 5 die combinations
    # We start with 3 combinations and then go upto the max category , i.e four a kind.
    
    # The following function was referred from this link : https://github.com/scheumann23/AI_Class_A2/blob/master/part1/SebastianAutoPlayer.py
    # -----Function starts here-----
    def final_score(self, dice, scorecard, bonus):
        one_to_six = [category for category in self.category1_6 if category not in scorecard]
        seven_to_thirtheen = [category for category in self.category7_13[:-1] if category not in scorecard]
        score_ = dict([(category, self.score_roll(dice, category, bonus)) for category in
                       one_to_six + seven_to_thirtheen if category not in scorecard])
        one_to_six_dict = dict([(category, score_[category]) for category in one_to_six])
        seven_to_thirtheen_dict = dict([(category, score_[category]) for category in seven_to_thirtheen])
        non_zero_one_to_six = dict(filter(lambda items: items[1] > 0, one_to_six_dict.items()))

        if "quintuplicatam" in seven_to_thirtheen and seven_to_thirtheen_dict["quintuplicatam"] == 50:
            return 50
        if "company" in seven_to_thirtheen and seven_to_thirtheen_dict["company"] == 40:
            return 40
        if "prattle" in seven_to_thirtheen and seven_to_thirtheen_dict["prattle"] == 30:
            return 30
        if "squadron" in seven_to_thirtheen_dict and seven_to_thirtheen_dict['squadron'] == 25:
            return 25

        for categories in one_to_six:
            # for the 3 re-rolls
            if one_to_six_dict[categories] >= self.numbers[categories] * 3:
                return one_to_six_dict[categories]

        if len(seven_to_thirtheen_dict) > 0:
            if max(seven_to_thirtheen_dict.items(), key=lambda i: i[1])[1] == 0:
                if len(non_zero_one_to_six) > 0:
                    return min(non_zero_one_to_six.items(), key=lambda i: i[1])[1]
                else:
                    return max(score_.items(), key=lambda i: i[1])[1]
            else:
                return max(score_.items(), key=lambda i: i[1])[1]
        else:
            return max(score_.items(), key=lambda i: i[1])[1]
    # ------------------------ Referred code ends here -------------------
    
    # The following function was referred from https://github.com/scheumann23/AI_Class_A2/blob/master/part1/SebastianAutoPlayer.py
    # ----function starts here----
    def final_category(self, dice, scorecard, bonus):
        one_to_six = [category for category in self.category1_6 if category not in scorecard]
        seven_to_thirtheen = [category for category in self.category7_13 if category not in scorecard]
        # print(one_to_six)
        # print(seven_to_thirtheen)
        score_ = dict([(category, self.score_roll(dice, category, bonus)) for category in
                       one_to_six + seven_to_thirtheen if category not in scorecard])
        one_to_six_dict = dict([(category, score_[category]) for category in one_to_six])
        seven_to_thirtheen_dict = dict([(category, score_[category]) for category in seven_to_thirtheen])
        non_zero_one_to_six = dict(filter(lambda items: items[1] > 0, one_to_six_dict.items()))

        if "quintuplicatam" in seven_to_thirtheen and seven_to_thirtheen_dict["quintuplicatam"] == 50:
            return "quintuplicatam"
        if "company" in seven_to_thirtheen and seven_to_thirtheen_dict["company"] == 40:
            return "company"
        if "prattle" in seven_to_thirtheen and seven_to_thirtheen_dict["prattle"] == 30:
            return "prattle"
        if "squadron" in seven_to_thirtheen_dict and seven_to_thirtheen_dict['squadron'] == 25:
            return "squadron"

        for categories in one_to_six:
            # Assigning a category after three rolls between primus to sextus
            if one_to_six_dict[categories] >= self.numbers[categories] * 3:
                return categories

        # Assigning a category from the seventh to thirteenth category
        if len(seven_to_thirtheen_dict) > 0:
            if max(seven_to_thirtheen_dict.items(), key=lambda i: i[1])[1] == 0:
                if len(non_zero_one_to_six) > 0:
                    return min(non_zero_one_to_six.items(), key=lambda i: i[1])[0]
                else:
                    return max(score_.items(), key=lambda i: i[1])[0]
            else:
                return max(score_.items(), key=lambda i: i[1])[0]
        else:
            return max(score_.items(), key=lambda i: i[1])[0]
# -----Referred Code ends here-------

    # expectaion_of_roll function referred from the Discussion 8 walkthrough : A mini game of Chance
    # Reference : https://www.geeksforgeeks.org/ml-expectation-maximization-algorithm/
    def expectaion_of_roll(self, roll, re_roll, scorecard, bonus):
        outcome = self.combo([((roll[dice],) if not re_roll[dice] else range(1, 7)) for dice in range(0, 5)])
        return sum([self.final_score(i, scorecard, bonus) for i in outcome]) / len(outcome)

    # max_strategy function referred from max_layer function given in Discussion 8 walkthrough : A mini game of Chance
    def max_strategy(self, roll, scorecard, bonus):
        max_score = max([(re_roll, self.expectaion_of_roll(roll, re_roll, scorecard, bonus)) for re_roll in
                         self.combo(((True, False),) * 5)], key=lambda item: item[1])
        # print(max_score)
        return [i for i in range(0, 5) if max_score[0][i]]

    def first_roll(self, dice, scorecard):
        return self.max_strategy(dice.dice, scorecard.scorecard,
                                 scorecard.bonusflag)  # always re-roll first die (blindly)

    def second_roll(self, dice, scorecard):
        return self.max_strategy(dice.dice, scorecard.scorecard,
                                 scorecard.bonusflag)  # always re-roll second and third dice (blindly)

    def third_roll(self, dice, scorecard):
        # returning a category after the third roll
        return self.final_category(dice.dice, scorecard.scorecard,
                                   scorecard.bonusflag)  # random.choice(list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())))
