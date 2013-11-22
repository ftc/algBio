# 
from math import log
def Bayesian_score(rpt_fileName,alpha_fileName,matrix_fileName):
    N=20 # number of amino acids
    rpt_file=open(rpt_fileName,'r');
    alpha_file=open(alpha_fileName,'r');
    matrix_fileName=open(matrix_fileName,'r')
    
    RPT_seq=rpt_file.read().strip();
    alpha_seq=alpha_file.read().strip();
    
    scoring_matrix=[] #read from a file
    
    aa_list=['a','b','c','d'] # to get the indices
    alpha_len=len(alpha_seq)
    
    score=0 # the final score for this RPT and alpha binding probability 
    
    for rpt in range(1,8):
        for alpha in range(1,alpha_len):
            row= aa_list.index(RPT_seq[rpt])
            column=aa_list.index(alpha_seq[alpha])
            
            joint_counts=scoring_matrix[row,column];
            likelihood=joint_counts/N
            prior=1/N #===== might be changed
            posterior=likelihood*prior
            score+=log(posterior,10)
            
    print("RPT: "+rpt_fileName+" alpha: "+alpha_fileName+" score: "+str(score))
            
            
            
            
    
    
    
