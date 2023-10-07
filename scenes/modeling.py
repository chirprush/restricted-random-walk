from manim import *
from manim_slides import Slide

from math import sqrt, exp

Text.set_default(font="Linux Libertine O", disable_ligatures=True)
Tex.set_default(tex_template=TexFontTemplates.libertine)

def gaussian(n, t):
    return n * exp(-n ** 2 * t ** 2)

def shifted_gaussian(n, t):
    if abs(t) > 1:
        return 0
    return gaussian(n, t) - gaussian(n, 1)

class ModelScene(Slide):
    def construct(self):
        self.camera.background_color = "#282c34"

        title_text = Text("Modeling")

        self.add(title_text)

        heading_text = Text("Modeling", font_size=34)
        heading_text.to_corner(UP + LEFT)

        self.play(Transform(title_text, heading_text))

        self.wait()

        motivator_text = Text("What is a path?")
        motivator_text.scale(0.8)
        motivator_text.move_to(UP)

        self.play(Write(motivator_text))

        lines = [
            Line(np.array([0, 0, 0]), np.array([0.5, 1, 0])),
            Line(np.array([0.5, 1, 0]), np.array([1.0, 0, 0])),
            Line(np.array([1.0, 0, 0]), np.array([1.5, 1, 0])),
        ]

        line_group = VGroup(*lines)
        line_group.set_color(BLUE)
        line_group.move_to(DOWN)

        self.wait(2)

        particle_object = VGroup(
            Circle(radius=sqrt(1.25), color=BLUE),
            Dot(point=ORIGIN)
        )

        particle_object.move_to(np.array([-0.75, -1.5, 0]))
        
        self.play(Create(particle_object))

        for i, line in enumerate(lines):
            self.play(Create(line))
            self.play(MoveAlongPath(particle_object, line))

        size_label = Tex("$\\frac{1}{N}$", font_size=30)
        size_label.move_to(DOWN * 0.9 + LEFT) # * 0.8)

        self.play(Write(size_label))

        self.next_slide()

        self.play(FadeOut(particle_object), FadeOut(line_group), FadeOut(motivator_text), FadeOut(size_label))

        self.wait(1)

        # Y'know this is gonna be a little scuffed but anything for the typography
        explanation_text = Tex(
            """
            Suppose we have a continuum of random variables $\\{\\mathit{X}_\\mathit{r} (\\mathit{t}) : \\mathit{t} \\in [0, 1] \\}$, \nwhere for all $\mathit{t}$ $\\mathit{X}_\\mathit{r} (\\mathit{t})$ is uniformly distributed on a circle of radius $\\mathit{r}$. Then our \nparticle distribution is
            """,
            font_size=30,
        )
        explanation_text.move_to(UP * 2)

        math_text = Tex(r"$$\int_{0}^1 \mathit{X}_{\mathit{dt}} (\mathit{t}) \, \mathit{dt} = \lim_{\mathit{N} \to \infty} \sum_{\mathit{k} = 0}^{\mathit{N}} \mathit{X}_{(1 / \mathit{N})} (\mathit{k} / \mathit{N}).$$", font_size=50)

        catch_text = Text("...sort of", font_size=20)
        catch_text.move_to(2 * DOWN)

        self.play(Write(explanation_text))
        self.play(Write(math_text))
        self.play(Write(catch_text))

        self.next_slide()

        angle1 = ValueTracker(0)
        angle2 = ValueTracker(0)
        angle1.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        angle2.add_updater(lambda mobject, dt: mobject.increment_value(dt))

        self.add(angle1)
        self.add(angle2)

        speed_mult1 = 5
        speed_mult2 = 5

        circle1 = Circle(radius=2.0, color=WHITE)
        circle2 = Circle(radius=2.0, color=WHITE).add_updater(
            lambda c: c.move_to(np.array([
                2.0 * np.cos(speed_mult1 * angle1.get_value()),
                2.0 * np.sin(speed_mult1 * angle1.get_value()),
                0
            ]))
        )

        line1 = Line(np.array([0, 0, 0]), np.array([2, 0, 0])).set_color(RED).add_updater(
            lambda l: l.put_start_and_end_on(
                np.array([0, 0, 0]),
                np.array([2 * np.cos(speed_mult1 * angle1.get_value()), 2 * np.sin(speed_mult1 * angle1.get_value()), 0])
            )
        )

        line2 = Line(np.array([2, 0, 0]), np.array([4, 0, 0])).set_color(RED).add_updater(
            lambda l: l.put_start_and_end_on(
                np.array([2 * np.cos(speed_mult1 * angle1.get_value()), 2 * np.sin(speed_mult1 * angle1.get_value()), 0]),
                np.array([2 * np.cos(speed_mult1 * angle1.get_value()) + 2 * np.cos(speed_mult2 * speed_mult1 * angle2.get_value()), 2 * np.sin(speed_mult1 * angle1.get_value()) + 2 * np.sin(speed_mult2 * speed_mult1 * angle2.get_value()), 0])
            )
        )

        dot1 = Dot(point=np.array([0, 0, 0])).add_updater(
            lambda l: l.move_to(
                np.array([2 * np.cos(speed_mult1 * angle1.get_value()), 2 * np.sin(speed_mult1 * angle1.get_value()), 0])
            )
        )

        dot2 = Dot(point=np.array([2, 0, 0])).add_updater(
            lambda l: l.move_to(
                np.array([2 * np.cos(speed_mult1 * angle1.get_value()) + 2 * np.cos(speed_mult2 * speed_mult1 * angle2.get_value()), 2 * np.sin(speed_mult1 * angle1.get_value()) + 2 * np.sin(speed_mult2 * speed_mult1 * angle2.get_value()), 0])
            )
        )


        self.play(FadeOut(explanation_text), FadeOut(math_text), FadeOut(catch_text))
        self.play(Create(circle1), Create(circle2), Create(line1), Create(line2), Create(dot1), Create(dot2))

        self.wait(10)

        self.play(FadeOut(circle1), FadeOut(circle2), FadeOut(line1), FadeOut(line2), FadeOut(dot1), FadeOut(dot2))

        self.next_slide()

        explanation_text1 = Tex(
            r"$-\frac{1}{\mathit{N}} \leqslant \mathit{x} \leqslant \frac{1}{\mathit{N}}$",
            font_size=60,
        )
        explanation_text1.move_to(UP)

        explanation_text2 = Tex(
            r"$$\mathit{f}(\mathit{t}) = \frac{\mathit{N}^{\mathit{N}}}{2^{\mathit{N}} (\mathit{N} - 1)!} \sum_{\mathit{k} = 0}^{\mathit{N}} \binom{\mathit{N}}{\mathit{k}} (-1)^{\mathit{k}} (\mathit{t} + (\mathit{N} - 2 \mathit{k}) \mathit{r})^{\mathit{N} - 1} \mathit{H} (\mathit{t} + (\mathit{N} - 2 \mathit{k}) \mathit{r}).$$",
            font_size=40,
        )
        explanation_text2.move_to(DOWN)

        self.play(Write(explanation_text1))

        self.wait(2)

        self.play(Write(explanation_text2))

        self.next_slide()

        self.play(FadeOut(explanation_text1), FadeOut(explanation_text2))

        number_plane = NumberPlane()
        self.play(Create(number_plane))

        # Used to illustrate the effect but not actually correct lmao
        graph1 = FunctionGraph(
            lambda t: shifted_gaussian(1.5, t),
            color=BLUE
        )

        graph2 = FunctionGraph(
            lambda t: shifted_gaussian(3, t),
            color=BLUE
        )

        graph3 = FunctionGraph(
            lambda t: shifted_gaussian(6, t),
            color=BLUE
        )
        
        self.play(FadeIn(graph1))

        self.next_slide()

        self.play(Transform(graph1, graph2))

        self.next_slide()

        self.play(FadeOut(graph2), Transform(graph1, graph3))

        self.next_slide()

        self.play(FadeOut(graph1), FadeOut(graph3), FadeOut(number_plane))

        explanation_text1 = Tex(
            r"$$Var(Particle) = \frac{1}{3 \mathit{N}} \to 0$$",
            font_size=50,
        )
        explanation_text1.move_to(UP)

        explanation_text2 = Tex(
            r"$\delta (\mathit{t})$",
            color=BLUE,
            font_size=70,
            tex_template=None
        )
        explanation_text2.move_to(DOWN)

        self.play(Write(explanation_text1))
        self.wait(2)
        self.play(Write(explanation_text2))

        self.next_slide()

        self.play(FadeOut(heading_text), FadeOut(title_text), FadeOut(explanation_text1), FadeOut(explanation_text2))

        new_title_text = Text("Conclusion")

        self.play(Write(new_title_text))
