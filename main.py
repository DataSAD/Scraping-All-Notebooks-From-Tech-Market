import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import openpyxl

# url we will use to get to the product page. we will add href to this url.
base_url = 'https://www.vatanbilgisayar.com/notebook'

# dictionary to save scraped data and then transform to pandas dataframe
notebooks_dict = {
    'notebook_name': [],
    'notebook_brand': [],
    'notebook_model': [],
    'product_code': [],
    'price': [],
    'currency': [],
    'cpu_brand': [],
    'cpu_gen': [],
    'cpu_tech': [],
    'cpu_no': [],
    'cpu_speed': [],
    'cpu_cores': [],
    'ram_capacity': [],
    'ram_type': [],
    'ram_speed': [],
    'monitor_size': [],
    'monitor_hz': [],
    'monitor_resolution': [],
    'monitor_type': [],
    'gpu_brand': [],
    'gpu_chipset': [],
    'disc_capacity': [],
    'disc_type': [],
    'os': [],
    'weight': []
}



last_page = False
page_number = 1

# loop for pages
while True:
    # if the previous page number is the last page number, break the loop.
    if last_page:
        break

    # format the page
    page_url = 'https://www.vatanbilgisayar.com/notebook/?page={}'.format(page_number)

    # get page content
    html_text = requests.get(page_url).text
    soup = BeautifulSoup(html_text, 'lxml')

    # if this is the last page, this is the final loop(next time, the if statement above will break the loop).
    if not soup.find('span', class_='icon-angle-right'):
        last_page = True

    # get the list of the products on that page
    notebooks = soup.find_all('div', class_='product-list--list-page')

    # loop for products on that page
    for notebook in notebooks:
        # get href attribute from a tag
        notebook_url = notebook.find('a')['href']

        # href string will be added to base url to get to the product page & we will add a string to see the technical specs.
        notebook_html_text = requests.get(base_url + notebook_url + '#urun-ozellikleri').text
        notebook_soup = BeautifulSoup(notebook_html_text, 'lxml')

        # if the content does not exist on the page, this will go to except and append None
        try:
            notebook_name = notebook_soup.find('h1', class_='product-list__product-name').text
            notebooks_dict['notebook_name'].append(notebook_name)
        except:
            notebooks_dict['notebook_name'].append('None')

        try:
            notebook_brand = notebook_soup.find_all('a', class_='bradcrumb-item')[3].text
            notebooks_dict['notebook_brand'].append(notebook_brand)
        except:
            notebooks_dict['notebook_brand'].append('None')

        try:
            notebook_model = notebook_soup.find_all('a', class_='bradcrumb-item')[4].text
            notebooks_dict['notebook_model'].append(notebook_model)
        except:
            notebooks_dict['notebook_model'].append('None')

        try:
            product_code = notebook_soup.find('div', class_='product-id')['data-productcode']
            notebooks_dict['product_code'].append(product_code)
        except:
            notebooks_dict['product_code'].append('None')

        try:
            price = notebook_soup.find('span', class_='product-list__price').text
            notebooks_dict['price'].append(price)
        except:
            notebooks_dict['price'].append('None')

        try:
            currency = notebook_soup.find('span', class_='product-list__currency').text
            notebooks_dict['currency'].append(currency)
        except:
            notebooks_dict['currency'].append('None')

        try:
            cpu_brand = notebook_soup.find('td', string='İşlemci Markası').find_next_sibling('td').p.text
            # if the content is there but marked as undefined(=Belirtilmemiş in Turkish) append None
            if cpu_brand == 'Belirtilmemiş':
                notebooks_dict['cpu_brand'].append('None')
            else:
                notebooks_dict['cpu_brand'].append(cpu_brand)
        except:
            notebooks_dict['cpu_brand'].append('None')

        try:
            cpu_gen = notebook_soup.find('td', string='İşlemci Nesli').find_next_sibling('td').p.text
            if cpu_gen == 'Belirtilmemiş':
                notebooks_dict['cpu_gen'].append('None')
            else:
                notebooks_dict['cpu_gen'].append(cpu_gen)
        except:
            notebooks_dict['cpu_gen'].append('None')

        try:
            cpu_tech = notebook_soup.find('td', string='İşlemci Teknolojisi').find_next_sibling('td').p.text
            if cpu_tech == 'Belirtilmemiş':
                notebooks_dict['cpu_tech'].append('None')
            else:
                notebooks_dict['cpu_tech'].append(cpu_tech)
        except:
            notebooks_dict['cpu_tech'].append('None')

        try:
            cpu_no = notebook_soup.find('td', string='İşlemci Numarası').find_next_sibling('td').p.text
            if cpu_no == 'Belirtilmemiş':
                notebooks_dict['cpu_no'].append('None')
            else:
                notebooks_dict['cpu_no'].append(cpu_no)
        except:
            notebooks_dict['cpu_no'].append('None')

        try:
            cpu_speed = notebook_soup.find('td', string='İşlemci Hızı').find_next_sibling('td').p.text
            if cpu_speed == 'Belirtilmemiş':
                notebooks_dict['cpu_speed'].append('None')
            else:
                notebooks_dict['cpu_speed'].append(cpu_speed)
        except:
            notebooks_dict['cpu_speed'].append('None')

        try:
            cpu_cores = notebook_soup.find('td', string='İşlemci Çekirdek Sayısı').find_next_sibling('td').p.text.split(' ')[0]
            if cpu_cores == 'Belirtilmemiş':
                notebooks_dict['cpu_cores'].append('None')
            else:
                notebooks_dict['cpu_cores'].append(cpu_cores)
        except:
            notebooks_dict['cpu_cores'].append('None')

        try:
            ram_capacity = notebook_soup.find('td', string='Ram (Sistem Belleği)').find_next_sibling('td').p.text
            if ram_capacity == 'Belirtilmemiş':
                notebooks_dict['ram_capacity'].append('None')
            else:
                notebooks_dict['ram_capacity'].append(ram_capacity)
        except:
            notebooks_dict['ram_capacity'].append('None')

        try:
            ram_type = notebook_soup.find('td', string='Ram Tipi').find_next_sibling('td').p.text
            if ram_type == 'Belirtilmemiş':
                notebooks_dict['ram_type'].append('None')
            else:
                notebooks_dict['ram_type'].append(ram_type)
        except:
            notebooks_dict['ram_type'].append('None')

        try:
            ram_speed = notebook_soup.find('td', string='Ram Hafıza Bus Hızı').find_next_sibling('td').p.text
            if ram_speed == 'Belirtilmemiş':
                notebooks_dict['ram_speed'].append('None')
            else:
                notebooks_dict['ram_speed'].append(ram_speed)
        except:
            notebooks_dict['ram_speed'].append('None')

        try:
            monitor_size = notebook_soup.find('td', string='Ekran Boyutu').find_next_sibling('td').p.text
            if monitor_size == 'Belirtilmemiş':
                notebooks_dict['monitor_size'].append('None')
            else:
                notebooks_dict['monitor_size'].append(monitor_size)
        except:
            notebooks_dict['monitor_size'].append('None')

        try:
            monitor_hz = notebook_soup.find('td', string='Ekran Yenileme Hızı').find_next_sibling('td').p.text
            if monitor_hz == 'Belirtilmemiş':
                notebooks_dict['monitor_hz'].append('None')
            else:
                notebooks_dict['monitor_hz'].append(monitor_hz)
        except:
            notebooks_dict['monitor_hz'].append('None')

        try:
            monitor_resolution = notebook_soup.find('td', string='Çözünürlük (Piksel)').find_next_sibling('td').p.text
            if monitor_resolution == 'Belirtilmemiş':
                notebooks_dict['monitor_resolution'].append('None')
            else:
                notebooks_dict['monitor_resolution'].append(monitor_resolution)
        except:
            notebooks_dict['monitor_resolution'].append('None')

        try:
            monitor_type = notebook_soup.find('td', string='Monitör Tipi').find_next_sibling('td').p.text
            if monitor_type == 'Belirtilmemiş':
                notebooks_dict['monitor_type'].append('None')
            else:
                notebooks_dict['monitor_type'].append(monitor_type)
        except:
            notebooks_dict['monitor_type'].append('None')

        try:
            gpu_brand = notebook_soup.find('td', string='Ekran Kartı Chipset Marka').find_next_sibling('td').p.text
            if gpu_brand == 'Belirtilmemiş':
                notebooks_dict['gpu_brand'].append('None')
            else:
                notebooks_dict['gpu_brand'].append(gpu_brand)
        except:
            notebooks_dict['gpu_brand'].append('None')

        try:
            gpu_chipset = notebook_soup.find('td', string='Ekran Kartı Chipseti').find_next_sibling('td').p.text
            if gpu_chipset == 'Belirtilmemiş':
                notebooks_dict['gpu_chipset'].append('None')
            else:
                notebooks_dict['gpu_chipset'].append(gpu_chipset)
        except:
            notebooks_dict['gpu_chipset'].append('None')

        try:
            disc_capacity = notebook_soup.find('td', string='Disk Kapasitesi').find_next_sibling('td').p.text
            if disc_capacity == 'Belirtilmemiş':
                notebooks_dict['disc_capacity'].append('None')
            else:
                notebooks_dict['disc_capacity'].append(disc_capacity)
        except:
            notebooks_dict['disc_capacity'].append('None')

        try:
            disc_type = notebook_soup.find('td', string='Disk Türü').find_next_sibling('td').p.text
            if disc_type == 'Belirtilmemiş':
                notebooks_dict['disc_type'].append('None')
            else:
                notebooks_dict['disc_type'].append(disc_type)
        except:
            notebooks_dict['disc_type'].append('None')

        try:
            os = notebook_soup.find('td', string='İşletim Sistemi').find_next_sibling('td').p.text
            if os == 'Belirtilmemiş':
                notebooks_dict['os'].append('None')
            else:
                notebooks_dict['os'].append(os)
        except:
            notebooks_dict['os'].append('None')

        try:
            weight = notebook_soup.find('td', string='Cihaz Ağırlığı').find_next_sibling('td').p.text
            if weight == 'Belirtilmemiş':
                notebooks_dict['weight'].append(weight)
            else:
                notebooks_dict['weight'].append(weight)
        except:
            notebooks_dict['weight'].append('None')

    page_number += 1


# transform our dictionary to pandas dataframe
df = pd.DataFrame(notebooks_dict)

# save the data in different formats using pandas
df.to_csv('notebooks.csv')
df.to_excel('notebooks.xlsx')
df.to_json('notebooks.json')


















