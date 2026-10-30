def describe_city(city, country = 'USA'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('London', 'England')
describe_city('new york')
describe_city('chicago')
describe_city(country = 'japan', city = 'Tokyo')