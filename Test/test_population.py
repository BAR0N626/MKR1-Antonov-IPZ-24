def test_population_data():
    with open("population.txt", "r") as file:
        population_data = {}
        for line in file:
            data = line.strip().split(", ")
            country = data[0]
            year = int(data[1])
            population = int(data[2])
            if country in population_data:
                population_data[country].append((year, population))
            else:
                population_data[country] = [(year, population)]

        # Test that the population data dictionary has the correct keys
        assert set(population_data.keys()) == set(['Ukraine', 'USA', 'Poland'])

        # Test that the population data dictionary has the correct number of entries for each country
        assert len(population_data['Ukraine']) == 3
        assert len(population_data['USA']) == 3
        assert len(population_data['Poland']) == 3

        # Test that the population data for Ukraine is correct
        ukraine_data = population_data['Ukraine']
        assert ukraine_data[0] == (2020, 44000000)
        assert ukraine_data[1] == (2021, 43900000)
        assert ukraine_data[2] == (2022, 43800000)

        # Test that the population data for the USA is correct
        usa_data = population_data['USA']
        assert usa_data[0] == (2020, 330000000)
        assert usa_data[1] == (2021, 332000000)
        assert usa_data[2] == (2022, 334000000)

        # Test that the population data for Poland is correct
        poland_data = population_data['Poland']
        assert poland_data[0] == (2020, 1400000000)
        assert poland_data[1] == (2021, 1399000000)
        assert poland_data[2] == (2022, 1398000000)

    # Test the population change calculations for each country
    assert calculate_population_change(population_data['Ukraine']) == [-1000000, -1000000]
    assert calculate_population_change(population_data['USA']) == [2000000, 2000000]
    assert calculate_population_change(population_data['Poland']) == [-10000000, -10000000]


def calculate_population_change(country_data):
    population_change = []
    for i in range(1, len(country_data)):
        year1, pop1 = country_data[i-1]
        year2, pop2 = country_data[i]
        population_change.append(pop2 - pop1)
    return population_change
