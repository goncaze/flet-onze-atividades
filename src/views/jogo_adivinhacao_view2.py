import flet as ft


class JogoAdivinhacao2(ft.View):
    def __init__(self, page: ft.Page, numero_sorteado: str):
        super().__init__()
        self.page = page
        self.numero_sorteado = int(numero_sorteado)
        self.route = "/jogo_adivinhacao2/numero_sorteado"
        self.appbar = ft.AppBar(
            title=ft.Text(value="Jogo da Adivinhação", color="white"), bgcolor="green"
        )
        self.resultado = ft.Text()
        self.ttf_chute = ft.TextField(label="Chute", hint_text="Chute um número")

        self.controls = [
            ft.Text(value="Um número foi sorteado!", size=25, color="blue"),
            ft.Text(value="Chute um número dentre 1 e 100.", size=15, color="blue"),
            self.ttf_chute,
            ft.ElevatedButton(
                text="Conferir",
                on_click=self.conferir,
            ),
            self.resultado,
        ]

    def conferir(self, e):
        chute = int(self.ttf_chute.value)
        if self.numero_sorteado == chute:
            self.resultado.value = (
                f"Parabéns, você acertou!! \nNº Sorteado: {self.numero_sorteado}"
            )
        elif chute < self.numero_sorteado:
            self.resultado.value = f"Chute mais alto"
        else:
            self.resultado.value = f"Chute mais baixo"
        self.resultado.update()


if __name__ == "__main__":
    pass
