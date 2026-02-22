def quicksort(s):
    if len(s) <= 1:
        return s
    else:
        pivot = s[0]
        s1 = [x for x in s[1:] if x < pivot]
        s2 = [x for x in s[1:] if x >= pivot]
        if __name__ == '__main__':
            print ("Ich sortiere: ", s)
            print('Aufspaltung:', s1, pivot, s2)
            return quicksort(s1) + [pivot] + quicksort(s2)

if __name__ == '__main__':
    s = [17, 7, 85, 15, 11, 20, 9, 5, 87]
    print ('Sortierte Liste:', quicksort(s))


""" 
Ich sortiere:  [17, 7, 85, 15, 11, 20, 9, 5, 87]
Aufspaltung: [7, 15, 11, 9, 5] 17 [85, 20, 87]
Ich sortiere:  [7, 15, 11, 9, 5]
Aufspaltung: [5] 7 [15, 11, 9]
Ich sortiere:  [15, 11, 9]
Aufspaltung: [11, 9] 15 []
Ich sortiere:  [11, 9]
Aufspaltung: [9] 11 []
Ich sortiere:  [85, 20, 87]
Aufspaltung: [20] 85 [87]
Sortierte Liste: [5, 7, 9, 11, 15, 17, 20, 85, 87]
 """