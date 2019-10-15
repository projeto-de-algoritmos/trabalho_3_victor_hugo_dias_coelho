from PIL import ImageTk, Image

IMGS = "imgs/{}_{}.png"

REAIS = {
         "0.01": "UM CENTAVO",
         "0.05": "CINCO CENTAVOS",
         "0.1": "DEZ CENTAVOS",
         "0.25": "VINTE E CINCO CENTAVOS",
         "0.5": "CIQUENTA CENTAVOS",
         "1.0": "UM REAL",
         "2.0": "DOIS REAIS",
         "5.0": "CINCO REAIS",
         "10.0": "DEZ REAIS",
         "20.0": "VINTE REAIS",
         "50.0": "CIQUENTA REAIS",
         "100.0": "CEM REAIS"}


class Money:
    def __init__(self, value, typ):
        self.value = value
        self.typ = typ
        self.name = self.__get_name()
        self.path = self.__get_path()

    def __get_path(self):
        value_string = str(self.value)
        return IMGS.format(value_string, self.typ)

    def __get_name(self):
        name = str(self.value)
        if self.typ == "real":
            return REAIS[name]
        return None

    def render_money(self):
        img = ImageTk.PhotoImage(Image.open(self.path))
        return img
