from manim import *
from manim_slides import Slide

Text.set_default(font="Linux Libertine O", disable_ligatures=True)

class ConcludeScene(Slide):
    def construct(self):
        self.camera.background_color = "#282c34"

        title_text = Text("Conclusion")

        self.add(title_text)

        heading_text = Text("Conclusion", font_size=34)
        heading_text.to_corner(UP + LEFT)

        self.play(Transform(title_text, heading_text))

        self.wait()

        thanks_text = Text("Thank you!")

        self.play(Write(thanks_text))
