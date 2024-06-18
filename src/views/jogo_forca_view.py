import flet as ft
from random import randint
from string import ascii_uppercase
from src.views.letra_container import LetraContainer


class JogoForca(ft.View):
    def __init__(self):
        super().__init__()
        self.route = "/jogo_forca"
        self.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.appbar = ft.AppBar(
            title=ft.Text(value="Jogo da Forca", color="white"),
            bgcolor="green",
        )

        self.lista_palavras: list[str] = [
            "AMOR",
            "BEIJO",
            "BOLA",
            "CASA",
            "HONRA",
        ]

        self.txt_parabens = ft.Text(
            value="Parabéns!!",
            size=50,
            color="white",
            bgcolor="green",
            weight=ft.FontWeight.BOLD,
            visible=False,
        )

        self.cptn_picker = ft.CupertinoPicker(
            selected_index=0,
            magnification=1.82,
            squeeze=1.2,
            use_magnifier=True,
            on_change=self.handle_picker_change,
            controls=[ft.Text(letra) for letra in ascii_uppercase],
        )

        self.row_letras: ft.Row = ft.Row(
            wrap=True,
            spacing=4,
        )

        self.palavra_sorteada: str = self.lista_palavras[
            randint(0, len(self.lista_palavras) - 1)
        ]

        self.ctn_palavra_sorteada = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                value=self.palavra_sorteada,
                size=30,
                color=ft.colors.BLUE,
                weight=ft.FontWeight.BOLD,
            ),
            margin=ft.margin.only(bottom=10, top=20),
            visible=False,
        )

        self.letras_corretas = 0

        self.btn_confirmar_letra = ft.ElevatedButton(
            text="Confirmar letra",
            on_click=self.confirmar_letra,
        )

        self.btn_selecionar_letra = ft.ElevatedButton(
            text="Selecionar letra",
            on_click=lambda _: self.page.show_bottom_sheet(
                ft.CupertinoBottomSheet(
                    self.cptn_picker,
                    height=416,
                    padding=ft.padding.only(top=6),
                )
            ),
        )

        self.txt_letra_selecionada = ft.Text(
            value=ascii_uppercase[0],
            size=30,
            color=ft.colors.BLUE,
            weight=ft.FontWeight.BOLD,
        )

        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                content=self.txt_parabens,
                margin=ft.margin.only(top=20),
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(
                    value=f"Palavra com {len(self.palavra_sorteada)} letras",
                    size=20,
                    color=ft.colors.GREEN,
                    weight=ft.FontWeight.BOLD,
                ),
                margin=ft.margin.only(top=20),
            ),
            ft.Container(
                alignment=ft.alignment.center,
                content=self.row_letras,
                margin=ft.margin.only(bottom=10, top=20),
            ),
            self.ctn_palavra_sorteada,
            ft.Container(
                alignment=ft.alignment.center,
                content=self.txt_letra_selecionada,
                margin=ft.margin.only(bottom=20, top=10),
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.btn_selecionar_letra,
                    self.btn_confirmar_letra,
                ],
            ),
        ]
        self.montar_ttfs()

    def montar_ttfs(self):
        for i in range(len(self.palavra_sorteada)):
            ctn_letra = LetraContainer(
                ft.Text(
                    value=self.palavra_sorteada[i],
                    visible=False,
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE,
                )
            )
            self.row_letras.controls.append(ctn_letra)

    def confirmar_letra(self, e):
        chute: str = self.txt_letra_selecionada.value
        for ctn in self.row_letras.controls:
            if ctn.content.value == chute.upper():
                ctn.content.visible = True
                self.letras_corretas += 1
        self.row_letras.update()

        if self.letras_corretas == len(self.palavra_sorteada):
            self.txt_parabens.visible = True
            self.txt_parabens.update()
            self.ctn_palavra_sorteada.visible = True
            self.ctn_palavra_sorteada.update()
            for letra_container in self.row_letras.controls:
                letra_container.animacao_offtset()

    def handle_picker_change(self, e):
        self.txt_letra_selecionada.value = ascii_uppercase[int(e.data)]
        self.txt_letra_selecionada.update()
