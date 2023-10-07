from manim import *
from manim_slides import Slide

from math import sqrt

Text.set_default(font="Linux Libertine O", disable_ligatures=True)
# Tex.set_default(tex_template=TexFontTemplates.libertine)

class PropScene(Slide):
    def construct(self):
        self.camera.background_color = "#282c34"

        title_text = Text("Properties")

        self.add(title_text)

        heading_text = Text("Properties", font_size=34)
        heading_text.to_corner(UP + LEFT)

        self.play(Transform(title_text, heading_text))

        self.wait()

        path1 = ParametricFunction(
            lambda t: np.array((t, np.sin(PI / 2 * t), 0)),
            t_range = np.array([0, 1]),
            fill_opacity = 0
        ).set_color(BLUE)

        path2 = ParametricFunction(
            lambda t: np.array((t, 2 * t - np.sin(PI / 2 * t), 0)),
            t_range = np.array([0, 1]),
            fill_opacity = 0
        ).set_color(BLUE)

        circle = Circle(radius=2.0, color=WHITE)
        center = Dot(point=ORIGIN)
        end_point = Dot(np.array([1, 1, 0]))

        to_rotate = VGroup(path1, path2, end_point)

        self.play(Create(circle), Create(center))
        self.play(Create(path1), Create(path2))
        self.play(Create(end_point))

        self.bring_to_front(center)
        self.bring_to_back(path1)
        self.bring_to_back(path2)

        self.next_slide()

        self.play(Rotate(
            to_rotate,
            angle = 1.57,
            about_point = ORIGIN,
            rate_func = smooth
        ))

        self.wait()

        self.play(Rotate(
            to_rotate,
            angle = -2,
            about_point = ORIGIN,
            rate_func = smooth
        ))

        self.wait()

        self.play(Rotate(
            to_rotate,
            angle = 0.43,
            about_point = ORIGIN,
            rate_func = smooth
        ))

        self.next_slide()

        self.play(FadeOut(path1), FadeOut(path2))

        radial_line = Line(np.array([0, 0, 0]), np.array([2, 0, 0])).set_color(BLUE)
        radial_point = Dot(point=np.array([2, 0, 0]))

        self.play(Create(radial_line), Transform(end_point, radial_point))

        self.next_slide()

        self.play(
            FadeOut(title_text),
            FadeOut(heading_text),
            FadeOut(circle),
            FadeOut(center),
            FadeOut(radial_line),
            FadeOut(radial_point),
            FadeOut(end_point)
        )

        new_title_text = Text("Modeling")

        self.play(Write(new_title_text))
