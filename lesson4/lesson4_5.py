import asyncio
from playwright.async_api import async_playwright, Error

async def main():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context()  # 使用 context 更安全
            page = await context.new_page()
            
            await page.goto('https://example.com')

            await page.wait_for_selector('p')  # 等待 <p> 元素出現
            content = await page.inner_text('p')  # 取得該元素的文字內容
            
            print("取得的內容：", content)

            await browser.close()

    except Error as e:
        print("Playwright 發生錯誤：", e)

# 確保以主程式形式執行
if __name__ == "__main__":
    asyncio.run(main())
