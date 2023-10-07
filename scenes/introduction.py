from manim import *
from manim_slides import Slide

Text.set_default(font="Linux Libertine O", disable_ligatures=True)
# Tex.set_default(tex_template=TexFontTemplates.libertine)
class Bezier(ParametricFunction):
    def __init__(self, points, **kwargs):
        super().__init__(bezier(points),**kwargs)

class IntroScene(Slide):
    def construct(self):
        self.camera.background_color = "#282c34"

        title_text = Text("Introduction")

        self.add(title_text)

        heading_text = Text("Introduction", font_size=34)
        heading_text.to_corner(UP + LEFT)

        self.play(Transform(title_text, heading_text))

        self.wait()

        problem_text = Text(
            """
            Given a particle at the origin, if it takes any path
            of distance 1, what is its displacement?
            """,
            t2s = {"any" : ITALIC}, t2c = {"distance" : BLUE, "displacement" : RED},
        )
        problem_text.scale(0.8)

        problem_text.move_to(UP * 0.5)

        circle = Circle(radius=1.5, color=WHITE)

        curve = Bezier([
            np.array([x, y, 0])
            for x, y in [
                (0, 0), (0.5, 0.5), (1, 0)
            ]
        ]).set_color(BLUE)

        curve.move_to(DOWN * 2 + np.array([0.5, 0.1, 0]))
        circle.move_to(DOWN * 2)
        dot_start = Dot(point=DOWN * 2)
        dot_end = Dot(point=DOWN * 2 + np.array([1, 0, 0]))
        displacement = Line(curve.get_start(), curve.get_end()).set_color(RED)

        self.play(Write(problem_text))

        self.play(Create(circle))
        self.play(Create(curve), Create(displacement), Create(dot_start), Create(dot_end))

        self.next_slide()

        self.play(FadeOut(problem_text), FadeOut(circle), FadeOut(dot_start), FadeOut(curve), FadeOut(displacement), FadeOut(dot_end))

        trap_text = Text("It's a trap!", color=RED)
        flushed_text = Text("...or is it?", font_size=28)
        flushed_text.move_to(DOWN)

        self.play(Write(trap_text))

        self.wait()

        self.play(Write(flushed_text))

        self.next_slide()

        self.play(FadeOut(title_text), FadeOut(heading_text), FadeOut(trap_text), FadeOut(flushed_text))

        new_title_text = Text("Properties")

        self.play(Write(new_title_text))
