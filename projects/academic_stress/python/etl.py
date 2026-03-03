import pandas as pd
from pathlib import Path

# Base folder: projects/academic_stress
BASE = Path(__file__).resolve().parents[1]

RAW = BASE / "data" / "raw" / "academic_stress.csv"
OUT = BASE / "data" / "processed" / "academic_stress_clean.csv"

def main() -> None:
    # EXTRACT
    df = pd.read_csv(RAW)

    # TRANSFORM
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("?", "", regex=False)
    )

    if "timestamp" in df.columns:
        df = df.drop(columns=["timestamp"])

    # LOAD
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    print(f"Saved to: {OUT}")
    print("ETL completed successfully.")

if __name__ == "__main__":
    main()