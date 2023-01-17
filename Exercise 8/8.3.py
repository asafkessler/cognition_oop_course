def sameVowels(s1, s2):

    dict_1 = {"a":0,
              "e":0,
              "i":0,
              "o":0,
              "u":0,
              "A":0,
              "E":0,
              "I":0,
              "O":0,
              "U":0
              }

    dict_2 = {"a":0,
              "e":0,
              "i":0,
              "o":0,
              "u":0,
              "A":0,
              "E":0,
              "I":0,
              "O":0,
              "U":0
              }

    for curr in s1:
        if dict_1.keys().__contains__(curr):
            dict_1[curr] +=1
    for curr in s2:
        if dict_2.keys().__contains__(curr):
            dict_2[curr] += 1

    if dict_1 == dict_2:
        return True
    else:
        return False


if __name__ == "__main__":
   if sameVowels('aabcefiok', 'xcexvcxaioa'):
       print("True")
   else:
       print("False")