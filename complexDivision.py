from manim import *
import numpy as np

class ComplexDivision(Scene):
    def construct(self):
        z_tex = MathTex(r"z &= 1 + 2i \\", r"z^{-1} &= \frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2}i \\", r"&= \frac{1}{5} - \frac{2}{5}i \\", r"&= \frac{1}{a^2 + b^2} (a - bi) \\", r"&= \frac{\overline{z}}{a^2 + b^2} \\", r"&= \frac{\overline{z}}{|z|^2} \\", r"&= \frac{1}{5} - \frac{2}{5}i")
        z_tex.font_size = 40
        z_tex.move_to([3, 0, 0])
        
        # Complex plane
        axes = ComplexPlane(x_range=[-3,3,1], y_range=[-3,3,1]).add_coordinates()
        axes.move_to([-3, 0, 0])
        self.play(Write(axes), run_time=2)

        # Creating the complex point
        z = complex(1, 2)
        mag_z = abs(z)
        arg_z = np.angle(z)
        arc_z = Arc(radius=0.4 * abs(z), start_angle=0, angle=arg_z, color=BLUE, arc_center=axes.c2p(0, 0))
        arc_z_copy = Arc(radius=0.4 * abs(z), start_angle=0, angle=arg_z, color=BLUE, arc_center=axes.c2p(0, 0))
    
        # Plot z with copy for later
        z_vector = Line(start=axes.c2p(0, 0), end=axes.c2p(z.real, z.imag), color=BLUE)
        z_vec_copy = Line(start=axes.c2p(0, 0), end=axes.c2p(z.real, z.imag), color=BLUE)
        z_dot = Dot(axes.c2p(z.real, z.imag), color=BLUE)
        z_dot_copy = Dot(axes.c2p(z.real, z.imag), color=BLUE)
        z_label = MathTex(r"z").next_to(axes.c2p(z.real, z.imag), (UP + RIGHT))
        self.play(Create(z_vector),
                  Create(z_dot), 
                  Create(arc_z), 
                  Write(z_label), 
                  Create(z_vec_copy), 
                  Create(z_dot_copy), 
                  Create(arc_z_copy), 
                  Write(z_tex[0]))
        self.wait(2)

        for i in range(1, 3):
            self.play(Write(z_tex[i]))
            self.wait(1)
        self.play(FadeOut(z_tex[2]))

        # Create the reflected vector as a new line object
        z_reflected = complex(z.real, -z.imag)

        z_reflected_vector = Line(start=axes.c2p(0, 0), end=axes.c2p(z_reflected.real, z_reflected.imag), color=RED)
        z_reflected_dot = Dot(axes.c2p(z_reflected.real, z_reflected.imag), color=RED)
        z_reflected_label = MathTex(r"\overline{z}").next_to(axes.c2p(z_reflected.real, z_reflected.imag), RIGHT)
        arc_z_reflected = Arc(radius=0.4 * abs(z_reflected), start_angle=0, angle=-arg_z, color=RED, arc_center=axes.c2p(0, 0))

        # Animate the original vector
        for i in range(3, 7):
            z_tex[i].shift(UP*0.8)
            self.play(Write(z_tex[i]))
            self.wait(1)
        self.play(Transform(z_vector, z_reflected_vector), 
                  Transform(z_dot, z_reflected_dot),
                  Transform(arc_z, arc_z_reflected), 
                  Write(z_reflected_label))
        self.wait(1)
        
        # Scale down the reflected vector 
        z_scaled = complex(z_reflected.real * (1 / (mag_z**2)), z_reflected.imag * (1 / (mag_z**2)))

        z_scaled_vector = Line(start=axes.c2p(0,0), end=axes.c2p(z_scaled.real, z_scaled.imag), color=RED)
        z_scaled_dot = Dot(axes.c2p(z_scaled.real, z_scaled.imag), color=RED)
        z_scaled_label = MathTex(r"z^{-1}").next_to(axes.c2p(z_scaled.real, z_scaled.imag), RIGHT)
        arc_z_scaled = Arc(radius=0.4 * abs(z_scaled), start_angle=0, angle=-arg_z, color=RED, arc_center=axes.c2p(0, 0))

        
        self.play(Transform(z_vector, z_scaled_vector), 
                  Transform(z_dot, z_scaled_dot),
                  Transform(arc_z, arc_z_scaled), 
                  Transform(z_reflected_label, z_scaled_label))

        self.wait(2)


        
