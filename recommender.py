import pandas as pd
from pathlib import Path


# ============================================================
# SIMPLE MUTUAL FUND RECOMMENDER
# ============================================================

PROJECT_DIR = Path(r"E:\internship\EBlueStock_MutualFund")

# Load fund data
fund_master = pd.read_csv(
    PROJECT_DIR / "data" / "processed" / "fund_master.csv"
)


def recommend_funds(risk_profile="Moderate", top_n=5):
    """
    Recommend mutual funds based on risk profile.

    Risk profiles:
    - Conservative
    - Moderate
    - Aggressive
    """

    data = fund_master.copy()

    # --------------------------------------------------------
    # Conservative investors
    # Prefer lower drawdown, lower beta and lower expense
    # --------------------------------------------------------
    if risk_profile.lower() == "conservative":

        data["recommendation_score"] = (
            data["expense_score"] * 0.25
            + data["drawdown_score"] * 0.35
            + data["sharpe_score"] * 0.25
            + data["alpha_score"] * 0.15
        )

    # --------------------------------------------------------
    # Moderate investors
    # Balanced performance and risk
    # --------------------------------------------------------
    elif risk_profile.lower() == "moderate":

        data["recommendation_score"] = (
            data["sharpe_score"] * 0.30
            + data["alpha_score"] * 0.25
            + data["drawdown_score"] * 0.20
            + data["expense_score"] * 0.15
            + data["cagr_score"] * 0.10
        )

    # --------------------------------------------------------
    # Aggressive investors
    # Prefer stronger return and performance metrics
    # --------------------------------------------------------
    elif risk_profile.lower() == "aggressive":

        data["recommendation_score"] = (
            data["cagr_score"] * 0.30
            + data["sharpe_score"] * 0.30
            + data["alpha_score"] * 0.25
            + data["drawdown_score"] * 0.10
            + data["expense_score"] * 0.05
        )

    else:
        raise ValueError(
            "Risk profile must be Conservative, Moderate, or Aggressive."
        )

    # Sort funds by recommendation score
    recommendations = (
        data.sort_values(
            "recommendation_score",
            ascending=False
        )
        .head(top_n)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "cagr_3y",
            "sharpe_ratio",
            "alpha",
            "max_drawdown",
            "expense_ratio_pct",
            "recommendation_score"
        ]
    ]


# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":

    print("\nConservative Investor Recommendations")
    print("--------------------------------------")
    print(
        recommend_funds(
            risk_profile="Conservative",
            top_n=5
        ).to_string(index=False)
    )

    print("\nModerate Investor Recommendations")
    print("----------------------------------")
    print(
        recommend_funds(
            risk_profile="Moderate",
            top_n=5
        ).to_string(index=False)
    )

    print("\nAggressive Investor Recommendations")
    print("-----------------------------------")
    print(
        recommend_funds(
            risk_profile="Aggressive",
            top_n=5
        ).to_string(index=False)
    )