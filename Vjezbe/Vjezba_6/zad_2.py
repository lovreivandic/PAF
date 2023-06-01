from harmonic_oscillator import HarmonicOscillator

oscilator = HarmonicOscillator(m=1.2, k=2, x0=0, v0=6.7, dt=0.01, t=20.0)
period = oscilator.period_titranja()
print("Period titranja: {} s".format(period))