from manim import *
import numpy as np

class TransitionRoots(Scene):
    def construct(self):
        # Define parameters
        c = complex(2, 2)  # The complex number
        n = 5  # Number of roots (e.g., 5th roots)
        
        # Calculate magnitude and argument of the complex number
        magnitude = abs(c)
        angle = np.angle(c)  # Argument of c in radians
        
        # Radius of the circle for the final roots
        root_radius = magnitude ** (1 / n)
        
        # Add axes
        axes = ComplexPlane().add_coordinates()
        self.play(Create(axes))
        
        # Draw the unit circle for the roots of unity
        unit_circle = Circle(radius=1, color=BLUE)
        self.play(Create(unit_circle))
        
        # Calculate and plot the nth roots of unity
        unity_roots = []
        unity_dots = []
        for k in range(n):
            # Roots of unity are evenly spaced on the unit circle
            root_angle = 2 * np.pi * k / n
            root = complex(np.cos(root_angle), np.sin(root_angle))
            unity_roots.append(root)
            dot = Dot(axes.c2p(root.real, root.imag), color=YELLOW)
            unity_dots.append(dot)
            self.play(FadeIn(dot), run_time=0.2)
        
        # Pause before transition
        self.wait(1)
        
        # Draw the final circle for the roots of the complex number
        final_circle = Circle(radius=root_radius, color=GREEN)
        self.play(Create(final_circle))
        
        # Calculate the nth roots of the complex number
        final_roots = []
        final_dots = []
        for k in range(n):
            # Roots of the complex number
            root_angle = angle / n + 2 * np.pi * k / n  # Add the phase shift
            root = root_radius * complex(np.cos(root_angle), np.sin(root_angle))
            final_roots.append(root)
        
        # Animate twisting and scaling
        for unity_dot, final_root in zip(unity_dots, final_roots):
            final_position = axes.c2p(final_root.real, final_root.imag)
            self.play(unity_dot.animate.move_to(final_position), run_time=1)
        
        # Pause to show the final configuration
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(unit_circle, final_circle, *unity_dots, axes))