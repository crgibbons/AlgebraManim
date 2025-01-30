from manim import *
import numpy as np

class SmoothRotation(Scene):
    def construct(self):
        # Define two complex numbers
        z1 = complex(2, 1)  # First complex number
        z2 = complex(1, -1)  # Second complex number

        # Compute their product
        z_product = z1 * z2

        # Extract magnitudes and arguments
        mag_z1 = abs(z1)
        mag_z2 = abs(z2)
        arg_z1 = np.angle(z1)
        arg_z2 = np.angle(z2)
        arg_product = np.angle(z_product)

        # Add axes
        axes = ComplexPlane().add_coordinates()
        self.play(Create(axes))

        # Plot z1
        z1_vector = Arrow(start=axes.c2p(0, 0), end=axes.c2p(z1.real, z1.imag), color=BLUE)
        z1_label = MathTex(r"z_1").next_to(axes.c2p(z1.real, z1.imag), UP)
        self.play(Create(z1_vector), Write(z1_label))

        # Plot z2
        z2_vector = Arrow(start=axes.c2p(0, 0), end=axes.c2p(z2.real, z2.imag), color=GREEN)
        z2_label = MathTex(r"z_2").next_to(axes.c2p(z2.real, z2.imag), UP)
        self.play(Create(z2_vector), Write(z2_label))

        # Step 1: Scale z1 by |z2|
        scaled_z1 = mag_z2 * z1
        scale_vector = Arrow(
            start=axes.c2p(0, 0), end=axes.c2p(scaled_z1.real, scaled_z1.imag), color=YELLOW
        )
        scale_label = MathTex(r"|z_2| \cdot z_1").next_to(axes.c2p(scaled_z1.real, scaled_z1.imag), UP)
        self.play(Transform(z1_vector, scale_vector), FadeIn(scale_label))

        # Step 2: Smooth rotation to z1 * z2
        radius = abs(scaled_z1)
        start_angle = np.angle(scaled_z1)
        target_angle = start_angle + arg_z2

        def rotate_vector(mob, alpha):
            """Updater for smooth rotation."""
            current_angle = start_angle + alpha * (target_angle - start_angle)
            new_endpoint = radius * complex(np.cos(current_angle), np.sin(current_angle))
            mob.put_start_and_end_on(
                axes.c2p(0, 0), axes.c2p(new_endpoint.real, new_endpoint.imag)
            )

        # Apply the updater for the rotation animation
        self.play(
            UpdateFromAlphaFunc(
                z1_vector,
                lambda mob, alpha: rotate_vector(mob, alpha),
            ),
            run_time=3,
        )

        # Update label for z1 * z2
        product_label = MathTex(r"z_1 \cdot z_2").next_to(axes.c2p(z_product.real, z_product.imag), UP)
        self.play(Write(product_label))

        # Pause to show the result
        self.wait(2)

        # Clean up
        self.play(FadeOut(z1_vector, z2_vector, scale_label, product_label, axes))