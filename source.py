# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:43:52 2020

@author: Neil McFarlane
"""

import pandas as pd
import re

class LootCalculator(object):
    
    def __init__(self, ref_nums, curse_cubes, heal_multiplier, heal_fixed):
        self.ref_nums = ref_nums
        self.curse_cubes = curse_cubes
        self.heal_multiplier = heal_multiplier
        self.heal_fixed = heal_fixed
        
    def card_data(self):
        '''
        Imports the data from card_data.csv. 
        Cleans the input from the player to remove artifacts such as letters, non-integer numbers and unnecessary spacing.
        Compares the reference numbers input from the player to the the data in card_data() and organises new data which represents the cards the player has for score calculation.
        '''
        
        card_df = pd.DataFrame()
        self.card_df = card_df
        self.card_df = pd.read_csv("card_data.csv")
        self.clean_ref_nums = []
        
        # Sub-method used in the main method which replaces common delimitters such as a comma, semicolon, or colon with a space.
        def delimitter_replace(string):
            string = re.sub(",", " ", string)
            string = re.sub(";", " ", string)
            string = re.sub(":", " ", string)
            return string
      
        # Sub-method used in the main method which splits the string of reference numbers input from the player to a series of items in a list.
        def split(string):
            li = list(string.split(" "))
            return li
        
        spaced_ref_nums = delimitter_replace(self.ref_nums)
        split_ref_nums = split(spaced_ref_nums)
        
        # For-loop which iterates through each item in the list split_ref_nums, checks if it is an integer and if it is then appends it to the list clean_ref_nums.
        for i in split_ref_nums:
            try:
                self.clean_ref_nums.append(int(i))
            except ValueError:
                continue
        
        self.clean_ref_nums.sort()
        
        # Takes the items from card_df which match the reference numbers input by the player.
        players_cards_df = self.card_df.loc[self.card_df["Reference Number"].isin(self.clean_ref_nums)] 
        self.players_cards_df = players_cards_df
    
    def curse_calculator(self):
        '''Calculates the gold which must be subtracted from the player's score due to having curse cubes which must be cured by the curse healer.'''
        
        # Simple calculation which solves the player's curse cost.
        curse_cost = (int(self.curse_cubes) * int(self.heal_multiplier)) + int(self.heal_fixed)
        
        print(curse_cost)

    def fixed_gold_calculator(self):
        '''Calculates the gold that the player has obtained from amulets, gold bags, jewels, crowns and skulls. This function does not consider multipliers or fixed bonuses.'''
    
        # Adds together all values from the column Gold Value to obtain the fixed gold.
        fixed_gold = self.players_cards_df["Gold Value"].sum(skipna = True)
        
        print(fixed_gold)
        
    def jewel_gold_calculator(self):
        '''Calculates the gold gained by having sets of jewels.'''   
        
        # In order to work with Jewel treasures, the Pandas dataframe jewel_df must be created.
        # jewel_df is simply a copy of players_cards_df with non Jewel treasures removed.
        jewel_df = self.players_cards_df.copy()
        index_names = jewel_df[jewel_df["Treasure Type"] != "Jewel"].index
        jewel_df.drop(index_names, inplace = True)
        
        # The total number of jewels is calculated by using index on the Pandas dataframe jewel_df.
        total_jewels = len(jewel_df.index)
        
        # Jewel scoring is done according to how many total jewels the player has, and this series of if and elif statements solves this.
        if total_jewels == 0:
            jewel_gold = 0
        elif total_jewels == 1:
            jewel_gold = 0
        elif total_jewels == 2:
            jewel_gold = 8
        elif total_jewels == 3:
            jewel_gold = 20
        elif total_jewels == 4:
            jewel_gold = 20
        elif total_jewels == 5:
            jewel_gold = 28
        elif total_jewels == 6:
            jewel_gold = 40
        elif total_jewels == 7:
            jewel_gold = 40
        elif total_jewels == 8:
            jewel_gold = 48
        elif total_jewels == 9:
            jewel_gold = 60
        elif total_jewels == 10:
            jewel_gold = 60
        elif total_jewels == 11:
            jewel_gold = 68
        elif total_jewels == 12:
            jewel_gold = 80
        elif total_jewels == 13:
            jewel_gold = 80
        elif total_jewels == 14:
            jewel_gold = 88
        
        print(jewel_gold)
        

obj1 = LootCalculator("10 15 34 67", 8, 2, 5) 
obj2 = LootCalculator("15 18 32 78", 8, 2, 5) 

obj1.card_data()
obj1.curse_calculator()
obj1.fixed_gold_calculator()
obj1.jewel_gold_calculator()

