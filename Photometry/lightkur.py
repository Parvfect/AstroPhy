
import lightkurve as lk

pixels = lk.search_targetpixelfile('Kepler-10').download()
pixels.plot()

lightcurve = pixels.to_lightcurve()
lightcurve.plot()