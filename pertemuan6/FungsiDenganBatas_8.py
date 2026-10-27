def fibonacci(n):
    if n == 0 or n == 1:  # BASE CASES
        return n
    else:                 # RECURSIVE CASE (Panggilan Ganda)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Contoh pemanggilan fungsi dengan batas 8
batas = 8
print(f"Masukan Batas Deret Bilangan Fibonacci : {batas}")
print("Deret Fibonacci:")
for i in range(batas):
    print(fibonacci(i), end=" ")