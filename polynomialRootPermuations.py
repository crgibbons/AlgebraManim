from manim import *
import numpy as np

class PolynomialRoots(Scene):
    def construct(self):
        # Add the title
        title = Text("Permutation by Conjugation").to_edge(UP)
        subtitle = MathTex(r"p(x) = x^5 + 3 x^3 - 7 x^2 - 21", font_size=24).next_to(title, DOWN, buff=0.2)
        self.play(Write(title), Write(subtitle))

        # Define the polynomial
        roots_x2_plus_3 = [complex(0, np.sqrt(3)), complex(0, -np.sqrt(3))]
        roots_x3_minus_7 = [
            7**(1/3),  # Real root
            7**(1/3) * complex(np.cos(2 * np.pi / 3), np.sin(2 * np.pi / 3)),  # 1st complex root
            7**(1/3) * complex(np.cos(4 * np.pi / 3), np.sin(4 * np.pi / 3)),  # 2nd complex root
        ]
        all_roots = roots_x2_plus_3 + roots_x3_minus_7

        # Create the complex plane
        axes = ComplexPlane(x_range=[-3.5, 3.5, 1], y_range=[-3.5, 3.5, 1])
        self.play(Create(axes))

        # Plot the roots as dots
        dots = []
        labels = []
        for i, root in enumerate(all_roots):
            dot = Dot(axes.c2p(root.real, root.imag), color=BLUE)
            dots.append(dot)
            label = MathTex(f"z_{i+1}").next_to(dot, UP, buff=0.2)
            labels.append(label)
            self.play(
                FadeIn(dot), 
                Write(label), 
                run_time=0.5
                )

        # Pause to show the original configuration
        self.wait(1)
        self.play(FadeOut(*labels))

        # Define a permutation (e.g., swap two roots)
        permuted_positions = [
            axes.c2p(roots_x2_plus_3[1].real, roots_x2_plus_3[1].imag),    # Root 1 -> Root 2
            axes.c2p(roots_x2_plus_3[0].real, roots_x2_plus_3[0].imag),    # Root 2 -> Root 1
            axes.c2p(roots_x3_minus_7[0].real, roots_x3_minus_7[0].imag),  # Root 3 stays put
            axes.c2p(roots_x3_minus_7[2].real, roots_x3_minus_7[2].imag),  # Root 4 -> Root 5
            axes.c2p(roots_x3_minus_7[1].real, roots_x3_minus_7[1].imag)   # Root 5 -> Root 4
            ]

        # Animate the permutation
        animations = []
        for dot, target_pos in zip(dots, permuted_positions):
            animations.append(dot.animate.move_to(target_pos))
        self.play(*animations, run_time=2)

        # Pause to show the permuted configuration
        self.wait(2)

        # Clean up
        self.play(FadeOut(*dots, axes))