from itertools import combinations

major_scale_ratios = [
    "1/1",  
    "9/8",  
    "5/4",  
    "4/3",  
    "3/2",  
    "5/3",  
    "15/8", 
    "2/1"
]

base_note = float(input())

notes = list()

for i in major_scale_ratios:
    numerador, denominator = i.split('/')
    note = round((base_note * float(numerador)) / float(denominator), 2)
    notes.append(note)


chords = list(combinations(notes, 3))

print(len(chords))

for i in chords:
    print(i)
