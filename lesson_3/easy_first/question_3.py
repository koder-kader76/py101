# Question 3

# Starting with the string:

# Show two different ways to create a new string with "Four score 
# and " prepended to the front of the string referenced by 
# famous_words.

# first method: string interpolation
famous_words = "seven years ago..."
print(f"Four Score and {famous_words}")

# second method: string concatenation
famous_words = "Four Score and " + famous_words
print(famous_words)

# third method: string format
print("Four score and {famous_words}".format(
                    famous_words="seven years ago..."))


# using string format email
template = (
"""Dear {customer},

Thank you for your recent purchase of {product}.

Remember, our support team is always here to assist you.

Best regards,
{employee}"""
)

print(
    template.format(
        customer="Bob",
        product="Canon EOS R5",
        employee="Kate"
    )
)

# Dear Bob,

# Thank you for your recent purchase of Canon EOS R5.

# Remember, our support team is always here to assist you.

# Best regards,
# Kate