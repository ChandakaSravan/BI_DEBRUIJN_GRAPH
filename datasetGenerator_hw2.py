########################### CSE 5370: Bioinformatics ###########################
################################# Assignment 2 #################################

# ->->->->->->->->->->->->->->->-> IMPORTANT <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-
# ANY CHANGES MADE TO THIS FILE WILL IMMEDIATELY RESULT INTO GETTING A ZERO
# GRADE FOR THE ASSIGNMENT. THE GRADING SCRIPT WILL GENERATE THE DATASET
# FROM YOUR UTA ID USING THIS SCRIPT, PLOT THE CORRECT DE BRUIJN GRAPH, THEN 
# THE TA FOR THE COURSE WILL COMPARE YOUR SUBMITTED VERSION WITH THE 
# VERSION GENERATED BY THE GRADING SCRIPT.

# This program will take your 10 digits UTA student ID as an input, and 
# generates a simple set of simulated genome sequencing reads unique to your
# 10 digit ID. To run the program, simply execute:
# >> python3 datasetGenerator_hw2.py --ID [your student ID]
# Execution of this code will generate a file [UTAID].txt as well as a 
# printout of the generated list to the console.

import os
import argparse

import numpy as np
import pandas as pd

READS = ["gac", "acg", "cga", "cgc", "cgt", "gcg", "tcg", "gag", "aga"]
P = 0.90
Q = 0.85

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='reads dataset generator.')
    parser.add_argument('--ID', type=int, required=True, help='your 10 digits student ID, e.g. 1001234567')
    args = parser.parse_args()
    ID = args.ID
    
    np.random.seed(ID)
    probs =[P, P, P, P, Q, P, Q, P, P]
    
    out = []
    for i in range(len(READS)):
        if np.random.random() < probs[i]:
           out.append(READS[i])
        
    with open(str(ID) + ".txt", "w") as f:
        for elem in out:
            f.write(str(elem)+'\n')
    f.close()
    