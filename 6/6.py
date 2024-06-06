from bs4 import BeautifulSoup

print("ПІБ: Бондар Олексій Олегович")
print("Група: І")

with open('сторінка.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

table_cells_content = []
table = soup.find('table')
if table:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        for cell in cells:
            cell_text = ' '.join(cell.stripped_strings)
            table_cells_content.append(cell_text)

print("\nВміст усіх комірок таблиці: ")
for content in table_cells_content:
    print(content)

filtered_table_content = [word for content in table_cells_content for word in content.split() if word.isalpha()]
print("\nТільки словоформи з вмісту таблиці: ")
for word in filtered_table_content:
    print(word)
