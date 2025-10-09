
from fit2gpx import Converter
import warnings
warnings.filterwarnings("ignore", category=UserWarning)



if __name__ == "__main__":
    conv = Converter()
    gpx = conv.fit_to_gpx(f_in='1.fit', f_out='1.gpx')
