import os
import pandas as pd

# Ajuste aqui para o nome EXATO do seu CSV
RAW_PATH = "academic Stress level - maintain....csv"

OUT_DIR = "data/processed"
OUT_PATH = os.path.join(OUT_DIR, "student_stress_clean.csv")


def standardize_columns(df):
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.replace(r"\s+", "_", regex=True)
    )
    return df


def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna(how="all")

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    numeric_cols = [
        "peer_pressure",
        "academic_pressure_from_your_home",
        "study_environment",
        "what_would_you_rate_the_academic_competition_in_your_student_life",
        "rate_your_academic_stress_index",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def create_features(df):
    components = [
        c for c in [
            "peer_pressure",
            "academic_pressure_from_your_home",
            "study_environment",
            "what_would_you_rate_the_academic_competition_in_your_student_life",
        ]
        if c in df.columns
    ]

    if components:
        df["overall_stress_score"] = df[components].sum(axis=1)

    return df


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    df = pd.read_csv(RAW_PATH)
    df = standardize_columns(df)
    df = clean_data(df)
    df = create_features(df)

    df.to_csv(OUT_PATH, index=False)

    print("ETL finished successfully")
    print("Rows:", len(df))
    print("Columns:", list(df.columns))


if __name__ == "__main__":
    main()

