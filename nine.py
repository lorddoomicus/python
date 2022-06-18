#!env python
#
# Shows the relationship between the sum of digits of an arbritrary number and '9'
#
# This is licensed for use under the GNU General Pulbic License v2
#
# 2015-10-27	dwalker	Initial Version
# 2020-11-14    dwalker Updated to run under Python3 under Pyenv
#

import sys

def usage():

	print( "Usage: nine <integer>" )
	sys.exit(1)

### End of usage function ###

#
# This takes in an int, and the add method then adds the digits of that int
# and returns it's value
#
class addem:

	ints = []

	def __init__( self, num ):

		addem.ints = list ( map( int, str( num )) )


	def add( self ):

		sum = 0

		for i in range( 0, len( addem.ints )):
			sum += addem.ints[i]

		return sum

### End of class addem
	
if len(sys.argv) == 2:
	try:
		n = int( sys.argv[1] )
	except:
		err = sys.argv[1]
		print( "ERRR!!!:{} is not a valid number!" .format( err ))
		usage()

else:	# len( sys.argv ) >=2
		print( "ERRR!!!" )
		usage()


sum = addem( n ).add()		# add digits
diff = n - sum			# subtract from original number
nine = addem( diff ).add() 	# add the resulting digits

print( "num = ", n, ", sum = ", sum, ", diff = ", diff,  ", nine = ", nine )
