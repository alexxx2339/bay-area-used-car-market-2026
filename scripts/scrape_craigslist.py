from playwright.sync_api import sync_playwright
from pathlib import Path

base = Path(__file__).resolve().parents[1]
data_dir = base / "data"
data_dir.mkdir(exist_ok=True)

offsets = list(range(0, 9600, 120))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    page = browser.new_page()

    for offset in offsets:
        url = f"https://sfbay.craigslist.org/search/cta?bundleDuplicates=1#search=2~list~{offset}"

        print(f"Scraping offset {offset}")

        page.goto(url, wait_until="commit", timeout=90000)
        page.wait_for_timeout(12000)

        text = page.locator("body").inner_text()

        file_path = data_dir / f"craigslist_page_{offset}.txt"
        file_path.write_text(text, encoding="utf-8")

        print(f"Saved {file_path}")

    input("Done. Press Enter to close...")