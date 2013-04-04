#!/usr/bin/env python2.7
import httplib2
import time

def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
   """Converts an integer to a base36 string."""
   if not isinstance(number, (int, long)):
       raise TypeError('number must be an integer')

   base36 = ''
   sign = ''

   if number < 0:
       sign = '-'
       number = -number

   if 0 <= number < len(alphabet):
       return sign + alphabet[number]

   while number != 0:
       number, i = divmod(number, len(alphabet))
       base36 = alphabet[i] + base36

   return sign + base36

def base36decode(number):
   return int(number, 36)


# let's allocate two A4s, 2.5cmx2.5cm, 88 pieces x 2 = 196
# when START == END means - that all urls up to START has been issued
START = 196
END = 196

if START >= END:
  print "wololo, you should issue new codes"

F = ["http://48.io/qr/%s" % (base36encode(x)) for x in range(START, END)]
#print F

curls = map(lambda x: "http://research.swtch.com/qr/draw?i=1c37805501b6127af881e31685b9dd0a&u=%s&m=2&x=-3&y=-8&v=8&c=0&r=0&d=0&t=1&s=985097826&z=-5&o=3" % x, F)
#print curls

count = 0

for c in curls:
  print c
  resp, content = httplib2.Http().request(c)
  print resp
  print "#############"
  with open("out/i"+base36encode(count+START)+".html", "w+") as f:
      f.write(content)
  print str(count)+" of "+str(END-START)

#  time.sleep(3)
  count += 1

