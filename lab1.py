# LAB 1 Tyler Clarke
# Mathematical model for hovering tape
import math # get functions like sqrt


dist = float(input("Space between tapes (m): ")) # test value: 0.01m
tape_len = float(input("Tape len (m): ")) # test value: 0.15m

tape_mass = 0.001 * tape_len # 0.001 kilograms per meter times the length of the tape in meters = the weight of the tape

g = 9.8 * tape_mass # force of gravity: we know that the electrical force must be exactly the same as this, but in the opposite direction, at the target distance

k = 8.99e9 # coulomb's constant: one over four pi e_0

# the equation for electrical force is k * q^2 / dist^2 (assuming q is the charge on both tapes)
# so we have k * q^2 / dist^2 = g, which solves to q = dist * sqrt(g / k)
q = dist * math.sqrt(g / k)

print("Charge on each tape is", q)
