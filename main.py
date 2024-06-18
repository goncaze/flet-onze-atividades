import flet as ft
from src.views.atividades_view import AtividadesView
from src.views.tabuada_view import TabuadaView
from src.views.maior_menor_media_view import MaiorMenorMedia
from src.views.jogo_adivinhacao_view import JogoAdivinhacao
from src.views.jogo_adivinhacao_view2 import JogoAdivinhacao2
from src.views.jogo_forca_view import JogoForca


class App:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 380
        self.page.window_height = 530
        # Conectar um manipulador de eventos ao page.on_route_change
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go("/")

    def route_change(self, route: ft.RouteChangeEvent):
        troute = ft.TemplateRoute(self.page.route)

        if troute.match("/"):
            self.page.views.clear()
            self.page.views.append(AtividadesView(self.page))
        elif troute.match("/tabuada"):
            self.page.views.append(TabuadaView())
        elif troute.match("/mmm"):
            self.page.views.append(MaiorMenorMedia())
        elif troute.match("/jogo_adivinhacao"):
            self.page.views.append(JogoAdivinhacao(self.page))
        elif troute.match("/jogo_adivinhacao2/:numero_sorteado"):
            self.page.views.append(JogoAdivinhacao2(self.page, troute.numero_sorteado))
        elif troute.match("/jogo_forca"):
            self.page.views.append(JogoForca())

        self.page.update()

    def view_pop(self, e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        self.page.update()


def main(page: ft.Page):
    App(page)


if __name__ == "__main__":
    ft.app(target=main)
