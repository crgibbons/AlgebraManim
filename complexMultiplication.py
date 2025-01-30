from manim import *
import numpy as np

class ComplexMultiplication(Scene):
    def construct(self):

    # Set up coordinate system
        axes = ComplexPlane(x_range=[-5,5,1],y_range=[-1,4,1]).add_coordinates() 

    # Define two complex numbers
        z1 = complex(2, 1)  # First complex number
        z2 = complex(-1, 2)  # Second complex number

    # Compute their product
        z_product = z1 * z2

    # Extract magnitudes and arguments
        mag_z1 = abs(z1)
        mag_z2 = abs(z2)
        mag_product = abs(z_product)
        arg_z1 = np.angle(z1)
        arg_z2 = np.angle(z2)
        arg_product = np.angle(z_product)
        arc_z1 = Arc(radius=1, start_angle=0, angle=arg_z1, color=BLUE, arc_center=axes.c2p(0, 0))
        arc_z2 = Arc(radius=1.25, start_angle=0, angle=arg_z2, color=GREEN, arc_center=axes.c2p(0, 0))
        arc_product_1 = Arc(radius = 1.5, start_angle=0, angle = arg_z1, color=BLUE, arc_center=axes.c2p(0, 0))
        arc_product_2 = Arc(radius = 1.5, start_angle=arg_z1, angle = arg_z2, color=GREEN, arc_center=axes.c2p(0, 0))

    # Add axes
        self.play(Create(axes))

    # Reposition the complex plane origin if needed

    # Plot z1
        z1_vector = Line(start=axes.c2p(0,0), end=axes.c2p(z1.real, z1.imag), color=BLUE)
        z1_dot = Dot(axes.c2p(z1.real, z1.imag), color=BLUE)
        z1_label = MathTex(r"z_1").next_to(axes.c2p(z1.real, z1.imag), UP)
        self.play(Create(z1_vector), Create(z1_dot), Create(arc_z1), Write(z1_label))

    # Plot z2
        z2_vector = Line(start=axes.c2p(0, 0), end=axes.c2p(z2.real, z2.imag), color=GREEN)
        z2_dot = Dot(axes.c2p(z2.real, z2.imag), color=GREEN)
        z2_label = MathTex(r"z_2").next_to(axes.c2p(z2.real, z2.imag), UP)
        self.play(Create(z2_vector), Create(z2_dot), Create(arc_z2), Write(z2_label))

    # Step 0: Fade out z1 z2
        self.play(FadeOut(arc_z1, z1_label, arc_z2, z2_label))

    # Step 1: Scale z1 by |z2| and plot it along the origin
        scaled_z1 = mag_z2 * z1
        scale_vector = Line(
            start=axes.c2p(0, 0), end=axes.c2p(mag_product, 0), color=YELLOW
        )
        scale_dot = Dot(axes.c2p(mag_product,0), color=YELLOW)
        scale_label = MathTex(r"|z_1 z_2| = |z_2| \cdot |z_1|").next_to(axes.c2p(mag_product, 0), DOWN)
        self.play(FadeIn(scale_vector, scale_dot, scale_label))

    # Step 2: Rotate the scaled vector by arg(z1)
        rotate_vector_1 = Line(
            start=axes.c2p(0, 0), end=axes.c2p(scaled_z1.real, scaled_z1.imag), color=RED
        )
        rotate_dot_1 = Dot(axes.c2p(scaled_z1.real, scaled_z1.imag), color=RED)
        self.play(
            Transform(
                scale_vector, 
                rotate_vector_1,
                path_arc = arg_z1, 
                arc_center = axes.c2p(0,0)
                ), 
            Transform(
                scale_dot,
                rotate_dot_1,
                path_arc = arg_z1,
                arc_center = axes.c2p(0,0)
                ), 
            FadeIn(arc_product_1)
            )

    # Step 3: Rotate the scaled vector by arg(z2)
        rotate_vector_2 = Line(
            start=axes.c2p(0, 0), end=axes.c2p(z_product.real, z_product.imag), color=RED
        )
        rotate_dot_2 = Dot(axes.c2p(z_product.real, z_product.imag), color=RED)
        label_position = .5 * z_product
        product_label = MathTex(r"z_1 z_2").next_to(axes.c2p(z_product.real, z_product.imag), LEFT)
        product_mag_label = MathTex(r"|z_1 z_2| = |z_1| \cdot |z_2|").next_to(axes.c2p(label_position.real, label_position.imag), DOWN + LEFT)
        self.play(
            Transform(
                rotate_vector_1, 
                rotate_vector_2, 
                path_arc = arg_z2, 
                arc_center = axes.c2p(0,0)
                ), 
            Transform(
                rotate_dot_1, 
                rotate_dot_2, 
                path_arc = arg_z2, 
                arc_center = axes.c2p(0,0)
                ),
            Transform(
                scale_label, 
                product_mag_label
                ), 
            FadeIn(arc_product_2),
            FadeIn(product_label)
            )


        # Highlight the addition of angles
        arc_product = Arc(radius=2, start_angle=0, angle=arg_product, color=RED, arc_center=axes.c2p(0, 0))
        angle_label = MathTex(r"\theta = \theta_1 + \theta_2").next_to(arc_product, .5*RIGHT + .5*UP)

        self.play(Create(arc_product_1), Create(arc_product_2), Create(arc_product), FadeIn(angle_label))

        # Pause to show the result
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(
                z1_vector, 
                z1_dot, 
                z2_vector, 
                z2_dot, 
                arc_product, 
                arc_product_1, 
                arc_product_2, 
                scale_dot, 
                scale_label,
                rotate_dot_1, 
                rotate_dot_2, 
                rotate_vector_1, 
                rotate_vector_2, 
                scale_vector, 
                angle_label, 
                product_mag_label, 
                product_label, 
                axes
                )
            )