import flet as ft


class AnimatedSwitcher(ft.AnimatedSwitcher):
    def __init__(self, initial_container: ft.Container):
        super().__init__(initial_container)
        self.transition = ft.AnimatedSwitcherTransition.SCALE
        self.duration = 500
        self.reverse_duration = 100
        self.switch_in_curve = ft.AnimationCurve.BOUNCE_OUT
        self.switch_out_curve = ft.AnimationCurve.BOUNCE_IN
