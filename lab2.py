# -------    IMPORTS AND FUNCTIONS   ------- #
import math


def vsub(one, two):                          # subtract two vectors
	return (one[0] - two[0], one[1] - two[1])

def vmag(r):                                 # magnitude of a vector
	return math.sqrt(r[0] * r[0] + r[1] * r[1])

def vadd(one, two):                          # add vectors
	return (one[0] + two[0], one[1] + two[1])

def vmuls(v, s):                             # vector times scalar
	return (v[0] * s, v[1] * s)


# ------- CONSTANTS AND FIXED VALUES ------- #

CONST_k = 8.99e9                             # coulomb's constant
CONST_g = 9.81                               # gravitational acceleration
CONST_segment_count = 200                    # segments per tape

tape_len = 0.16                              # 16cm
tape_mass = tape_len * 0.001                 # 1 gram per meter

tape_y_sep = 0.01                            # 1cm

tape_charge = 4.176314377505037e-09          # calculated in the first lab

dX = tape_len / CONST_segment_count          # space between tape segments

dQ = tape_charge / CONST_segment_count       # charge on each segment

# -------          PROGRAM            -------#


def do_get_eforce(): # calculate the electrical force between tapes given the parameters
	totalForce = (0, 0) # electrical force
	for lower_segment in range(0, CONST_segment_count):
		lower_seg_pt = (lower_segment * dX, 0)
		for upper_segment in range(0, CONST_segment_count):
			upper_seg_pt = (upper_segment * dX, tape_y_sep)
			r = vsub(upper_seg_pt, lower_seg_pt) # distance between upper and lower segment
			f = vmuls(r, CONST_k * dQ * dQ / (vmag(r) ** 3)) # coulomb's law
			totalForce = vadd(totalForce, f)
	return totalForce

totalForce = do_get_eforce()

print("\033[32;1m=== initial data (based on lab 1) ===\033[0m")
print("Total force vector on top tape:", totalForce)
fMag = vmag(totalForce)
gMag = CONST_g * tape_mass
wrong = math.sqrt(gMag / fMag)
print("Magnitude of force vector:", fMag)
print("Magnitude of gravitational force:", gMag)
print("\033[32;1m=== charge is off by a factor of about", str(wrong) + ",", "adjusting ===\033[0m")
tape_charge *= wrong # because force is proportional to charge^2, not charge
dQ = tape_charge / CONST_segment_count
print("Adjusted tape charge:", tape_charge)
print("New force magnitude:", vmag(do_get_eforce()))

