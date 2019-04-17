import gen
#ngen, popsize, gen_max, mut_min, mut_max, mutpb, mutgenpb, elite_inst, stop_rand, rand_inst
outFile = open('output.txt', 'w')
avg = 0

ngen = 5
for popsize in range(20, 41, 5):
	for gen_max in range(70, 101, 10):
		for mut_max in range(2, 5):
			mut_min = -mut_max
			for mutpb in range(1, 4):
				for mutgenpb in range(1, 4):
					for elite_inst in range(1,3):
						for stop_rand in range(7,11):
							for rand_inst in range(1,4):
								data = [ngen, popsize, gen_max, mut_min, mut_max, mutpb/10.0, mutgenpb/10.0, elite_inst/10.0, stop_rand/10.0, elite_inst/10.0]
								data_p = " ".join([str(i) for i in data])

								outFile.write(data_p)
								outFile.write('\n')
								avg = 0
								for i in range(50):
									a, b = gen.main(ngen, popsize, gen_max, mut_min, mut_max, mutpb/10.0, mutgenpb/10.0, elite_inst/10.0, stop_rand/10.0, elite_inst/10.0)
									avg += b
									if b == 0:
										outFile.write(str(a)+'\n')										

								print(avg/50)
								outFile.write(str(avg/50)+'\n')
								outFile.write('__________________________________________________'+'\n')

								
outFile.close()