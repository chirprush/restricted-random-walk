# FLAGS := -ql

present:
	manim-slides TitleScene IntroScene PropScene ModelScene ConcludeScene

slides: TitleSlide IntroSlide PropSlide ModelSlide ConcludeSlide

TitleSlide:
	manim $(FLAGS) scenes/title.py TitleScene

IntroSlide:
	manim $(FLAGS) scenes/introduction.py IntroScene

PropSlide:
	manim $(FLAGS) scenes/properties.py PropScene

ModelSlide:
	manim $(FLAGS) scenes/modeling.py ModelScene

ConcludeSlide:
	manim $(FLAGS) scenes/conclusion.py ConcludeScene

.PHONY: slides, TitleSlide, IntroSlide, PropScene, ModelSlide, ConcludeSlide
