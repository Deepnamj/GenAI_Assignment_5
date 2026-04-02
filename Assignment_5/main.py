#task 1
import math_utils as mu
print("Task 1")
print("Addition : 5 +3 =", mu.add(5, 3))
print("Subtraction : 10-5 =", mu.subtract(10, 5))
print("Square of 5:", mu.square(5))

#task 2
import string_utils as st
print("\nTask 2")
text = "hello world"
print("Capitalized:", st.capitalize_words(text))
print("Reversed:", st.reverse_string(text))
print("Word Count:", st.word_count(text))

#task 3
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax
print("\nTask 3")
print("Price after 10% disc on 200:", disc.apply_discount(200, 10))
print("Price after flat disc on 200:", disc.flat_discount(200))
print("Total price:", calculate_total([100, 200, 300]))
print("Price after tax on 500:", apply_tax(500))