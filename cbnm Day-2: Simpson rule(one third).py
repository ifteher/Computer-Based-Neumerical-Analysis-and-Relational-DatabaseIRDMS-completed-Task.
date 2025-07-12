The Simpson’s 1/3 Rule is a more accurate method than the trapezoidal rule. It approximates the curve by a second-degree polynomial (parabola).
Note: 
𝑛
n must be even.

Formula:
∫
𝑎
𝑏
𝑓
(
𝑥
)
 
𝑑
𝑥
≈
ℎ
3
[
𝑓
(
𝑎
)
+
4
𝑓
(
𝑥
1
)
+
2
𝑓
(
𝑥
2
)
+
4
𝑓
(
𝑥
3
)
+
⋯
+
𝑓
(
𝑏
)
]
∫ 
a
b
​
 f(x)dx≈ 3/h[f(a)+4f(x1)+2f(x2)+4f(x3)+⋯+f(b)]
Where,
ℎ=(𝑏−𝑎)/𝑛



Python code:
# 🔷 Simpson's 1/3 Rule
def simpsons_one_third(a, b, n):
    if n % 2 != 0:
        print("Simpson's 1/3 Rule-এর জন্য n জোড় (even) হতে হবে।")
        return -1
    
    h = (b - a) / n  # h = step size
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 != 0:
            result += 4 * f(x)  # বিজোড় ইনডেক্স হলে ৪ গুণ করে যোগ
        else:
            result += 2 * f(x)  # জোড় ইনডেক্স হলে ২ গুণ করে যোগ

    return (h / 3) * result
