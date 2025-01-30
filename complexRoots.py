from manim import *
import numpy as np

class TransitionRootsSimultaneous(Scene):
    def construct(self):
        # Define parameters
        c = complex(3,3)  # The complex number
        n = 5  # Number of roots (e.g., 5th roots)

        # Calculate magnitude and argument of the complex number
        magnitude = abs(c)
        angle = np.angle(c)  # Argument of c in radians
        # Radius of the circle for the final roots
        root_radius = magnitude ** (1 / n)
        # Extract real and imaginary parts
        real_part = c.real
        imag_part = c.imag


        # Add axes
        axes = ComplexPlane().add_coordinates()
        self.play(Create(axes))


        # Plot the original complex number
        original_dot = Dot(axes.c2p(c.real, c.imag), color=GREEN)
        
        # Determine how to display the number
        if real_part == 0 and imag_part == 0:
            # Case: 0
            formatted_c = "0"
        elif real_part == 0:
            # Case: Pure imaginary number
            formatted_c = f"{imag_part}i"
        elif imag_part == 0:
            # Case: Pure real number
            formatted_c = f"{real_part}"
        elif imag_part > 0:
            # Case: General case with positive imaginary part
            formatted_c = f"{real_part} + {imag_part}i"
        else:
            # Case: General case with negative imaginary part
            formatted_c = f"{real_part} - {-imag_part}i"

        # Display the formatted complex number
        original_label = MathTex(f"c = {formatted_c}").next_to(original_dot, RIGHT)
        
        self.play(FadeIn(original_dot), Write(original_label))
        
        # Draw the unit circle for the roots of unity
        unit_circle = Circle(radius=1, color=BLUE)
        self.play(Create(unit_circle))
        
        # Calculate and plot the nth roots of unity
        unity_roots = []
        unity_dots = []
        unity_radii = []
        for k in range(n):
            # Roots of unity are evenly spaced on the unit circle
            root_angle = 2 * np.pi * k / n
            root = complex(np.cos(root_angle), np.sin(root_angle))
            unity_roots.append(root)
            
            # Plot root
            dot = Dot(axes.c2p(root.real, root.imag), color=YELLOW)
            unity_dots.append(dot)
            self.play(FadeIn(dot), run_time=0.2)
            
            # Add radius line
            radius = Line(axes.c2p(0, 0), axes.c2p(root.real, root.imag), color=YELLOW)
            unity_radii.append(radius)
            self.play(Create(radius), run_time=0.2)
        
        # Pause before transition
        self.wait(1)
        
        # Draw the final circle for the roots of the complex number
        final_circle = Circle(radius=root_radius, color=GREEN)
        self.play(Create(final_circle))
        
        # Calculate the nth roots of the complex number
        final_roots = []
        final_positions = []
        for k in range(n):
            # Roots of the complex number
            root_angle = angle / n + 2 * np.pi * k / n  # Add the phase shift
            root = root_radius * complex(np.cos(root_angle), np.sin(root_angle))
            final_roots.append(root)
            final_positions.append(axes.c2p(root.real, root.imag))
        
        # Animate all dots and radii simultaneously
        dot_animations = [dot.animate.move_to(final_pos) for dot, final_pos in zip(unity_dots, final_positions)]
        radius_animations = [
            Transform(unity_radius, Line(axes.c2p(0, 0), final_pos, color=GREEN))
            for unity_radius, final_pos in zip(unity_radii, final_positions)
        ]
        self.play(*dot_animations, *radius_animations, run_time=2)
        
        # Pause to show the final configuration
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(unit_circle, final_circle, *unity_dots, *unity_radii, axes))