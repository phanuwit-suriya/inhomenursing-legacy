import time
import requests
from bs4 import BeautifulSoup

import database

for numPage in range(1, 181):
    page_url = "http://www.calforlife.com/th/calories/food/page{}/".format(
        numPage)
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.text, 'html.parser')
    links = page_soup.find_all('a', href=True)
    for numLink in range(30, 80):
        link = links[numLink]['href']
        if not "http://www.calfirlife.com/th/calories/food/page" in link:
            url = link
            response = requests.get(url)
            html_soup = BeautifulSoup(response.text, 'html.parser')

            servingSize = html_soup.find_all(
                'p', class_='nut-big-line')[0].span.text

            if servingSize == '__':
                servingSize = '0'

            calories, totalFat, satFat, cholesterol, sodium, potassium, totalCarb, dietFiber, protein = '0', '0', '0', '0', '0', '0', '0', '0', '0'

            dataLeft = html_soup.find_all('p', class_='nut-left')

            calories = dataLeft[0].span.text
            totalFat = dataLeft[1].span.text
            satFat = dataLeft[2].span.text
            cholesterol = dataLeft[3].span.text
            sodium = dataLeft[4].span.text
            potassium = dataLeft[5].span.text
            totalCarb = dataLeft[6].span.text
            dietFiber = dataLeft[7].span.text
            protein = dataLeft[8].span.text

            if calories == '__':
                calories = '0'
            if totalFat == '__':
                totalFat = '0'
            if satFat == '__':
                satFat = '0'
            if cholesterol == '--':
                cholesterol = '0'
            if sodium == '__':
                sodium = '0'
            if potassium == '__':
                potassium = '0'
            if totalCarb == '__':
                totalCarb = '0'
            if dietFiber == '--':
                dietFiber = '0'
            if protein == '__':
                protein = '0'

            calFat, percent_totalFat, percent_satFat, percent_cholesterol, percent_sodium, percent_potassium, percent_totalCarb, percent_dietFiber, percent_protein = '0', '0', '0', '0', '0', '0', '0', '0', '0'

            dataRight = html_soup.find_all('p', class_='nut-right')

            calFat = dataRight[0].span.text
            percent_totalFat = dataRight[1].text.strip("%")
            percent_satFat = dataRight[2].text.strip("%")
            percent_cholesterol = dataRight[3].text.strip("%")
            percent_sodium = dataRight[4].text.strip("%")
            percent_potassium = dataRight[5].text.strip("%")
            percent_totalCarb = dataRight[6].text.strip("%")
            percent_dietFiber = dataRight[7].text.strip("%")
            percent_protein = dataRight[8].text.strip("%")

            if calFat == '__':
                calFat = '0'
            if percent_totalFat == '__':
                percent_totalFat = '0'
            if percent_satFat == '__':
                percent_satFat = '0'
            if percent_cholesterol == '__':
                percent_cholesterol = '0'
            if percent_sodium == '__':
                percent_sodium = '0'
            if percent_potassium == '__':
                percent_potassium = '0'
            if percent_totalCarb == '__':
                percent_totalCarb = '0'
            if percent_dietFiber == '__':
                percent_dietFiber = '0'
            if percent_protein == '__':
                percent_protein = '0'

            polyFat, monoFat, transFat, sugar = '0', '0', '0', '0'

            fatsugar = html_soup.find_all('p', class_='nut-indent nut-sm-line')

            polyFat = fatsugar[0].span.text
            monoFat = fatsugar[1].span.text
            transFat = fatsugar[2].span.text
            sugar = fatsugar[3].span.text

            if polyFat == '__':
                transFat = '0'
            if monoFat == '__':
                monoFat = '0'
            if transFat == '__':
                transFat = '0'
            if sugar == '__':
                sugar = '0'

            vitA, vitC, calcium, iron, vitD, vitB6, vitB12, Magnesium, thiamin, riboflavin = '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
            niacin, zinc, phosphorus, vitK = '0', '0', '0', '0'

            data = html_soup.find_all('div', class_='nut-sm-line nut-50 cheight')

            for i in range(len(data)):
                key = data[i].text
                if not '_' in key:
                    value = data[i].span.text
                if 'วิตามินเอ' in key:
                    vitA = value
                if 'วิตามินซี' in key:
                    vitC = value
                if 'แคลเซียม' in key:
                    calcium = value
                if 'เหล็ก' in key:
                    iron = value
                if 'วิตามืนดี' in key:
                    vitD = value
                if 'วิตามินบี 6' in key:
                    vitB6 = value
                if 'วิตามินบี 12' in key:
                    vitB12 = value
                if 'แมกนีเซียม' in key:
                    magnesium = value
                if 'ไทอามิน' in key:
                    thiamin = value
                if 'ไรโบพลาวิน' in key:
                    riboflavin = value
                if 'ไนอาซิน' in key:
                    niacin = value
                if 'ซิงค์' in key:
                    zinc = value
                if 'ฟอสฟอรัส' in key:
                    phosphorus = value
                if 'วิตามินเค' in key:
                    vitK = value

            if vitA == '__':
                vitA = '0'
            if vitC == '__':
                vitC = '0'
            if calcium == '__':
                calcium = '0'
            if iron == '__':
                iron = '0'
            if vitD == '__':
                vitD = '0'
            if vitB6 == '__':
                vitB6 = '0'
            if vitB12 == '__':
                vitB12 = '0'
            if magnesium == '__':
                magnesium = '0'
            if thiamin == '__':
                thiamin = '0'
            if riboflavin == '__':
                riboflavin = '0'
            if niacin == '__':
                niacin = '0'
            if zinc == '__':
                zinc = '0'
            if phosphorus == '__':
                phosphorus = '0'
            if vitK == '__':
                vitK = '0'

            database.insert_nutrition(servingSize, calories, calFat, totalFat, satFat, polyFat, monoFat, transFat, cholesterol, sodium, potassium, totalCarb, dietFiber, sugar,
                                      protein, percent_totalFat, percent_satFat, percent_cholesterol, percent_sodium, percent_potassium, percent_totalCarb, percent_dietFiber, percent_protein, vitA, vitC, calcium, iron, vitD, vitB6, vitB12, magnesium, thiamin, riboflavin, niacin, zinc, phosphorus, vitK)

    print('Page {}: Done!'.format(numPage))
