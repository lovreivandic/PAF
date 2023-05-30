import harmonic_oscillator as h_o

oscilator = h_o.HarmonicOscillator(m=1.2, k=2, x0=0, v0=6.7, dt=0.01, t=20)
period = oscilator.period_titranja()
print("Period titranja: ", period)