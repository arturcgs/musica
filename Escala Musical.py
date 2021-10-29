# This program will give you the musical scale after you choose a note

def main():

    def which_key(dictionary, search_value):
        ''' (dic, str) --> (int)
        Loops through a dictionary and returns the key
        correspondant to the search_value'''
        for key, value in dictionary.items():
            if value == search_value:
                return key

    def get_scale(steps, note):
        '''(dic, list, int) --> (list)
        Loops through a list in steps, adding the correspondant step
        to each note in the scale. Then checks if sharps or flats should be used'''
        #Forming the scale in sharps
        scale = []
        for i in steps:
            if note > 6.5:
                note -= 6
            scale.append(scale_sharp[note])
            note += i
        #Checking if sharps is good enough
        for i in range(1, 7):
            if scale[i-1][0] == scale[i][0]:
                #Forming the scale in flats
                scale = []
                for i in steps:
                    if note > 6.5:
                        note -= 6
                    scale.append(scale_flat[note])
                    note += i
                break
        #Checking if the first note is the same as the last
        if scale[0][0] == scale[6][0]:
            scale = []
            for i in steps:
                if note > 6.5:
                    note -= 6
                scale.append(scale_flat[note])
                note += i
        return scale

    def print_list(list):
        '''(list) --> prints
        Prints each item in the list'''
        for i in range(len(list)):
            print("%s | " % (list[i]), end='')
        print('\n')

    #Defining my scales and steps
    scale_sharp = {1: 'C', 1.5: 'C#', 2: 'D', 2.5: 'D#', 3: 'E', 3.5: 'F', 4: 'F#',
                   4.5: 'G', 5: 'G#', 5.5: 'A', 6: 'A#', 6.5: 'B'}
    scale_flat = {1: 'C', 1.5: 'Db', 2: 'D', 2.5: 'Eb', 3: 'E', 3.5: 'F', 4: 'Gb',
                   4.5: 'G', 5: 'Ab', 5.5: 'A', 6: 'Bb', 6.5: 'B'}
    scale_flat_upper = {1: 'C', 1.5: 'DB', 2: 'D', 2.5: 'EB', 3: 'E', 3.5: 'F', 4: 'GB',
                   4.5: 'G', 5: 'AB', 5.5: 'A', 6: 'BB', 6.5: 'B'}
    major_steps = [1, 1, 0.5, 1, 1, 1, 0.5]
    minor_steps = [1, 0.5, 1, 1, 0.5, 1, 1]

    #Informing the user
    print('''This program gives you the major or minor scale for a note of your choice.
To exit de program, simply type X anytime. Thank you!''')

    while True:
        # Asking for the Note
        note = input("Type the note you want the scale from: ")
        note = note.upper()
        if note == 'X':
            print("\nThank you very much!")
            break

        elif note in scale_sharp.values():  # checking the note's number Sharp
            note = which_key(scale_sharp, note)
        elif note in scale_flat_upper.values():  # checking the note's number Flat
            note = which_key(scale_flat_upper, note)
        else:
            print("\nThis is Not a Valid Note.\nPlease type a Valid Note.\n")
            continue

        #Asking for The Scale
        scale_choice = input("Do you want a Major or Minor scale? ")
        scale_choice = scale_choice.upper()

        if scale_choice == 'MAJOR':
            print("\nHere's your scale:\n")
            print_list(get_scale(major_steps, note))

            continue
        elif scale_choice == 'MINOR':
            print("\nHere's your scale:\n")
            print_list(get_scale(minor_steps, note))
            continue
        elif scale_choice == 'X':
            print("\nThank you very much!")
            break
        else:
            print('\nThis is not a viable scale.\nPlease type Major or Minor\n')
            continue

main()