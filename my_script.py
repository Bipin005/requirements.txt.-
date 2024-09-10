from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Create a square
        square = Square()
        square.set_fill(BLUE, opacity=0.5)  # Set the fill color and opacity
        square.set_stroke(WHITE, width=2)   # Set the border color and width
        
        # Create a circle
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)  # Set the fill color and opacity
        circle.set_stroke(WHITE, width=2)  # Set the border color and width
        
        # Position the shapes
        square.move_to(LEFT)
        circle.move_to(RIGHT)
        
        # Display the square
        self.play(Create(square))
        self.wait(1)
        
        # Transform the square into a circle
        self.play(Transform(square, circle))
        self.wait(1)

# To render the scene, use the command:
# manim -pql square_to_circle.py SquareToCircle
