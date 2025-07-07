m = float(input('Escolha um valor em metros: '))
c = m * 100
mm = m * 1000
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
print('Aqui está as conversões do seu valor:\n{}cm.\n{}mm.\n{}km.\n{}hm.\n{}dam.\n{}dm.'.format(
    c, mm, km, hm, dam, dm))
