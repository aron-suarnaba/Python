from playwright.sync_api import sync_playwright

def login(page):
    page.goto("http://192.168.2.10/syteline/syteline/LogIn.php")
    page.get_by_label(" Your email or username ").fill("guest")
    page.locator("input[name='password']").fill("guest2017")
    page.get_by_role("button", name="Submit").click()

def auto_click(page):
    while True:
        page.reload()
        page.wait_for_selector("#btn_count")

        killer_btn = page.locator("#btn_count")

        try:
            value = int(killer_btn.inner_text().strip())
            print(f"Button value: {value}")

            if value > 55:
                killer_btn.click()
                print("✅ Clicked the button!")
        except Exception as e:
            print("⚠️ Could not read button value:", e)
        except KeyboardInterrupt as ki:
            print("Closing Syteline Auto Killer ... ")

        page.wait_for_timeout(2000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    
    login(page)
    auto_click(page)
