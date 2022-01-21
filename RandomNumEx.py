import random

def random_exclude(range_start, range_end, excludes):
	r = random.randint(range_start,range_end)
	while r in excludes:
		r = random.randint(range_start, range_end)
	return r

if __name__ == "__main__":
	ex = [2,5,8]
	for i in range(0,50):
		h = random_exclude(1,10,ex)
		print(h)
