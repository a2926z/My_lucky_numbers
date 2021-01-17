def split(word):
    return [char.upper() for char in word]

word = ""

print([x for x in split(word) if x != ' '])


def wordnums(word):
    sum = 0
    for letter in split(word):
        if letter == ' ':
            sum = sum + 0
        if letter == 'Α':
            sum = sum + 1
        if letter == 'Ά':
            sum = sum + 1
        if letter == 'Β':
            sum = sum + 2
        if letter == 'Γ':
            sum = sum + 3
        if letter == 'Δ':
            sum = sum + 4
        if letter == 'Ε':
            sum = sum + 5
        if letter == 'Έ':
            sum = sum + 5
        if letter == 'ΣΤ':
            sum = sum + 6
        if letter == 'Ζ':
            sum = sum + 7
        if letter == 'Η':
            sum = sum + 8
        if letter == 'Ή':
            sum = sum + 8
        if letter == 'Θ':
            sum = sum + 9
        if letter == 'Ι':
            sum = sum + 10
        if letter == 'Ί':
            sum = sum + 10
        if letter == 'Κ':
            sum = sum + 20
        if letter == 'Λ':
            sum = sum + 30
        if letter == 'Μ':
            sum = sum + 40
        if letter == 'Ν':
            sum = sum + 50
        if letter == 'Ξ':
            sum = sum + 60
        if letter == 'Ο':
            sum = sum + 70
        if letter == 'Ό':
            sum = sum + 70
        if letter == 'Π':
            sum = sum + 80
        if letter == 'Ρ':
            sum = sum + 100
        if letter == 'Σ':
            sum = sum + 200
        if letter == 'Τ':
            sum = sum + 300
        if letter == 'Υ':
            sum = sum + 400
        if letter == 'Ύ':
            sum = sum + 400
        if letter == 'Φ':
            sum = sum + 500
        if letter == 'Χ':
            sum = sum + 600
        if letter == 'Ψ':
            sum = sum + 700
        if letter == 'Ω':
            sum = sum + 800
        if letter == 'Ώ':
            sum = sum + 800
    print("Το όνομα σας αντιστοιχεί στον αριθμό: " + format(sum, "3,d"))
    return sum


wordnums(word)