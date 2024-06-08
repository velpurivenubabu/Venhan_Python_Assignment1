def find_frequency_letters(input_string):
    frequency_dect= {}
    for i in input_string:
        if i in frequency_dect:
            frequency_dect[i] += 1
        else:
             frequency_dect[i] = 1
    return frequency_dect
print("Enter the string")
input_string = input()
print(find_frequency_letters(input_string))
