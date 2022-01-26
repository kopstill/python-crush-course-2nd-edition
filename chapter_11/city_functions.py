def get_city_country_name(city_name, country_name, population=''):
    if population:
        city_country_name = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        city_country_name = f"{city_name.title()}, {country_name.title()}"
    return city_country_name
