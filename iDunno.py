import sys

sides = len(sys.argv)


sideA = int(sys.argv[1])
sideB = int(sys.argv[2])
sideC = int(sys.argv[3])

sideAandB = sideA + sideB
sideAandC = sideA + sideC
sideBandC = sideB + sideC

print(f"sideA + sideB : {sideAandB}")
print(f"sideA + sideC : {sideAandC}")
print(f"sideB + sideC : {sideBandC}")
if ((sideBandC)> sideA and (sideAandC)> sideB and (sideAandB)> sideC):
    print ("This triangle would be possible to make.")
else:
    print ("This triangle would be impossible to make.")

