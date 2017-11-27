import requests
from bs4 import BeautifulSoup

class Nutrition:

    def __init__(self, calories, totalFat, satFat, cholesterol, sodium, potassium, totalCarb, dietFiber, protein, calFat, percent_totalFat, percent_satFat, percent_cholesterol, percent_sodium, percent_potassium, percent_totalCarb, percent_dietFiber, percent_protein, polyFat, monoFat, transFat, sugar, vitA, vitC, calcium, iron, vitD, vitB6, vitB12, Magnesium, thiamin, riboflavin):

        self.calories = calories
        self.totalFat = totalFat
        self.satFat = satFat
        self.cholesterol = cholesterol
        self.sodium = sodium
        self.potassium = potassium
        self.totalCarb = totalCarb
        self.dietFiber = dietFiber
        self.protein = protein
        self.calFat = calFat
        self.percent_totalFat = percent_totalFat
        self.percent_satFat = percent_satFat
        self.percent_cholesterol = percent_cholesterol
        self.percent_sodium = percent_sodium
        self.percent_potassium = percent_potassium
        self.percent_totalCarb = percent_totalCarb
        self.percent_dietFiber = percent_dietFiber
        self.percent_protein = percent_protein
        self.polyFat = polyFat
        self.monoFat = monoFat
        self.transFat = transFat
        self.sugar = sugar
        self.vitA = vitA
        self.vitC = vitC
        self.calcium = calcium
        self.iron = iron
        self.vitD = vitD
        self.vitB6 = vitB6
        self.vitB12 = vitB12
        self.magnesium = magnesium
        self.thiamin = thiamin
        self.riboflavin = riboflavin
        self.niacin = niacin
        self.zinc = zinc
        self.phosphorus = phosphorus
        self.vitK = vitK

    def checkNone():

