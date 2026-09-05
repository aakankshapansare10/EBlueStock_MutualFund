import requests
import pandas as pd
from pathlib import Path

# Output folder
OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Five key schemes given in the task
schemes = {
    119551: "SBI Bluechip",
    120503: "ICICI Bluechip",
    118632: "Nippon Large Cap",
    119092: "Axis Bluechip",
    120841: "Kotak Bluechip"
}

# Fetch NAV data for each scheme
for scheme_code, scheme_name in schemes.items():

    print("\n" + "=" * 70)
    print(f"Fetching: {scheme_name}")
    print(f"Scheme Code: {scheme_code}")
    print("=" * 70)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        # Convert NAV records into DataFrame
        nav_df = pd.DataFrame(data["data"])

        # Add scheme information
        nav_df["scheme_code"] = scheme_code
        nav_df["scheme_name"] = scheme_name

        # Create filename
        filename = scheme_name.lower().replace(" ", "_") + "_nav.csv"

        output_file = OUTPUT_DIR / filename

        # Save CSV
        nav_df.to_csv(output_file, index=False)

        print("Records:", len(nav_df))
        print("Saved to:", output_file)

    else:
        print("API request failed.")
        print(response.text)