import numpy.random as rnd
rnd.seed(0)

rnd.uniform(low = 0.0, high = 1.0, size = None)
rnd.rand(2,3)
rnd.randint(low = 0, high = 9, size = None)
rnd.normal(loc = 0.0, scale = 1.0, size = None)
rnd.randn(2,3)
rnd.binomial(n = 4, p = 0.5, size = None)

selection = rnd.binomial(1,p = 0.5 ,size = len()).astype(bool)
