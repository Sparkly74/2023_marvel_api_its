class Character:
    def __init__(self, id, name, description, image, extension_image):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.extension_image = extension_image
    @classmethod # Décorateur pour définir une méthode de classe permettant la représentation cls qui renvoie à la classe elle-même
    def from_dict(cls, data): # Définir une méthode de classe pour créer une instance de la classe Character depuis un dictionnaire. cls est convention de nommage tout comme self pour les méthodes d'instance
        return cls(
            id = data['id'],
            name = data['name'],
            description = data['description'],
            image = data['thumbnail']['path'],
            extension_image = data['thumbnail']['extension']
        )

# data = {
#     'id': 1011334,
#     'name' : 'Iron Man',
#     'description' : 'descrition',
#     'image' : 'image',
#     'extension_image' : 'jpg'
# }
# character = Character.from_dict(data)
# Character(id=1011334, name="Iron Man", description="descrition", image="image", extension_image="jpg")
# Character(data['id'], data['name'], data['description'], data['image'], data['extension_image'])
# print(character.id)