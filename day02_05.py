#Chapter 4: if 조건문

'''
print(bool(set()))
print(bool([]))
print(bool(""))
print(bool(dict()))
'''

letter="o"
if letter=="a" or letter=="e" or letter=="i"\
    or letter=="o" or letter=="u":
    print(letter,"is a vowel")
else:
    print(letter,"is not a vowel")


vowls="aeiou"
letter="u"
if letter in vowls:
    print(letter,"is a vowel")
else:
    print(letter,"is not a vowel")


limits=20
tweets="Pass"*6
diff_=limits-len(tweets)
if diff_>=0:
    print("A fitting tweet")
else:
    print(f"Went over by {abs(diff_)}")  #abs는 절대값 함수

