from scipy import interpolate

def f(x):
    x_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y_points = [54.4, 54.6, 67.1, 78.3, 85.3, 88.7, 96.9, 97.6, 84.1, 80.1, 68.8, 61.1]

    tck = interpolate.splrep(x_points, y_points)
    return interpolate.splev(x, tck)

print(f(3.5))