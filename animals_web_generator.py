import requests


def load_data(): 
    """ Fetching data from API """
    name = 'fox'
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'b4+kesU9iqd0ckcpssjDXg==yP3BD3c4OBxMBpNc'})
    data = response.json()
    return data


def read_html(file_path):
    """ Read an HTML file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def serialize_animal(animal_obj):
    """ Serialization of a single animal object """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title" style="margin: 10px;">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">\n'
    output += '<ul>\n'
    output += f'<li><strong>Genus:</strong> {animal_obj["taxonomy"].get("genus")}</li>\n'
    output += f'<li><strong>Diet:</strong> {animal_obj["characteristics"].get("diet")}</li>\n'
    output += f'<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    output += f'<li><strong>Type:</strong> {animal_obj["characteristics"].get("type")}</li>\n'
    output += f'<li><strong>Color:</strong> {animal_obj["characteristics"].get("color")}</li>\n'
    output += f'<li><strong>Skin type:</strong> {animal_obj["characteristics"].get("skin_type")}</li>\n'
    output += '</ul>'
    output += '</div>'
    output += '</li>\n'
    return output
    
    
def get_animal_info(data):
    """ Displays name, diet, location and type of the animal from the data """
    output = ""
    for animal in data:   
        output += serialize_animal(animal) 
    return output


def new_html_data(file_path, animals_data): 
    """ Creating a new HTML file with the necessery information """
    with open(file_path, "w", encoding="utf-8") as handle:
        html_data = read_html("animals_template.html")
        animals_info = get_animal_info(animals_data)
        new = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_info)
        return handle.write(new)

    
def error_page(file_path):
    """ Renders an error page """
    with open(file_path, "w", encoding="utf-8") as handle:
        output = ''
        output += '<li class="cards__item">\n'
        output += '<div class="card__title" style="margin: 10px;">Cards are not found!</div>\n'
        output += '</div>'
        output += '</li>\n'

        html_data = read_html("animals_template.html")
        new = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
        return handle.write(new)
    
    
def main(): 
    """ Main logic of the program """
    animals_data = load_data()

    if animals_data:
        print(new_html_data("animals.html", animals_data))
    else:
        print("Invalid skin type")
        print(error_page("animals.html"))


if __name__ == "__main__":
    main()
    
