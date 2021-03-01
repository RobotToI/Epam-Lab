import requests
from bs4 import BeautifulSoup


def get_html_file(url, table_name='covid-statistics'):
    """
    DOCSTRING: Writes all HTML code to file
    INPUT: URL Address, and name of table
    OUTPUT: None, just existing file with HTML
    """
    response_html = requests.get(url)
    with open(str(table_name + '.html'), 'wb') as output_file:
        output_file.write(response_html.text.encode('UTF-8'))


def get_information(file_name):
    """
        DOCSTRING: Gets all statistics information from html file
        INPUT: name of html file
        OUTPUT: hash table with another hash table in there like: Belarus: {Total : IntValue,
                                                                            Number of death : IntValue,
                                                                             etc...}
    """
    with open(file_name, 'rb') as html:
        soup = BeautifulSoup(html, 'lxml')
    # table_header = dict()
    countries = soup.find('tbody', class_='ppcUXd')
    for each in countries.find_all('tr'):
        print(each.text)


if __name__ == '__main__':
    get_information('covid-statistics.html')
