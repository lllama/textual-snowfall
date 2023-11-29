import random
from itertools import chain, takewhile

from rich.segment import Segment
from rich.style import Style
from textual.containers import Container
from textual.geometry import Size
from textual.strip import Strip

SNOW = ["❄️", "❅", "❆", "❄"]


class FlakeColumn:
    def __init__(self):
        self.speed = random.randrange(1, 10)
        self.tick_count = 0
        self.snow_fall = []
        self.started = False

    def tick(self):
        if self.tick_count < self.speed:
            self.tick_count += 1
            return

        self.tick_count = 0

        if random.random() > 0.1:
            self.snow_fall.insert(0, " ")
            return

        self.snow_fall.insert(0, random.choice(SNOW))
        self.snow_fall = self.snow_fall[:200]

    def __getitem__(self, index):
        try:
            return self.snow_fall[index]
        except IndexError:
            return " "


def snow_machine():
    while True:
        yield FlakeColumn()


class Snowfall(Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_interval(0.1, self.tick)
        self.snowing = False
        self.mounted = False
        self.flakes: list[FlakeColumn] = []

    def tick(self):
        for column in self.flakes:
            column.tick()

        self.refresh()

    def on_mount(self, event):
        self.snowing = True

    def on_resize(self, event):
        self.flakes = [
            col
            for (_, col) in takewhile(lambda x: x[0] <= event.size.width, enumerate(chain(self.flakes, snow_machine())))
        ]

    def render_line(self, y):
        # if self.flakes:
        #     return Strip([Segment(f"{len(self.flakes)=}"), Segment(f"{self.flakes[0].snow_fall=}")])
        # return Strip([Segment(f"{len(self.flakes)=}")])
        # if y == 0:
        # return Strip([Segment(f"{self.flakes=}")])
        return Strip([Segment(column[y], Style(bold=True)) for column in self.flakes])
