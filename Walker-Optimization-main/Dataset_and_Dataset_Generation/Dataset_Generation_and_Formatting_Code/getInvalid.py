# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:29:09 2022

@author: Lyle
Modified: Advaith
"""


def getInvalid(df):
    df=df.copy()
    
    if not df.columns[0].startswith(" "):
        df.columns = [" " + string for string in list(df.columns)]
        
    invalid_walkers=[]
    for idx in df.index:    
        invalid=False
        if df.at[idx, " H"]<=0:
            invalid=True
        if df.at[idx, " L1"]<=0:
            invalid=True
        if df.at[idx, " L2"]<=0:
            invalid=True
        if df.at[idx, " L3"]<=0:
            invalid=True
        if df.at[idx, " L4"]<=0:
            invalid=True
        if df.at[idx, " L5"]<=0:
            invalid=True
        if df.at[idx, " L7"]<=0:
            invalid=True
        if df.at[idx, " L8"]<=0:
            invalid=True
        if df.at[idx, " A2"]<=0:
            invalid=True
        if df.at[idx, " D"]<=0:
            invalid=True
        if df.at[idx, " T"]<=0:
            invalid=True
        if df.at[idx, " D2"]<=0:
            invalid=True
        if df.at[idx, " T2"]<=0:
            invalid=True
        if df.at[idx, " D3"]<=0:
            invalid=True
        if (df.at[idx, " L3"] + df.at[idx, " L4"]) >= df.at[idx, " H"]:
            invalid=True
        if (df.at[idx, " L2"]) >= (df.at[idx, " H"]-3):
            invalid=True
        if (df.at[idx, " L3"]) <= (df.at[idx, " D"] + (2*df.at[idx, " T"]) + 0.5):
            invalid=True
        if (df.at[idx, " D"] + (2*df.at[idx, " T"])) > 1:
            invalid=True
        if (df.at[idx, " D3"] >= (df.at[idx, " D"] + (2*df.at[idx, " T"]))):
            invalid=True
        # #H-L2 in 1 range of (L3 + L4)
        # if ((df.at[idx, " H"]-df.at[idx, " L2"])<(df.at[idx, " L3"]+df.at[idx, " L4"]+df.at[idx, " D3"]+0.1) and ((df.at[idx, " H"]-df.at[idx, " L2"])>(df.at[idx, " L3"]+df.at[idx, " L4"]-df.at[idx, " D3"]-0.1))):
        #     invalid=True
        # #H-L2 in 0.9 range of (L4)
        # if ((df.at[idx, " H"]-df.at[idx, " L2"])<(df.at[idx, " L4"]+0.4) and ((df.at[idx, " H"]-df.at[idx, " L2"])>(df.at[idx, " L4"]-0.4))):
        #     invalid=True



        #TEMPORARY: IF D2+T2 needs to be set to D and T DELETE
        if (df.at[idx, " D2"] + (2*df.at[idx, " T2"])) > (df.at[idx, " D"] + (2*df.at[idx, " T"])): 
            invalid=True

        if invalid==True:
            invalid_walkers.append(idx)


    perc=1-len(invalid_walkers)/float(len(df.index))
    return invalid_walkers, perc