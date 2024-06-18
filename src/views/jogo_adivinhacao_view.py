import flet as ft
from random import randint


class JogoAdivinhacao(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.route = "/jogo_adivinhacao"
        self.appbar = ft.AppBar(
            title=ft.Text(value="Jogo da Adivinhação", color="white"), bgcolor="green"
        )

        self.numero_aleatorio = randint(a=1, b=100)

        self.controls = [
            ft.ElevatedButton(
                text="Começar",
                on_click=lambda _: self.page.go(
                    f"/jogo_adivinhacao2/{self.numero_aleatorio}"
                ),
            ),
        ]


if __name__ == "__main__":
    pass
