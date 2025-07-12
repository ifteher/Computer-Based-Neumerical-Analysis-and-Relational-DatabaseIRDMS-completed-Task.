Simpson’s 3/8 Rule is another numerical integration method, best suited when the number of intervals 
𝑛
n is a multiple of 3.

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
3
ℎ
8
[
𝑓
(
𝑎
)
+
3
𝑓
(
𝑥
1
)
+
3
𝑓
(
𝑥
2
)
+
2
𝑓
(
𝑥
3
)
+
3
𝑓
(
𝑥
4
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
 f(x)dx≈ 
8
3h
​
 [f(a)+3f(x 
1
​
 )+3f(x 
2
​
 )+2f(x 
3
​
 )+3f(x 
4​
 )+⋯+f(b)]
Where,
ℎ
=
𝑏
−
𝑎
𝑛
h= 
n
b−a
​
def f(x):
    return x * x  # মূল ফাংশন f(x) = x^2

# 🔷 Trapezoidal Rule
def trapezoidal(a, b, n):
    h = (b - a) / n  # h = প্রতিটি ভাগের প্রস্থ (step size)
    result = f(a) + f(b)  # f(a) ও f(b) যোগ করা হচ্ছে

    for i in range(1, n):
        result += 2 * f(a + i * h)  # মাঝের মানগুলো ২ গুণ করে যোগ

    return (h / 2) * result  # চূড়ান্ত মান h/2 দিয়ে গুণ

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

# 🔷 Simpson's 3/8 Rule
def simpsons_three_eighth(a, b, n):
    if n % 3 != 0:
        print("Simpson's 3/8 Rule-এর জন্য n অবশ্যই ৩-এর গুণিতক হতে হবে।")
        return -1
    
    h = (b - a) / n  # h = step size
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            result += 2 * f(x)  # ৩-এর গুণিতক হলে ২ গুণ করে যোগ
        else:
            result += 3 * f(x)  # অন্য সব ক্ষেত্রে ৩ গুণ করে যোগ

    return (3 * h / 8) * result


# 🔷 Main Program
a = float(input("Enter lower limit a: "))  # a = সমাকলনের নিচের সীমা (lower limit)
b = float(input("Enter upper limit b: "))  # b = সমাকলনের উপর সীমা (upper limit)
n = int(input("Enter number of intervals n: "))  # n = কত ভাগে বিভক্ত করবে (number of subintervals)

# 🔷 ফলাফল দেখানো হবে
print("\nResults:")

trap = trapezoidal(a, b, n)  # Trapezoidal Rule প্রয়োগ
print(f"Trapezoidal Rule Result: {trap:.6f}")

sim13 = simpsons_one_third(a, b, n)  # Simpson's 1/3 Rule প্রয়োগ
if sim13 != -1:
    print(f"Simpson's 1/3 Rule Result: {sim13:.6f}")

sim38 = simpsons_three_eighth(a, b, n)  # Simpson's 3/8 Rule প্রয়োগ
if sim38 != -1:
    print(f"Simpson's 3/8 Rule Result: {sim38:.6f}")
