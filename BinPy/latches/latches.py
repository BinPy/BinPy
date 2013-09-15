from BinPy import Gates
import sys

def rs_latch(R, S, Q = 0):
	'''
	This method implements a R-S Latch
	'''
	if(R==1 and S==1):
		sys.exit("ERROR: This combination of R and S is not allowed")

	Q = Gates().NOR(R,Gates().NOR(Q,S))

	return Q

def rs_latch_low(R, S, Q = 0):
	'''
	This method implements the low active R-S latch
	'''

	R_modified = Gates().NOT(R)
	S_modified = Gates().NOT(S)

	return rs_latch(R_modified, S_modified, Q)

def jk_latch(J, K, Q = 0):
	'''
	This method implements the J-K latch
	'''
	Q_comp = Gates().NOT(Q)
	K_comp = Gates().NOT(K)

	J_term = Gates().AND(J, Q_comp)
	K_term = Gates().AND(K_comp, Q)

	output = Gates().OR(J_term, K_term)

	return output
