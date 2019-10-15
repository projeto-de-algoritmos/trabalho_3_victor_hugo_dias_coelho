from tkinter import (
    Canvas,
    Tk,
    Button,
    PanedWindow,
    Frame,
    Label,
    Entry)
from money import Money

WIDTH = 1200
HEIGHT = 800
TITLE = "COIN CHANGE"


class Program:
    def __init__(self):
        self.root = Tk()
        self.frame = Frame()
        self.frame.pack(side="top")
        self.title = Label(self.frame, text=TITLE)
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT,
                             borderwidth=0, highlightthickness=0, bg="black")
        self.painel = PanedWindow(orient="horizontal")
        self.list_money = []
        self.ents = []
        self.num_itens = 0
        self.wallet = 0
        self.loss = 0
        self.typ = ""

    def create_form(self):
        entries = []
        fields = ["Wallet", "Loss", "Coin"]
        for field in fields:
            row = Frame(self.painel)
            lab = Label(self.painel, width=15, text=field, anchor='w')
            ent = Entry(self.painel)
            entries.append((row, lab, ent))
        return entries

    def create_money(self):
        values_list = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.25, 0.1,
                       0.05, 0.01]

        change = self.wallet - self.loss
        count = 0
        while change > 0.0:
            if change - values_list[count] >= 0.0:
                change -= values_list[count]
                change = round(change, 2)
                print(change)
                money = Money(values_list[count], self.typ)
                self.list_money.append(money)
            else:
                count += 1

    def render_notes(self):
        print(self.list_money)
        place = [0, 0]
        for each in self.list_money:
            img = each.render_money()
            imge = Label(self.canvas, image=img)
            imge.image = img
            imge.place(x=place[0], y=place[1])
            if place[0] >= 1000:
                place[1] += 150
                place[0] = 0
                continue
            place[0] += 150

    def fetch(self):
        count = 0
        self.list_money = []
        self.canvas.delete("all")
        self.canvas.update()
        for entry in self.ents:
            count += 1
            text = entry.get()
            if count == 1:
                self.wallet = float(text)
            if count == 2:
                self.loss = float(text)
            if count == 3:
                self.typ = str(text)

        print("WALLET: {}\nLOSS: {}\nTyp: {}".format(
              self.wallet, self.loss, self.typ))
        self.create_money()
        self.render_notes()
        self.canvas.update()

    def create_painel(self):
        ents = self.create_form()
        for row, lab, ent in ents:
            self.painel.add(row)
            self.painel.add(lab)
            self.painel.add(ent)
            self.ents.append(ent)

        self.painel.add(Button(self.painel, text="submit",
                               command=self.fetch))

    def main(self):
        self.canvas.pack()
        self.painel.pack()
        self.title.pack(side="top")
        self.create_painel()
        self.root.mainloop()


if __name__ == "__main__":
    program = Program()
    program.main()
