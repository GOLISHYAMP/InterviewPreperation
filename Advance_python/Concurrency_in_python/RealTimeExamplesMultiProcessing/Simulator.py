from multiprocessing import Pool
import random, time

def simulate_particle(particle_id):
    return sum(random.random() for _ in range(1000000))

if __name__ == "__main__":
    particles = range(100)
    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(simulate_particle, particles)
    # for i in particles:
    #     simulate_particle(i)
    print("time took : ", time.time()-start)
    # print(results)
