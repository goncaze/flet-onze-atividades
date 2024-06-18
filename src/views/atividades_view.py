import flet as ft


class AtividadesView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(title=ft.Text("Atividades"), bgcolor="green")
        self.page = page
        self.ttf_dado = ft.TextField(expand=True)

        self.controls = [
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        text="Tabuada",
                        on_click=lambda _: self.page.go("/tabuada"),
                    ),
                    ft.ElevatedButton(
                        text="Maior, menor e média",
                        on_click=lambda _: self.page.go("/mmm"),
                    ),
                    ft.ElevatedButton(
                        text="Jogo da adivinhação",
                        on_click=lambda _: self.page.go("/jogo_adivinhacao"),
                    ),
                    ft.ElevatedButton(
                        text="Jogo da Forca",
                        on_click=lambda _: self.page.go("/jogo_forca"),
                    ),
                ],
            )
        ]
