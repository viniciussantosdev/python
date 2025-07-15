import math
an = float(input('Digite o ângulo que você queira:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de {:.2f} tem o Seno de {:.2f}'.format(an,sen))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an,cos))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(an,tan))
