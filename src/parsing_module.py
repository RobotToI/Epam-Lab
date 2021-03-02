import requests
from bs4 import BeautifulSoup


def get_information(url="https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"):
    """
        DOCSTRING: Gets all statistics information from response content
        INPUT: URL link
        OUTPUT: hash table with another hash table in there like: Belarus: {Total : IntValue,
                                                                            Number of death : IntValue,
                                                                             etc...}
    """
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'lxml')
    table_header = dict()
    countries = soup.find('tbody')
    for each in countries.find_all('tr'):
        buff = each.text.split()
        if 'No' in buff:
            buff = buff[:-1]
        name = ' '.join(buff[:-4])
        have_brackets = name.find('[')
        if have_brackets > 0:
            name = name[:have_brackets]
        table_header[name] = tuple(buff[-4:-1])


if __name__ == '__main__':
    get_information()
