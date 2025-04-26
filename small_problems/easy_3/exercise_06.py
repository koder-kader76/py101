# 6. Madlibs

# Madlibs is a simple game where you create a story template with 
# "blanks" for words. You, or another player, then construct a 
# list of words and place them into the story, creating an often 
# silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, a verb, 
# an adverb, and an adjective, and injects them into a story that 
# you create.

def get_word(word_type):
    return input(f"Enter a {word_type}: ").strip()


def madlibs():
    thing = get_word('noun')
    doing = get_word('verb')
    making = get_word('adjective')
    word = get_word('adverb')

    line = (
        f"Do you {doing} your {making} {thing} {word}? That's hilarious!\n"
        f"The {making} {thing} {doing}s {word} over the lazy {thing}.\n"
        f"The {thing} {word} {doing}s up to Joe's {making} turtle."
    )

    print(line)

madlibs()
