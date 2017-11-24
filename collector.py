import requests
from bs4 import BeautifulSoup

url = "http://www.calforlife.com/th/calories/egg-whole-raw-fresh"

response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

dataLeft = html_soup.find_all('p', class_='nut-left')
calories = dataLeft[0].span.text
totalFat = dataLeft[1].span.text
satFat = dataLeft[2].span.text
cholesterol = dataLeft[3].span.text
Na = dataLeft[4].span.text
K = dataLeft[5].span.text
totalCarb = dataLeft[6].span.text
dietFib = dataLeft[7].span.text
protein = dataLeft[8].span.text

dataRight = html_soup.find_all('p', class_='nut-right')
calFat = dataRight[0].span.text
perTotalFat = dataRight[1].text
perSatFat = dataRight[2].text
perChol = dataRight[3].text
perNa = dataRight[4].text
perK = dataRight[5].text
perTotalCarb = dataRight[6].text
perDietFib = dataRight[7].text
perProtein = dataRight[8].text
vitA = dataRight[9].text
vitC = dataRight[10].text
Ca = dataRight[11].text
Fe = dataRight[12].text
vitD = dataRight[13].text
vitB6 = dataRight[14].text
vitB12 = dataRight[15].text
Mg = dataRight[16].text

fatsugar = html_soup.find_all('p', class_='nut-indent nut-sm-line')
polyFat = fatsugar[0].span.text
monoFat = fatsugar[1].span.text
transFat = fatsugar[2].span.text
sugar = fatsugar[3].span.text

servingSize = html_soup.find_all('p', class_='nut-big-line')[0].span.text

print('Serving Size: ', servingSize)
print('Calories: ', calories)
print('Calories from Fat: ', calFat)
print('Total Fat: ', totalFat)
print('% Total Fat: ', perTotalFat)
print('Saturated Fat: ', satFat)
print('% Saturated Fat: ', perSatFat)
print('Polyunsaturated Fat: ', polyFat)
print('Monounsaturated Fat: ', monoFat)
print('Trans Fat: ', transFat)
print('Cholesterol: ', cholesterol)
print('% Cholesterol: ', perChol)
print('Sodium: ', Na)
print('% Sodium: ', perNa)
print('Potassium: ', K)
print('% Potassium: ', perK)
print('Total Carbohydrate: ', totalCarb)
print('% Total Carbohydrate: ', perTotalCarb)
print('Dietary Fiber: ', dietFib)
print('% Dietary Fiber: ', perDietFib)
print('Sugar: ', sugar)
print('Protein: ', protein)
print('% Protein: ', perProtein)
print('Vitamin A: ', vitA)
print('Vitamin C: ', vitC)
print('Calcium: ', Ca)
print('Iron: ', Fe)
print('Vitamin D: ', vitD)
print('Vitamin B6: ', vitB6)
print('Vitamin B12: ', vitB12)
print('Magnesium: ', Mg)
