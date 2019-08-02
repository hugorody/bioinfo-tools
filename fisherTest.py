#!/usr/bin/python3

from scipy import stats

tratA = 17
remainingA = 94 - 17
tratB = 94
remainingB = 788
cutoff = 0.05

print ("Treatments",tratA,tratB)
print ("Remaining values",remainingA,remainingB)

treatment = [tratA,tratB]
remain = [remainingA,remainingB]

oddsratio, pvalue = stats.fisher_exact([treatment, remain])
print (pvalue)

################################################################################
proportion_a = tratA / remainingA
proportion_b = tratB / remainingB

if proportion_a > proportion_b:
    proptext = "Proportion of Treatment in A (" +str(proportion_a)+ ") is greater than in B ("+str(proportion_b)+")."
else:
    proptext = "Proportion of Treatment in A (" +str(proportion_a)+ ") is smaller than in B ("+str(proportion_b)+")."


if pvalue <= cutoff:
    print ("p-value significant. proportions are statistically different.\n" + proptext)
else:
    print ("p-value NOT significant. proportions are not statistically different.\n" + proptext)
