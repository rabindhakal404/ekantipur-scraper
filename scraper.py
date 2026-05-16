from playwright.sync_api import sync_playwright
import json

def click_skip(page):
    """Clicks skip button only if it appears"""
    try:
        page.wait_for_timeout(2000)
        skip = page.get_by_role("button", name="Skip")
        if skip.is_visible():
            skip.click()
    except:
        pass  # skip silently if not found

def get_image(img):
    if not img:
        return None

    for url in (
        img.get_attribute("data-src"),
        img.get_attribute("data-original"),
        img.get_attribute("src"),
        img.get_attribute("data-lazy"),
    ):
        if not url or url.startswith("data:"):
            continue
        if "kantipur-logo" in url or url.rstrip("/").endswith("logo.svg"):
            continue
        return url
    return None

def _norm_text(el):
    if not el:
        return None
    t = el.inner_text()
    if not t:
        return None
    t = t.strip()
    return t or None


def extract_entertainment(page):
        # Clicking the entertainment link in navbar
        page.locator(".bottom-nav").get_by_text("मनोरञ्जन").click()

        # Waiting for the page to load
        page.wait_for_load_state("networkidle")

        # Selecting the news cards
        cards = page.query_selector_all(
            ".category-main-wrapper .category-inner-wrapper"
        )

        result = []
        for card in cards:
            title_el = card.query_selector(".category-description h2 a")
            if not title_el:
                title_el = card.query_selector(".category-description h2")
            title = _norm_text(title_el)
            if not title:
                continue

            image_el = card.query_selector(".category-image img")
            image_url = get_image(image_el)

            author_el = card.query_selector(".author-name a")
            author = _norm_text(author_el)

            result.append({
                "title": title,
                "image_url": image_url,
                "category": "मनोरञ्जन",
                "author": author,
            })
            if len(result) >= 5:
                break

        return result

def extract_cartoon(page):
        # Direct url to cartoon if available as "व्यंग्यचित्र" doesnot exist
        page.goto("https://ekantipur.com/cartoon", wait_until="networkidle")

        cartoon = page.query_selector(".cartoon-wrapper, .cartoon-image")
        if not cartoon:
            return None

        title_c = cartoon.query_selector("h1, h2, h3")
        title_cartoon = title_c.text_content() if title_c else None

        image_c = cartoon.query_selector("img")
        image_url_cartoon = get_image(image_c)

        author_c = cartoon.query_selector("p")

        author_cartoon = None

        if author_c:
            text = author_c.text_content().strip()

            if "-" in text:
                author_part = text.split("-")[-1].strip()

                # only accept if not empty
                if author_part:
                    author_cartoon = author_part

        return{
            "title": title_cartoon,
            "image_url_cartoon": image_url_cartoon,
            "author": author_cartoon
        }

def main():     
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.ekantipur.com/", wait_until = "domcontentloaded")

        click_skip(page)
        
        page.wait_for_timeout(2000)

        entertainment = extract_entertainment(page)

        cartoon = extract_cartoon(page)

        browser.close()

        output = {
            "entertainment_news": entertainment,
            "cartoon_of_the_day": cartoon
        }

        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=4)

        print(json.dumps(output, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
