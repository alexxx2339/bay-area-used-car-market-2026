from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.cargurus.com/search?sourceContext=cargurus&sortType=BEST_MATCH&sortDirection=ASC&distance=50&newUsed=2&isDeliveryEnabled=false&hideWithoutPhotos=false&seoPageTypeId=10&srpVariation=DEFAULT_SEARCH"
    )

    page.wait_for_timeout(10000)

    print(page.title())

    input("Press Enter to close browser...")

    browser.close()