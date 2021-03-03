import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class CountryInfo:
    name: str
    cases: str
    deaths: str
    recovered: [int, str] = 'No data'


def get_information(url="https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data"):
    """
        DOCSTRING: Gets all statistics information from response content
        INPUT: URL link
        OUTPUT: hash table with another hash table in there like: Belarus: {Total : IntValue,
                                                                            Number of death : IntValue,
                                                                             etc...}
    """
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    table_header = dict()
    countries = soup.find('tbody').find_all('tr')
    for each in countries:
        text_presentation = each.text.split()[:-1]
        if 'No' in text_presentation:
            text_presentation = text_presentation[:-2]
            text_presentation.append('No data')
        name = ' '.join(text_presentation[:-3])
        bracket_index = name.find('[')
        if bracket_index > 0:
            name = name[:bracket_index]
        g = CountryInfo(name, text_presentation[-3], text_presentation[-2], text_presentation[-1])
        if name == 'Tanzania':
            break


if __name__ == '__main__':
    get_information()
