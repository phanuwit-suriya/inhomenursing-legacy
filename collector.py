import re
import time
import requests
from bs4 import BeautifulSoup

from database import insert_nutrition


def main():
    for num_page in range(1, 181):
        page_url = 'http://www.calforlife.com/th/calories/food/page{}'.format(
            num_page)
        page_response = requests.get(page_url)
        page_soup = BeautifulSoup(page_response.text, 'html.parser')
        links = page_soup.find_all('a', href=True)
        for num_link in range(30, 80):
            link = links[num_link]['href']
            if not 'http://www.calfirlife.com/th/calories/food/page' in link:
                url = link
                response = requests.get(url)
                html_soup = BeautifulSoup(response.text, 'html.parser')

                try:
                    name = html_soup.find_all(
                        'div', class_='bread-crumb')[0].contents[8].text
                    name = re.sub('[()]', '', name)
                    serving_size = html_soup.find_all(
                        'p', class_='nut-big-line')[0].span.text
                    if serving_size == '__':
                        serving_size = '0'
                except IndexError:
                    break

                calories, total_fat, sat_fat, cholesterol, sodium, potassium, total_carb, diet_fiber, protein = '0', '0', '0', '0', '0', '0', '0', '0', '0'

                data_left = html_soup.find_all('p', class_='nut-left')

                calories = data_left[0].span.text
                total_fat = data_left[1].span.text
                sat_fat = data_left[2].span.text
                cholesterol = data_left[3].span.text
                sodium = data_left[4].span.text
                potassium = data_left[5].span.text
                total_carb = data_left[6].span.text
                diet_fiber = data_left[7].span.text
                protein = data_left[8].span.text

                if calories == '__':
                    calories = '0'
                if total_fat == '__':
                    total_fat = '0'
                if sat_fat == '__':
                    sat_fat = '0'
                if cholesterol == '--':
                    cholesterol = '0'
                if sodium == '__':
                    sodium = '0'
                if potassium == '__':
                    potassium = '0'
                if total_carb == '__':
                    total_carb = '0'
                if diet_fiber == '--':
                    diet_fiber = '0'
                if protein == '__':
                    protein = '0'

                cal_fat, percent_total_fat, percent_sat_fat, percent_cholesterol, percent_sodium, percent_potassium, percent_total_carb, percent_diet_fiber, percent_protein = '0', '0', '0', '0', '0', '0', '0', '0', '0'

                data_right = html_soup.find_all('p', class_='nut-right')

                cal_fat = data_right[0].span.text
                percent_total_fat = data_right[1].text.strip("%")
                percent_sat_fat = data_right[2].text.strip("%")
                percent_cholesterol = data_right[3].text.strip("%")
                percent_sodium = data_right[4].text.strip("%")
                percent_potassium = data_right[5].text.strip("%")
                percent_total_carb = data_right[6].text.strip("%")
                percent_diet_fiber = data_right[7].text.strip("%")
                percent_protein = data_right[8].text.strip("%")

                if cal_fat == '__':
                    cal_fat = '0'
                if percent_total_fat == '__':
                    percent_total_fat = '0'
                if percent_sat_fat == '__':
                    percent_sat_fat = '0'
                if percent_cholesterol == '__':
                    percent_cholesterol = '0'
                if percent_sodium == '__':
                    percent_sodium = '0'
                if percent_potassium == '__':
                    percent_potassium = '0'
                if percent_total_carb == '__':
                    percent_total_carb = '0'
                if percent_diet_fiber == '__':
                    percent_diet_fiber = '0'
                if percent_protein == '__':
                    percent_protein = '0'

                poly_fat, mono_fat, trans_fat, sugar = '0', '0', '0', '0'

                fatsugar = html_soup.find_all(
                    'p', class_='nut-indent nut-sm-line')

                poly_fat = fatsugar[0].span.text
                mono_fat = fatsugar[1].span.text
                trans_fat = fatsugar[2].span.text
                sugar = fatsugar[3].span.text

                if poly_fat == '__':
                    trans_fat = '0'
                if mono_fat == '__':
                    mono_fat = '0'
                if trans_fat == '__':
                    trans_fat = '0'
                if sugar == '__':
                    sugar = '0'

                vit_a, vit_c, calcium, iron, vit_d, vit_b6, vit_b12, magnesium, thiamin, riboflavin = '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
                niacin, vit_e, vit_k, zinc, phosphorus = '0', '0', '0', '0', '0'

                data = html_soup.find_all(
                    'div', class_='nut-sm-line nut-50 cheight')

                for i in range(len(data)):
                    key = data[i].text
                    if not '_' in key:
                        value = data[i].span.text
                    if 'วิตามินเอ' in key:
                        vit_a = value
                    if 'วิตามินซี' in key:
                        vit_c = value
                    if 'แคลเซียม' in key:
                        calcium = value
                    if 'เหล็ก' in key:
                        iron = value
                    if 'วิตามืนดี' in key:
                        vit_d = value
                    if 'วิตามินบี 6' in key:
                        vit_b6 = value
                    if 'วิตามินบี 12' in key:
                        vit_b12 = value
                    if 'แมกนีเซียม' in key:
                        magnesium = value
                    if 'ไทอามิน' in key:
                        thiamin = value
                    if 'ไรโบพลาวิน' in key:
                        riboflavin = value
                    if 'ไนอาซิน' in key:
                        niacin = value
                    if 'วิตามินอี' in key:
                        vit_e = value
                    if 'วิตามินเค' in key:
                        vit_k = value
                    if 'ซิงค์' in key:
                        zinc = value
                    if 'ฟอสฟอรัส' in key:
                        phosphorus = value

                if vit_a == '__':
                    vit_a = '0'
                if vit_c == '__':
                    vit_c = '0'
                if calcium == '__':
                    calcium = '0'
                if iron == '__':
                    iron = '0'
                if vit_d == '__':
                    vit_d = '0'
                if vit_b6 == '__':
                    vit_b6 = '0'
                if vit_b12 == '__':
                    vit_b12 = '0'
                if magnesium == '__':
                    magnesium = '0'
                if thiamin == '__':
                    thiamin = '0'
                if riboflavin == '__':
                    riboflavin = '0'
                if niacin == '__':
                    niacin = '0'
                if vit_e == '__':
                    vit_e = '0'
                if vit_k == '__':
                    vit_k = '0'
                if zinc == '__':
                    zinc = '0'
                if phosphorus == '__':
                    phosphorus = '0'

                insert_nutrition(name, serving_size, calories, cal_fat, total_fat, sat_fat, poly_fat, mono_fat, trans_fat, cholesterol, sodium, potassium, total_carb, diet_fiber, sugar, protein, percent_total_fat, percent_sat_fat, percent_cholesterol,
                                 percent_sodium, percent_potassium, percent_total_carb, percent_diet_fiber, percent_protein, vit_a, vit_c, calcium, iron, vit_d, vit_b6, vit_b12, magnesium, thiamin, riboflavin, niacin, vit_e, vit_k, zinc, phosphorus)

        print('Page {}: Done!'.format(num_page))
