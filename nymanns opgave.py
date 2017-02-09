#-*- coding: utf-8 -*-

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#print "Sum of all natural numbers below 10, that are multiples of 3 or 5"
#yaya

def vardien_af_3_eller_5 ():
    for number in xrange(1000):
        if not number % 3 or not number % 5:
            yield number

x = sum(vardien_af_3_eller_5())
print "Summen er %s" % x