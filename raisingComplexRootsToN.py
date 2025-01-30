from manim import *
import numpy as np

class AnimateRootsRotatingRadii(Scene):
    def construct(self):
        # Define parameters
        c = complex(2, 2)  # The complex number
        n = 5  # Number of roots (e.g., 5th roots)

        # Calculate magnitude and argument of the complex number
        magnitude = abs(c)
        angle = np.angle(c)  # Argument of c in radians

        # Radius of the circle for the nth roots of c
        root_radius = magnitude ** (1 / n)

        # Add axes
        axes = ComplexPlane().add_coordinates()
        self.play(Create(axes))

        # Calculate the nth roots of the complex number
        roots = []
        for k in range(n):
            root_angle = angle / n + 2 * np.pi * k / n  # Add the phase shift
            root = root_radius * complex(np.cos(root_angle), np.sin(root_angle))
            roots.append(root)

        # Plot roots and connect to origin
        dots = []
        lines = []
        for root in roots:
            dot = Dot(axes.c2p(root.real, root.imag), color=YELLOW)
            dots.append(dot)
            line = Line(axes.c2p(0, 0), axes.c2p(root.real, root.imag), color=YELLOW)
            lines.append(line)
            self.play(FadeIn(dot), Create(line), run_time=0.5)

        # Pause before power animation
        self.wait(1)

        # Phase 1: Scale the magnitude by n
        scale_dots = []
        scale_lines = []
        scaled_positions = []
        for dot, line, root in zip(dots, lines, roots):
            # Scale magnitude by n
            scaled_root = n * root_radius * complex(
                np.cos(np.angle(root)), np.sin(np.angle(root))
            )
            scaled_positions.append(scaled_root)
            final_position = axes.c2p(scaled_root.real, scaled_root.imag)
            scale_dots.append(dot.animate.move_to(final_position))
            scale_lines.append(
                Transform(line, Line(axes.c2p(0, 0), final_position, color=BLUE))
            )
        self.play(*scale_dots, *scale_lines, run_time=2)

        # Phase 2: Rotate the argument by n
        rotate_dots = []
        rotating_lines = []
        for dot, line, scaled_root in zip(dots, lines, scaled_positions):
            # Rotate by n times the argument
            final_position = axes.c2p(c.real, c.imag)
            rotate_dots.append(dot.animate.move_to(final_position))
            
            # Create a line that rotates around the origin
            rotating_line = always_redraw(
                lambda: Line(axes.c2p(0, 0), dot.get_center(), color=GREEN)
            )
            self.add(rotating_line)
            rotating_lines.append(rotating_line)

        self.play(*rotate_dots, run_time=2)
        
        # Pause to show the final configuration
        self.wait(1)

        # Clean up
        self.play(FadeOut(*dots, *rotating_lines, axes))