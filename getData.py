import pandas as pd

def getMetadata(data):
    metadata = pd.read_csv("data/prs_metadata_trial.csv")
    variants = metadata.variant.values.tolist()
    return metadata, variants

def getPopdata(data):
    return

def checkGenotype(fileName, metadata):
    variant = pd.read_csv(f"data/variants1000genome/{fileName}_EUR.csv")
    row = metadata.loc[metadata['variant'] == fileName]
    
    rA1 = row['riskAllele1'].values[0] + row['riskAllele1'].values[0]
    rA2 = row['riskAllele2'].values[0] + row['riskAllele2'].values[0]
    rA3 = row['riskAllele1'].values[0] + row['riskAllele2'].values[0]
    rA4 = row['riskAllele2'].values[0] + row['riskAllele1'].values[0]

    print(rA1, rA2, rA3, rA4)

    return 


if __name__ == "__main__":
    metaDataName = "prs_metadata.csv"
    metadata, variantList = getMetadata(metaDataName)
    for v in variantList:
        checkGenotype(v, metadata)