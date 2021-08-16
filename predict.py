import cog
from pathlib import Path
from models.colorize import Colorizer

class InstColorizationPredictor(cog.Predictor):
    def setup(self):
        self.colorizer = Colorizer()

    @cog.input("input", type=Path, help="grayscale input image")
    def predict(self, input):
        output_path = self.colorizer.colorize(input)
        return output_path
