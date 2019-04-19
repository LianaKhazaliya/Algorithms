import gen
#ngen, popsize, gen_max, mut_min, mut_max, mutpb, mutgenpb, elite_inst, stop_rand, rand_inst
avg = 0


for i in range(100):
	a, b = gen.main(5, 40, 2500, -5, 5, 0.1, 0.5, 0.3, 1, 0.4)
	avg += b
	if b == 0:
		outFile.write(str(a)+'\n')										

print(avg/100)
