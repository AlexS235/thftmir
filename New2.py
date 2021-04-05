from manim import *

class Intro(Scene):
    def construct(self):
        titleIntro1 = Tex("The hunt for the most", tex_to_color_map={"the most": YELLOW}).scale(1.5)
        titleIntro2 = Tex("Irrational Number", tex_to_color_map={"Irrational Number": BLUE}).scale(3)
        titleIntro = VGroup(titleIntro1, titleIntro2).arrange(DOWN)
        self.play(Write(titleIntro1))
        self.play(Write(titleIntro2))
        self.wait()
    
class New2(Scene):
    def construct(self):
        title1 = Tex("IRRATIONAL NUMBERS",
                     tex_to_color_map={"IRRATIONAL NUMBERS": BLUE})
        title1.scale(2)
        irrationalNums = MathTex("\\pi , \\sqrt{2}, \\sqrt{5}")
        irrationalNums.scale(3)
        self.play(
            FadeInFrom(title1, DOWN)
        )
        self.wait()
        self.play(title1.animate.shift(UP*2))
        self.play(Write(irrationalNums))
        definition = Tex("Can’t be expressed as a ratio between two integers",
                         tex_to_color_map={"ratio between two integers": YELLOW})
        definition.shift(DOWN*2)
        self.wait(2)
        self.play(Write(definition))
        self.wait(3)
        self.play(
            FadeOut(title1),
            FadeOut(irrationalNums),
            FadeOut(definition)
        )

        rationalExample = MathTex("0.5 = \\frac{1}{2}")
        rationalExample.scale(2)
        irrationalExample = MathTex("\\pi = \\frac{?}{?}",
                     tex_to_color_map={"\\pi = \\frac{?}{?}": RED})
        irrationalExample.scale(3)

        self.play(Write(rationalExample))
        self.wait()
        self.play(Transform(rationalExample, irrationalExample))
        self.wait(3)

        continued1 = MathTex("\\pi=", "3.141592...")
        continued1.scale(3)
        continued1c1 = MathTex("\\pi=", "3.", "141592...",
                              tex_to_color_map={"\\pi=": BLUE,
                                                "3.": BLUE,
                                                "141592...": BLUE})
        continued1c1.to_corner(UP)
        continued1c2 = MathTex("\\pi=", "3.", "141592...",
                              tex_to_color_map={"\\pi=": BLUE,
                                                "3.": BLUE,
                                                "141592...": YELLOW})
        continued1c2.to_corner(UP)
        continued2 = MathTex("\\pi=3+something")
        continued2.scale(2)
        continued2c1 = MathTex("\\pi=3+something",
                              tex_to_color_map={"something": YELLOW})
        continued2c1.scale(2)
        continued3c1 = MathTex("\\pi=", "3+", "\\frac{1}{something}",
                              tex_to_color_map = {"\\frac{1}{something}": YELLOW})
        continued3c1.scale(2)

        self.play(Transform(rationalExample, continued1))
        self.wait()
        self.play(Transform(rationalExample, continued1c1))
        self.play(Write(continued2))
        self.wait()
        self.play(Transform(rationalExample, continued1c2),
                  FadeOut(continued2), FadeIn(continued2c1))
        self.wait()
        #self.play(FadeOut(continued2c1),FadeIn(continued3c1))
        self.play(Transform(continued2c1,continued3c1))
        self.wait()
        frameBox1 = SurroundingRectangle(continued3c1[2], buff=0.1)
        self.play(Create(frameBox1))
        self.wait()
        continued4c1 = MathTex("\\pi=", "3+", "\\frac{1}{7.062545...}",
                              tex_to_color_map = {"\\frac{1}{7.062545...}": YELLOW})
        continued4c1.scale(2)
        continued4 = MathTex("\\pi=", "3+", "\\frac{1}{7.062545...}")
        continued4.scale(2)
        
        
        self.play(Uncreate(frameBox1),
                  Transform(continued2c1, continued4c1))
        self.wait()

        continued1.scale(1/3)
        continued1.to_corner(UP)
        continued4c2 = MathTex("\\pi=", "3+", "\\frac{1}{7.062545...}",
                              tex_to_color_map = {"7.062545...": RED})
        continued4c2.scale(2)

        self.play(FadeOut(rationalExample), FadeIn(continued1c1),
                  FadeOut(continued2c1),
                  FadeIn(continued4))
        self.wait()
        self.play(FadeOut(continued4), FadeIn(continued4c2))
        self.wait()
        
        continued5c1 = MathTex("\\pi=", "3+", "\\frac{1}{7+something}",
                              tex_to_color_map = {"something": YELLOW})
        continued5c1.scale(2)
        continued5c2 = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{something}}",
                              tex_to_color_map = {"\\frac{1}{something}": YELLOW})
        continued5c2.scale(2)

        self.play(Transform(continued4c2, continued5c1))
        self.wait()
        self.play(Transform(continued4c2, continued5c2))
        self.play
        self.wait()
        
        continued6 = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15.9965...}}",
                             tex_to_color_map = {"\\frac{1}{15.9965...}": YELLOW})
        continued6.scale(2)
        continued6c1 = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15+\\frac{1}{something}}}",
                               tex_to_color_map = {"\\frac{1}{something}": YELLOW})
        continued6c1.scale(2)

        self.play(Transform(continued4c2, continued6))
        self.wait()
        self.play(Transform(continued4c2, continued6c1))
        self.wait()

        continuedX1 = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}")
        continuedX1.scale(2)
        self.play(TransformMatchingTex(continued4c2,continuedX1))
        self.wait()
        braceContinuedFraction = Brace(continuedX1, direction=UP).shift(DOWN*0.5)
        braceContinuedFractionText = braceContinuedFraction.get_text("Continued Fraction")
        self.play(continuedX1.animate.shift(DOWN*0.5),
                  Wait(),
                  Create(braceContinuedFraction),
                  Wait(),
                  Create(braceContinuedFractionText))
        self.wait()

        continuedXconv1 = MathTex("\\pi=3", "+\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}",
                                  tex_to_color_map = {"+\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}": RED})
        continuedXconv1.scale(2)
        continuedXconv1.shift(DOWN*0.5)
        framebox2 = SurroundingRectangle(continuedXconv1[0])
        framebox2text = Brace(framebox2, direction=DOWN).get_text("First convergent")
        
        self.play(FadeOut(continuedX1),
                  FadeIn(continuedXconv1),
                  Create(framebox2),
                  Write(framebox2text))
        self.wait()
        self.play(FadeOut(continuedXconv1),
                  FadeIn(continuedX1),
                  Uncreate(framebox2),
                  Unwrite(framebox2text))
        self.wait()

        continuedXconv2c1 = MathTex("\\pi=3", "+\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}",
                                  tex_to_color_map = {"+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}": RED})
        continuedXconv2c1.scale(2)
        continuedXconv2c1.shift(DOWN*0.5)
        continuedXconv2 = MathTex("\\pi=3", "+\\frac{1}{7}")
        continuedXconv2.scale(2)
        continuedXconv2.shift(DOWN*0.5)
        braceContinuedXconv2 = Brace(continuedXconv2, direction=UP)
        braceContinuedXconv2Text = braceContinuedXconv2.get_text("Second convergent")
        braceContinuedXconv2TextDown = Brace(continuedXconv2, direction=DOWN).get_text("accurate to two decimals")
        continuedXconv2simple = MathTex("\\pi=", "\\frac{22}{7}")
        continuedXconv2simple.scale(2)
        continuedXconv2simple.shift(DOWN*0.5)
        continuedXconv2simpleR = MathTex("\\pi=", "\\frac{22}{7}", "=3.142857...")
        continuedXconv2simpleR.scale(2)
        continuedXconv2simpleR.shift(DOWN*0.5)
        continuedXconv2simpleRc1 = MathTex("\\pi=", "\\frac{22}{7}", "=3.142857...",
                                           tex_to_color_map = {"3.14": GREEN, "2857...": RED})
        continuedXconv2simpleRc1.scale(2)
        continuedXconv2simpleRc1.shift(DOWN*0.5)
        braceContinuedXconv2simpleRc1 = Brace(continuedXconv2simpleRc1, direction = UP)
        
        
        self.play(FadeOut(continuedX1),
                  FadeIn(continuedXconv2c1))
        self.wait()
        self.play(TransformMatchingTex(continuedXconv2c1, continuedXconv2),
                  Uncreate(braceContinuedFractionText),
                  Uncreate(braceContinuedFraction),
                  Wait(),
                  Create(braceContinuedXconv2),
                  Write(braceContinuedXconv2Text))
        self.wait()
        self.play(TransformMatchingTex(continuedXconv2, continuedXconv2simple))
        self.wait()
        self.play(TransformMatchingTex(continuedXconv2simple, continuedXconv2simpleR),
                  ReplacementTransform(braceContinuedXconv2, braceContinuedXconv2simpleRc1))
        self.wait()
        self.play(FadeOut(continuedXconv2simpleR),
                  FadeIn(continuedXconv2simpleRc1))
        self.wait()
        self.play(Write(braceContinuedXconv2TextDown))
        self.wait(2)
#BACK TO CONTINUED FRAC
        self.play(FadeOut(continuedXconv2simpleRc1),
                  FadeOut(braceContinuedXconv2TextDown),
                  FadeOut(braceContinuedXconv2Text),
                  FadeOut(braceContinuedXconv2simpleRc1))
        continuedXconv3c1 = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}",
                                  tex_to_color_map = {"+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}": RED})
        continuedXconv3c1.scale(2)
        continuedXconv3c1.shift(DOWN*0.5)
        braceContinuedFraction2 = Brace(continuedX1, direction=UP)
        braceContinuedFractionText2 = braceContinuedFraction2.get_text("Continued Fraction")
        
        self.play(FadeInFrom(continuedX1,DOWN),
                  Create(braceContinuedFractionText2),
                  Create(braceContinuedFraction2))
        self.wait()
        self.play(FadeOut(continuedX1), FadeIn(continuedXconv3c1))
        self.wait()
        continuedXconv3 = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15}}").scale(2).shift(DOWN*0.5)
        continuedXconv3simple = MathTex("\\pi=", "3+", "\\frac{15}{106}").scale(2).shift(DOWN*0.5)
        continuedXconv3simpleR = MathTex("\\pi=", "3+", "\\frac{15}{106}", "=3.1415094...").scale(2).shift(DOWN*0.5)
        continuedXconv3simpleRc1 = MathTex("\\pi=", "3+", "\\frac{15}{106}", "=3.1415094...",
                                         tex_to_color_map = {"3.1415": GREEN, "094...":RED}).scale(2).shift(DOWN*0.5)
        braceContinuedXconv3 = Brace(continuedXconv3, direction=UP)
        braceContinuedXconv3Text = braceContinuedXconv3.get_text("Third convergent")
        braceContinuedXconv3TextDown = Brace(continuedXconv3, direction=DOWN).get_text("accurate to four decimals")
        braceContinuedXconv3simpleRc1 = Brace(continuedXconv3simpleRc1, direction = UP)
        
        self.play(TransformMatchingTex(continuedXconv3c1, continuedXconv3),
                  Uncreate(braceContinuedFractionText2),
                  Uncreate(braceContinuedFraction2),
                  Create(braceContinuedXconv3),
                  Write(braceContinuedXconv3Text))
        self.wait()
        self.play(TransformMatchingTex(continuedXconv3, continuedXconv3simple))
        self.wait()
        self.play(TransformMatchingTex(continuedXconv3simple, continuedXconv3simpleR),
                  ReplacementTransform(braceContinuedXconv3, braceContinuedXconv3simpleRc1))
        self.wait()
        self.play(FadeOut(continuedXconv3simpleR),
                  FadeIn(continuedXconv3simpleRc1),
                  Write(braceContinuedXconv3TextDown))
        self.wait()
        
class New2ptB(Scene):
    def construct(self):
        title2t = Tex("Convergents")
        title2c = MathTex("c")
        title2of = Tex("of")
        title2pi = MathTex("\\pi")
        title2 = VGroup(title2t, title2c, title2of, title2pi).arrange(RIGHT).scale(2).to_corner(UP)

        convpi1 = MathTex("c_{1}=3.0000000000...", tex_to_color_map = {"3.": GREEN, "0000000000...":RED})
        convpi2 = MathTex("c_{2}=3.1428571428...", tex_to_color_map = {"3.14": GREEN, "28571428...":RED})
        convpi3 = MathTex("c_{3}=3.1415094339...", tex_to_color_map = {"3.1415": GREEN, "094339...":RED})
        convpi4 = MathTex("c_{4}=3.1415929203...", tex_to_color_map = {"3.141592": GREEN, "9203...":RED})
        convpi5 = MathTex("c_{5}=3.1415926530...", tex_to_color_map = {"3.141592653": GREEN, "0...":RED})
        convpi6 = MathTex("c_{6}=3.1415926539...", tex_to_color_map = {"3.141592653": GREEN, "9...":RED})
        convpi7 = MathTex("c_{7}=3.1415926534...", tex_to_color_map = {"3.141592653": GREEN, "4...":RED})
        convpi8 = MathTex("c_{8}=3.1415926536...", tex_to_color_map = {"3.141592653": GREEN, "6...":RED})
        convpi9 = MathTex("c_{9}=3.1415926535...", tex_to_color_map = {"3.1415926535": GREEN, "...":RED})
        convpi9long = MathTex("c_{9}=3.1415926535811...", tex_to_color_map = {"3.1415926535": GREEN, "811...":RED}).scale(3)

        convpi1to9 = VGroup(convpi1, convpi2, convpi3,
                            convpi4, convpi5, convpi6,
                            convpi7, convpi8, convpi9).arrange(DOWN).shift(DOWN*0.5)

        
        self.play(Write(title2))
        self.play(Write(convpi1to9))
        self.wait()
        self.play(Transform(convpi1to9, convpi9))
        
