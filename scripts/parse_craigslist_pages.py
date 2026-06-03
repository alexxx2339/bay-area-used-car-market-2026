from pathlib import Path
import re
import pandas as pd

base = Path(__file__).resolve().parents[1]
data_dir = base / "data"

rows = []

for file in data_dir.glob("craigslist_page_*.txt"):
    lines = [x.strip() for x in file.read_text(encoding="utf-8", errors="ignore").splitlines() if x.strip()]

    for i in range(len(lines) - 1):
        title = lines[i]
        detail = lines[i + 1]

        if ("$" in detail or "Call for Price" in detail) and "mi" in detail:
            price_match = re.search(r"\$([\d,]+)", detail)
            mileage_match = re.search(r"([\d,]+k?|[\d,]+)\s?mi", detail, re.I)
            year_match = re.search(r"\b(19\d{2}|20\d{2})\b", title)

            rows.append({
                "source_file": file.name,
                "title": title,
                "detail": detail,
                "year": year_match.group(1) if year_match else None,
                "mileage": mileage_match.group(0) if mileage_match else None,
                "price": price_match.group(1).replace(",", "") if price_match else None
            })

df = pd.DataFrame(rows).drop_duplicates()

out = data_dir / "craigslist_cars_sample.csv"
df.to_csv(out, index=False)

print(f"Saved {len(df)} rows to {out}")