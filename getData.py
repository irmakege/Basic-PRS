import pandas as pd

def getMetadata(data):
    metadata = pd.read_csv("data/prs_metadata.csv")
    variants = metadata.variant.values.tolist()
    return print(metadata, variants)


if __name__ == "__main__":
    metaDataName = "prs_metadata.csv"
    getMetadata(metaDataName)