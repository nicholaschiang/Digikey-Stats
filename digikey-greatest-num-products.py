from selenium import webdriver
import time
import re
import csv

option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(options=option)
driver.get("https://www.digikey.com/products/en")
time.sleep(3)

#makes element list
elem_parents = driver.find_elements_by_class_name("catfiltersub")

elem_lists = []
for ind in range(0,len(elem_parents)):
    individual_elem = elem_parents[int(ind)].text
    elem_lists.append(individual_elem.split(r'\n'))

all_categories = [x[0].split('\n') for x in elem_lists]
final_list = [b for a in all_categories for b in a]
print(final_list)

p = re.compile(r'((?:\w|\W)+)(?:\s\()(\d+)(?:.*)')

with open('digikey_stats.csv', 'w') as csvfile:
    for item in final_list:
        m = p.match(item)
        writer = csv.writer(csvfile)
        category, num_items = m.groups()
        try:
            writer.writerow([category.replace("\"", "").strip(), num_items])
        except AttributeError:
            import pdb; pdb.set_trace()
