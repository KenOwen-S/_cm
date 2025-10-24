import math

# ---------------------------
# 定義基本幾何物件
# ---------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def scale(self, sx, sy, origin=None):
        if origin is None:
            origin = Point(0, 0)
        return Point(origin.x + (self.x - origin.x) * sx,
                     origin.y + (self.y - origin.y) * sy)

    def rotate(self, angle_deg, origin=None):
        if origin is None:
            origin = Point(0, 0)
        angle_rad = math.radians(angle_deg)
        x_shifted = self.x - origin.x
        y_shifted = self.y - origin.y
        x_new = x_shifted * math.cos(angle_rad) - y_shifted * math.sin(angle_rad)
        y_new = x_shifted * math.sin(angle_rad) + y_shifted * math.cos(angle_rad)
        return Point(x_new + origin.x, y_new + origin.y)

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"


class Line:
    # Ax + By + C = 0
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    @classmethod
    def from_points(cls, p1, p2):
        A = p2.y - p1.y
        B = p1.x - p2.x
        C = -(A * p1.x + B * p1.y)
        return cls(A, B, C)

    def intersection(self, other):
        D = self.A * other.B - other.A * self.B
        if D == 0:
            return None  # 平行
        Dx = -self.C * other.B + other.C * self.B
        Dy = -self.A * other.C + other.A * self.C
        return Point(Dx / D, Dy / D)

    def perpendicular_through(self, point):
        # Ax + By + C = 0 -> perpendicular line through point
        A_perp = self.B
        B_perp = -self.A
        C_perp = -(A_perp * point.x + B_perp * point.y)
        return Line(A_perp, B_perp, C_perp)

    def __repr__(self):
        return f"Line({self.A}x + {self.B}y + {self.C} = 0)"


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def intersection_with_line(self, line):
        # 用參數法解方程
        x0, y0 = self.center.x, self.center.y
        r = self.radius
        A, B, C = line.A, line.B, line.C
        points = []
        if B != 0:
            # y = (-A x - C)/B
            # (x - x0)^2 + (y - y0)^2 = r^2
            a = 1 + (A/B)**2
            b = 2*A*C/(B**2) + 2*A*B*y0/(B**2) - 2*x0
            c = x0**2 + (C + B*y0)**2 / (B**2) - r**2
            disc = b**2 - 4*a*c
            if disc < 0:
                return []
            x1 = (-b + math.sqrt(disc)) / (2*a)
            x2 = (-b - math.sqrt(disc)) / (2*a)
            y1 = (-A*x1 - C)/B
            y2 = (-A*x2 - C)/B
            points.append(Point(x1, y1))
            if disc > 0:
                points.append(Point(x2, y2))
        else:  # B=0 -> x = -C/A
            x = -C/A
            delta = r**2 - (x - x0)**2
            if delta < 0:
                return []
            y1 = y0 + math.sqrt(delta)
            y2 = y0 - math.sqrt(delta)
            points.append(Point(x, y1))
            if delta > 0:
                points.append(Point(x, y2))
        return points

    def intersection_with_circle(self, other):
        # (x-x0)^2 + (y-y0)^2 = r^2
        # (x-x1)^2 + (y-y1)^2 = r1^2
        x0, y0, r0 = self.center.x, self.center.y, self.radius
        x1, y1, r1 = other.center.x, other.center.y, other.radius
        dx = x1 - x0
        dy = y1 - y0
        d = math.hypot(dx, dy)
        if d > r0 + r1 or d < abs(r0 - r1):
            return []  # 不相交
        a = (r0**2 - r1**2 + d**2) / (2*d)
        h = math.sqrt(r0**2 - a**2)
        xm = x0 + a*dx/d
        ym = y0 + a*dy/d
        xs1 = xm + h*dy/d
        ys1 = ym - h*dx/d
        xs2 = xm - h*dy/d
        ys2 = ym + h*dx/d
        if h == 0:
            return [Point(xs1, ys1)]
        return [Point(xs1, ys1), Point(xs2, ys2)]

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

# ---------------------------
# 定義三角形物件
# ---------------------------
class Triangle:
    def __init__(self, p1, p2, p3):
        self.vertices = [p1, p2, p3]

    def translate(self, dx, dy):
        return Triangle(*(v.translate(dx, dy) for v in self.vertices))

    def scale(self, sx, sy, origin=None):
        return Triangle(*(v.scale(sx, sy, origin) for v in self.vertices))

    def rotate(self, angle_deg, origin=None):
        return Triangle(*(v.rotate(angle_deg, origin) for v in self.vertices))

    def __repr__(self):
        return f"Triangle({self.vertices[0]}, {self.vertices[1]}, {self.vertices[2]})"


# ---------------------------
# 驗證畢氏定理
# ---------------------------
def verify_pythagoras(line, external_point):
    perp_line = line.perpendicular_through(external_point)
    foot = line.intersection(perp_line)
    a = external_point.distance_to(foot)
    b = foot.distance_to(Point(line.A, line.B))  # 隨便取線上點
    c = external_point.distance_to(Point(line.A, line.B))
    print(f"Right triangle sides: a={a:.2f}, b=?, c={c:.2f}")
    # 這裡可以計算實際三角形邊長
    return a, foot

# ---------------------------
# 範例使用
# ---------------------------
if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    line = Line.from_points(p1, p2)
    external = Point(2, 3)

    print("Line:", line)
    perp = line.perpendicular_through(external)
    print("Perpendicular line through external point:", perp)
    foot = line.intersection(perp)
    print("Foot of perpendicular:", foot)

    circle1 = Circle(Point(0,0), 5)
    circle2 = Circle(Point(4,0), 3)
    print("Circle-circle intersections:", circle1.intersection_with_circle(circle2))

    tri = Triangle(Point(0,0), Point(3,0), Point(3,4))
    print("Original triangle:", tri)
    print("Triangle rotated 90 deg:", tri.rotate(90))
    print("Triangle translated:", tri.translate(1,2))
