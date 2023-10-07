from manim import *
from manim_slides import Slide

Text.set_default(font="Linux Libertine O", disable_ligatures=True)

class TitleScene(Slide):
    def construct(self):
        self.camera.background_color = "#282c34"

        # The title really is a work in progress
        # ^ The specific problem is really a springboard for talking more generally
        # about creating and solving math problems

        # title_text = Text("A Restricted Random Walk", font="Liberation Serif")
        title_text = Text("A Restricted Random Walk")
        credits_text = Text("By: Rushil Surti", color="#e7e7ff", font_size=24)
        credits_text.move_to(DOWN * 0.75)

        self.play(Write(title_text))
        self.wait()
        self.play(Write(credits_text))
        self.next_slide()

        self.play(FadeOut(title_text), FadeOut(credits_text))

        new_title_text = Text("Introduction")

        self.play(Write(new_title_text))
