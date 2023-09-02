class Data:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def interpolate(f: list, xi: int, n: int) -> float:

	result = 0.0
	for i in range(n):

		term = f[i].y
		for j in range(n):
			if j != i:
				term = term * (xi - f[j].x) / (f[i].x - f[j].x)

		result += term

	return result

if __name__ == "__main__":
	# nhap data
	#f = [Data(,), Data(,), Data(,), Data(,), Data(,)]
	f = [Data(0,0), Data(1.5,0.682), Data(2,0.841)]
	# nhap gia tri can tinh, so du lieu cho truoc
	print("Value of is :", interpolate(f, 1, 3))

