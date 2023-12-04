import read_fcns as f

if __name__ == "__main__":
    input = f.read_as_text("day01.txt")
    sum = 0
    for row in input:
        numerals = []
        row = row.replace("one", "one1one")
        row = row.replace("two", "two2two")
        row = row.replace("three", "three3three")
        row = row.replace("four", "four4four")
        row = row.replace("five", "five5five")
        row = row.replace("six", "six6six")
        row = row.replace("seven", "seven7seven")
        row = row.replace("eight", "eight8eight")
        row = row.replace("nine", "nine9nine")
        for element in row:
            if element.isnumeric():
                numerals += element
        sum += int(numerals[0]+numerals[-1])
    print(sum)
