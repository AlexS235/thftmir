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
                  FadeIn(continuedXconv2simpleRc1),
                  Write(braceContinuedXconv2TextDown))
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
        #convpi9long = MathTex("c_{9}=3.1415926535811...", tex_to_color_map = {"3.1415926535": GREEN, "811...":RED}).scale(3)
        #convpi2c = MathTex("c_{2}=3.1428571428...", tex_to_color_map = {"3.1428571428...":YELLOW}).scale(3)
        convpi3c = MathTex("c_{3}=3.1415094339...", tex_to_color_map = {"3.1415": GREEN, "094339...":RED}).scale(3)
        convpi1to9 = VGroup(convpi1, convpi2, convpi3,
                            convpi4, convpi5, convpi6,
                            convpi7, convpi8, convpi9).arrange(DOWN).shift(DOWN*0.5)
        fb = [SurroundingRectangle(convpi5), SurroundingRectangle(convpi6),SurroundingRectangle(convpi7),SurroundingRectangle(convpi8)]

        self.play(Write(title2))
        self.play(Write(convpi1to9))
        self.wait()
        self.play(Create(fb[0]))
        for i in [1,2,3]:
            self.play(ReplacementTransform(fb[i-1],fb[i]))
        self.wait()
        self.play(FadeOut(convpi1),
                  FadeOut(convpi2),
                  FadeOut(convpi4),
                  FadeOut(convpi5),
                  FadeOut(convpi6),
                  FadeOut(convpi7),
                  FadeOut(convpi8),
                  FadeOut(convpi9),
                  FadeOut(fb[3]))
        self.play(TransformMatchingTex(convpi3, convpi3c))
        self.wait()
        title3 = Tex("Pi is really easily approximated with fractions",
                     tex_to_color_map = {"Pi is really easily approximated with fractions": BLUE}).scale(1.25).shift(DOWN*2.5)
        self.play(Write(title3))
        self.wait()
        
class New2ptC(Scene):
        def construct(self):
            title4 = Tex("The most irrational number is \\\\ the hardest to approximate",
                         tex_to_color_map = {"most irrational number": BLUE, "hardest": RED}).scale(2)
            
            continuedPi = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}").scale(2).shift(DOWN*0.5)
            continuedPic = MathTex("\\pi=", "3+", "\\frac{1}{7+\\frac{1}{15+\\frac{1}{1+\\frac{1}{292+\\frac{1}{1+...}}}}}",
                                  tex_to_color_map = {"292": GREEN}).scale(2).shift(DOWN*0.5)
            braceContinuedFractionPi = Brace(continuedPi, direction=UP)
            braceContinuedFractionPiText = braceContinuedFractionPi.get_text("Continued Fraction")
        
            self.play(Write(title4))
            self.wait()
            self.play(FadeOut(title4))
            self.play(Write(continuedPi),
                      Create(braceContinuedFractionPi),
                      Write(braceContinuedFractionPiText))
            self.wait()
            self.play(FadeOut(continuedPi),
                      FadeIn(continuedPic))
            self.wait()

class New2ptD(Scene):
    def construct(self):
        title1 = Tex("Most irrational number",
                    tex_to_color_map = {"Most irrational number": BLUE}).scale(2).to_corner(UP)
        title2 = Tex("The Golden Ratio",
                    tex_to_color_map = {"The Golden Ratio": "#E1B658"}).scale(3).to_corner(UP)
        math1 = MathTex("x").scale(3)
        math2 = MathTex("x", "=", "1+", "\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+...}}}}}").scale(2).shift(DOWN*0.5)
        math3 = MathTex("x", "=", "1+", "\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+...}}}}}",
                        tex_to_color_map = {"1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+\\frac{1}{1+...}}}}": YELLOW}).scale(2).shift(DOWN*0.5)
        math4 = MathTex("x", "=", "1+", "\\frac{1}{x}").scale(3)
        math5 = MathTex("x", "\\times x", "=", "x(", "1+", "\\frac{1}{x}", ")").scale(3)
        math6 = MathTex("x","^2", "=", "x+1").scale(4)
        math7 = MathTex("x", "=", "\\frac{1+\\sqrt{5} }{2}").scale(3)
        math8 = MathTex("\\Phi", "=", "\\frac{1+\\sqrt{5} }{2}").scale(3)
        math9 = MathTex("\\Phi", "=", "1.61803398...", tex_to_color_map = {"\\Phi": BLUE,"=": BLUE, "1.61803398...": BLUE}).to_corner(UP)
        fb = SurroundingRectangle(math8[2])
        self.play(Write(title1, 0.5))
        self.play(Write(math1))
        self.wait()
        self.play(TransformMatchingTex(math1,math2))
        self.wait()
        self.play(FadeOut(math2),
                  FadeIn(math3))
        self.wait()
        self.play(TransformMatchingTex(math3, math4))
        self.wait()
        self.play(TransformMatchingTex(math4, math5))
        self.wait()
        self.play(TransformMatchingTex(math5, math6))
        self.wait()
        self.play(TransformMatchingTex(math6, math7))
        self.wait()
        self.play(TransformMatchingTex(math7,math8))
        self.wait()
        self.play(Transform(title1,title2))
        self.wait()
        self.play(Create(fb))
        self.wait()
        self.play(Uncreate(fb))
        self.wait()
        self.play(FadeOut(title1))
        self.play(TransformMatchingTex(math8, math9))
        self.wait()

class New2ptE(Scene):
    def construct(self):
        start = MathTex("\\Phi", "=", "1.61803398...", tex_to_color_map = {"\\Phi": BLUE,"=": BLUE, "1.61803398...": BLUE}).to_corner(UP)
        self.add(start)

        convphi = [MathTex("c_{1}=", "1 \\divisionsymbol 1", "=", "1.0000000000...", tex_to_color_map = {"1.": GREEN, "0000000000...":RED}),
                   MathTex("c_{2}=", "2 \\divisionsymbol 1", "=", "2.0000000000...", tex_to_color_map = {"2.0000000000...":RED}),
                   MathTex("c_{3}=", "3 \\divisionsymbol 2", "=", "1.5000000000...", tex_to_color_map = {"1.": GREEN, "5000000000...":RED}),
                   MathTex("c_{4}=", "5 \\divisionsymbol 3", "=1.6666666666...", tex_to_color_map = {"1.6": GREEN, "666666666...":RED}),
                   MathTex("c_{5}=", "8 \\divisionsymbol 5", "=1.6000000000...", tex_to_color_map = {"1.6": GREEN, "000000000...":RED}),
                   MathTex("c_{6}=", "13 \\divisionsymbol 8", "=1.6250000000...", tex_to_color_map = {"1.6": GREEN, "250000000...":RED}),
                   MathTex("c_{7}=", "21 \\divisionsymbol 13", "=1.6153846153...", tex_to_color_map = {"1.61": GREEN, "53846153...":RED}),
                   MathTex("c_{8}=", "34 \\divisionsymbol 21", "=1.6190476190...", tex_to_color_map = {"1.61": GREEN, "90476190...":RED}),
                   MathTex("c_{9}=", "55 \\divisionsymbol 34", "=1.6176470588...", tex_to_color_map = {"1.61": GREEN, "76470588...":RED}),
                   MathTex("c_{10}=", "89 \\divisionsymbol 55", "=1.6181818182...", tex_to_color_map = {"1.618": GREEN, "1818182...":RED})]
        convphigroup = VGroup()
        for i in convphi:
            convphigroup.add(i)
        convphigroup.arrange(DOWN).scale(0.8)

        convphi0 = MathTex("c_{1}=", "1").scale(3)
        convphi1 = MathTex("c_{2}=", "1+\\frac{1}{1}", "=", "2").scale(3)
        convphi2 = MathTex("c_{3}=", "1+\\frac{1}{ 1+\\frac{1}{1} }", "=", "\\frac{3}{2}").scale(2.5).shift(DOWN*0.5)
        c10fb = SurroundingRectangle(convphi[9])
        
        convphifbgroup = VGroup()
        for i in convphi:
            convphifbgroup.add(SurroundingRectangle(i[1]))
            
        titlefib = Tex("Fibonacci \\\\ Sequence", tex_to_color_map = {"Fibonacci \\\\ Sequence": "#E1B658"}).scale(3).to_corner(LEFT)
        smoltitlefib = Tex("Fibonacci Sequence", tex_to_color_map = {"Fibonacci Sequence": "#E1B658"}).scale(1.5)
        why = MathTex("1", ",", "1", ",", "2", ",", "3", ",", "5", ",", "8", ",", "13", ",", "21", ",", "34", ",", "55", ",\\\\",
                      "89", ",", "144", ",", "233", ",", "377", ",", "610", ",", "987", ",\\\\", "1597", ",", "2584", ",", "4181",
                      ",", "6765", ",\\\\", "10946", ",", "17711", ",", "28657", ",", "46368", ",\\\\", "\\ldots").to_corner(RIGHT).shift(DOWN*0.5)
        fibgroup = VGroup(smoltitlefib, why).arrange(DOWN).to_corner(RIGHT)
        whyfb = [SurroundingRectangle(why[(12-1)*2]),
                 SurroundingRectangle(why[(11-1)*2]),
                 SurroundingRectangle(why[(24-1)*2]),
                 SurroundingRectangle(why[(23-1)*2])]
        
        fibconv1 = VGroup(
            MathTex("\\frac{144}{89}").scale(1.5),
            MathTex("=1.6179775281...", tex_to_color_map = {"1.61": GREEN, "79775281...":RED})
            ).scale(1.5).arrange(DOWN).to_corner(LEFT).shift(RIGHT/2)
        fibconv2 = VGroup(
            MathTex("\\frac{46368}{28657}").scale(1.5),
            MathTex("\\\\ =1.6180339882...", tex_to_color_map = {"1.618033988": GREEN, "2...":RED})
            ).scale(1.5).arrange(DOWN).to_corner(LEFT).shift(RIGHT/2)
        self.play(Write(convphi0))
        self.wait()
        self.play(TransformMatchingTex(convphi0,convphi[0]))
        self.wait()
        self.play(Write(convphi1, 0.5))
        self.wait()
        self.play(TransformMatchingTex(convphi1,convphi[1]))
        self.wait()
        self.play(Write(convphi2, 0.5))
        self.wait()
        self.play(TransformMatchingTex(convphi2,convphi[2]))
        self.wait()

        for i in [3,4,5,6,7,8,9]:
            self.play(Write(convphi[i],0.2))
        self.wait()
        self.play(Create(c10fb))
        self.wait()
        self.play(FadeOut(c10fb))
        self.wait()
        self.play(Create(convphifbgroup))
        self.wait()
        self.play(convphigroup.animate.shift(RIGHT*3.75),
                  convphifbgroup.animate.shift(RIGHT*3.75))
        self.play(Write(titlefib, 0.5))
        self.wait()
        self.play(Uncreate(convphigroup, run_time=0.5),
                  Uncreate(convphifbgroup, run_time=0.5))
        self.play(Write(why, 0.5))
        self.play(Transform(titlefib, smoltitlefib))
        self.wait()
        self.play(Create(whyfb[0]),
                  Create(whyfb[1]),
                  Write(fibconv1))
        self.wait()
        self.play(Uncreate(whyfb[0]),
                  Uncreate(whyfb[1]))
        self.wait(0.2)
        self.play(Transform(fibconv1,fibconv2),
                  Create(whyfb[2]),
                  Create(whyfb[3]))
        self.wait()

class New2ptF(Scene):
    def construct(self):
        title = Tex("To recap...").scale(3)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

class New2ptG(Scene):
    def construct(self):
        title = Tex("Thanks for \\\\ watching!",
                    tex_to_color_map = {"Thanks for \\\\ watching!": BLUE}).scale(2)
        credit = Tex("Made by Alex Solis using \\\\ Manim Community 5.0",
                     tex_to_color_map = {"Alex Solis": YELLOW})
        
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=WHITE).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m).scale(0.25)  # order matters

        rightGroup = VGroup(credit, logo).arrange(DOWN)
        group = VGroup(title, rightGroup).arrange(RIGHT)
        title.shift(LEFT*0.5)
        rightGroup.shift(RIGHT*0.5)
        self.play(Write(title,3))
        self.play(Write(rightGroup, 2))
        self.wait()

class New2clarification(Scene):
    def construct(self):
        text1 = Tex("Yes, there are technically two\\\\",
                    "solutions, but in this context we\\\\"
                    "only take into account the positive \\\\"
                    "one. Remember, we're adding\\\\",
                    "positive values only!\\\\",
                    tex_to_color_map = {"positive values":YELLOW}).scale(1.8)
        self.play(Create(text1))
        self.wait(4)
