import pandas as pd
import os

def getMetadata(data):
    metadata = pd.read_csv("data/prs_metadata_trial.csv")
    variants = metadata.variant.values.tolist()
    return metadata, variants

def getPopdata(data):
    return

def checkGenotype(fileName, metadata):
    variant = pd.read_csv(f"data/variants1000genome/{fileName}_EUR.csv")['Genotype (forward strand)'].to_frame()
    row = metadata.loc[metadata['variant'] == fileName]

    rA1  = row['riskAllele1'].values[0]
    rA2 = row['riskAllele2'].values[0]    
    rG1 = row['riskAllele1'].values[0] + row['riskAllele1'].values[0]
    rG2 = row['riskAllele2'].values[0] + row['riskAllele2'].values[0]
    rG3 = row['riskAllele1'].values[0] + row['riskAllele2'].values[0]
    rG4 = row['riskAllele2'].values[0] + row['riskAllele1'].values[0]
    
    variantScore = []
    for index, sample in variant.iterrows():
        if rG1 in sample.values[0] or rG2 in sample.values[0]:
            score = row['effectSize'].values[0] * 2
            variantScore.append(score)
        elif rG3 in sample.values[0] or rG4 in sample.values[0]:
            score = row['effectSize'].values[0]
            variantScore.append(score)
        else: 
            score = 0
            variantScore.append(score)

        
        """ if rA1 not in sample.values[0] or rA2 not in sample.values[0]: 
            print(f'No match in {fileName}') """
        variantScoreCol = pd.DataFrame()
    variantScoreCol[fileName + " Score"] = variantScore
    
    
    

    return variantScoreCol


    


if __name__ == "__main__":
    metaDataName = "prs_metadata.csv"
    metadata, variantList = getMetadata(metaDataName)

    if os.path.isfile('data/prs_trial.xlsx'):
        os.remove('data/prs_trial.xlsx')
    polyScore = pd.DataFrame()
    
    for v in variantList:
        col1 = checkGenotype(v, metadata)
        polyScore[v] = col1
    
    polyScore['total'] = polyScore.sum(axis=1)
    polyScore.to_excel("data/prs_trial.xlsx", index=False)