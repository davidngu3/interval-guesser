import random

notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
intervals = ['Octave/Unison', 'Minor second', 'Major second', 'Minor third', 'Major third', 'Perfect fourth', 'Tritone', 'Perfect fifth', 'Minor sixth', 'Major sixth', 'Minor Seventh', 'Major seventh']

if __name__ == '__main__':
    while True:
        # select 2 random indices from 0-10 inclusive and index their notes
        idx1 = random.randint(0, 10)
        idx2 = random.randint(0, 10)
        note1 = notes[idx1]
        note2 = notes[idx2]

        # print the question
        ans = input(f"How many semitones are there between {note1} and {note2}? Type 'q' to quit. \n")
        if ans == 'q':
            print("Thanks for playing! Exiting...\n")
            break

        # calculate the answer:
        # case 1: note 2 > note 1 then just take difference in index
        # case 2: note 1 > note 2, add 12 to note2 first (i.e. move lower note up an octave)
        if idx1 > idx2:
            idx2 += 12
        correctAns = idx2 - idx1 

        # compare answer against user input
        if ans == str(correctAns):
            print("Correct! ")
        else:
            print("Incorrect. ")
            
        # print correct information, along with interval name
        print(f"There are {str(correctAns)} semitones between {note1} and {note2}")
        print(f"This interval is also called a {intervals[correctAns]}\n")



