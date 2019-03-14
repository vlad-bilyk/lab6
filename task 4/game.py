class Room:

    # char_lst = []
    # item_lst = []

    def __init__(self, name):
        self.name = name

    def set_description(self, text):
        self.dscrp = text

    def link_room(self, room, side):
        self.link = [room, side]

    def set_character(self, char):
        self.char = char

    def set_item(self, item):
        self.item = item

    def get_details(self):
        return """You are in the {}.\nPeople in this room: {}\n
        Items in this room: {}""".format(self.name, self.get_character(), self.get_item())

    def get_character(self):
        try:
            return self.char
        except:
            return None

    def get_item(self):
        try:
            return self.item
        except:
            return None

    def move(self, direction):
        if direction in self.link:
            print(self.link[0])
            return self.link[0]


class Enemy:

    amount = 0

    def __init__(self, name, bio):
        self.name = name
        self.bio = bio

    def set_conversation(self, text):
        self.conv = text

    def set_weakness(self, item):
        self.wkns = item

    def describe(self):
        return self.bio

    def talk(self):
        return self.conv

    def fight(self, item):
        result = item == self.wkns
        if result:
            self.amount += 1
            return result

    def get_deafeated(self):
        return self.amount


class Item:

    def __init__(self, name):
        self.name = name

    def set_description(self, text):
        self.dscrp = text

    def describe(self):
        return self.dscrp

    def get_name(self):
        return self.name
