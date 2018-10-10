# x =input("Put a number")
# print("a")

# if int(x) <= 10:
#     print("b")
# else:
#     print("c")
    
# print("d")
# print("e")
 
# x = 8

# if x % 3 == 0:
#     if x > 10:
#         if x ==15:
#             print("Ooooh! 15!!!")
#         else:
#             print("Boring")
        
#     else:
#         print("B")
# else:
#     print("C")
# print("Done")

# x=3
# print("A")

# i=0
# while i < x:
#     print("B")
#     i += 1
# print("C")
# print("D")
# print("E")

# x = input("Enter a number: ")
# y = input("Enter another number: ")
# x = int(x)
# y = int(y)
# print(x+y)

# num = [1, 2, 3, 4]
# for x in num:
#     for y in num:
#         print(x+y)


# "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the #multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."


# i=1
# while i<=100:
#     if (i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
    
#     else:
#         print(i)
#     i+=1
# num = range(1, 101)

# for x in num:
#       if (x % 3 == 0 and x % 5 == 0):
#           print("FizzBuzz")
          
#       elif x % 3 == 0:
#         print("Fizz")
#       elif x % 5 == 0:
#         print("Buzz")
    
#       else:
#         print(x)

# nums = range(1, 1001)
# print(sum(nums))

# l = [i*2 for i in range(10)]
# print(l)

# d = {
#     "Tom": 21,
#     "mary" : 25,
#     "ann": 20,
# }

# x = d.get("age",0)

# print(x)

# m = {
#      "name":"John",
#      "nationalety":"Irish",
#     "instruments":[{"name": "Violin","proficiency":98,},
                   # {"name": "Violin","proficiency":98,}]
     
# }

# print(m)

beatles ={ "John":{"nationalety":"English","instruments":{"guitar":56,
                                                        "drums":49}},
           "Ringo":{"nationalety":"English","instruments":{"drums":42,
                                                         "bass":35,}},
           "Paul":{"nationalety":"English","instruments": {"guitar":28,
                                                         "bass":8,}},
           "George":{"nationalety":"English","instruments":{"bass":21,
                                                        "guitar":15,}}
}

# for b in beatles:
#         # print(b.get("name"))
#         if (b["name"]) =="Paul":
#             print(b["instrument"])
# print(beatles["Paul"]["instruments"]["drums"])


# musician =beatles["Paul"]

# instruments =musician["instruments"]
# guitar_prof = instruments.get("drums", 0)
# print(guitar_prof)

# def show_instrument_proficiency(name):
#     musician = beatles[name]

#     instruments = musician["instruments"]

#     if "name" in musician:
#         print(musician['name'])
#     print("----------")
#     for i, p in instruments.items():
#         print("Proficiency in {0} is {1}".format(i, p))    
    
# show_instrument_proficiency("George")

    


























    
      















































