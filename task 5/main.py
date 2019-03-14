import game

# Creating streets

st_kozl = game.Street("Kozelnystska St.")
st_kozl.set_description("""A large modern building which appears to be the
                        Ukrainian Catholic University.""")

st_str = game.Street("Striyska St.")
st_str.set_description("A long wide street with a lovely park on the right side.")

st_shot = game.Street("Shota Rustaveli St.")
st_shot.set_description("""One of the city's oldest streets. The bus stops can
                            be dangerous sometimes.""")

st_sah = game.Street("Saharova St.")
st_sah.set_description("""A narrow but rather noisy street. Famous ShoCo Bakery
                        sits where the old store used to be.""")

st_frank = game.Street("Franka St.")
st_frank.set_description("""An impressive street which carries the name of one
                        of the most famous Ukrainian poets""")

# Linking streets

st_kozl.link_street(st_str, "north")
st_str.link_street(st_sah, "west")
st_str.link_street(st_shot, "east")
st_sah.link_street(st_frank, "south")
st_shot.link_street(st_frank, "north")
st_frank.link_street(st_koz, "south")

# Creating characters
