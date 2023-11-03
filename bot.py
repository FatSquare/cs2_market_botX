### TODO: trying to get weapon float with a simple GET request but BOT detection (even with http headers) ===> get(f"https://api.csfloat.com/?url={inspect_link}" ).json()


### BOT CONFIG (explained in documentation)
skins_start,skins_count = 0,100 
skin_name = "M4A1-S | VariCamo"
rarity = "Field-Tested"
statrak = False
max_float = 1



from bot_config import *
import asyncio,time
from playwright.async_api import async_playwright, Playwright

def print_red(text): print("\033[91m{}\033[0m".format(text))
def print_green(text): print("\033[92m{}\033[0m".format(text))
def print_blue(text):print("\033[94m{}\033[0m".format(text))
def get_d_number(ch,id):
    ch = str(ch)
    i = 0 
    while i < 4:
        ch = ch[ch.find(id)+1:]
        i+=1
    return ch[52:170].replace('\\','')

async def run(playwright: Playwright):
    skin_full_name = f"StatTrak™ {skin_name} ({rarity})" if statrak else f"{skin_name} ({rarity})"
    skin_page = f"https://steamcommunity.com/market/listings/730/{skin_full_name}?query=&start={skins_start}&count={skins_count}"

    print("loading browser")
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch()
    context = await browser.new_context()

    if steam_login_secure == "":
        print_red("No steam_login_secure found in bot_config.py.\nMarket's currency will be random");time.sleep(3)
    else:
        print_blue("Setting up cookies")
        await context.add_cookies([login_hash])

    page = await context.new_page()
    page2 = await browser.new_page()

    #  visiting steam page
    print("visiting steam page")
    await page.goto(skin_page)
    print("visiting csfloat")
    await page2.goto("https://csfloat.com/checker")

    weapon_index = skins_start + 1
    print_blue(f"Skin: {skin_full_name}")
    skins = await page.query_selector_all('.market_recent_listing_row')

    if len(skins) == 0:
        await page.screenshot(path="error.png")
        print_red("Error: 0 skins loadded!\nScreenshot saved at error.png")
        exit()

    print_green(f"{len(skins)} Skins were loadded!")

    # Saving page HTML for method 2 (which is about getting inspect link from the javascript code)
    page_content = await (await page.query_selector('body')).text_content()

    for skin in skins:

        price_el = await skin.query_selector('div.market_listing_price_listings_block > div.market_listing_right_cell.market_listing_their_price > span > span.market_listing_price.market_listing_price_with_fee')
        price = (await price_el.text_content()).strip()

        
        ### method 1 : ~3% slower + page interacting with buttons
        # btn = await skin.query_selector('.market_listing_item_img_container a')
        # await btn.evaluate_handle('button => button.click()', arg=btn)
        # inspect_link = await page.locator('#market_action_popup_itemactions > a').get_attribute('href')
        
        ### method 2 : little bit faster and doens't require page interaction but hardcodded
        listing_id = (await skin.get_attribute('id')).replace('listning_','')[-19:]
        item_id = (await (await skin.query_selector('.market_listing_price_listings_block > div > div > a')).get_attribute('href'))[-13:-2]
        inspect_link = get_d_number(page_content.encode('utf-8'),item_id).replace('%listingid%',listing_id).replace('%assetid%',item_id)

        # Getting weapon float from csfloat
        inpt = page2.locator('#mat-input-1')
        await inpt.fill(inspect_link)
        await page2.screenshot(path="error2.png")
        await page2.wait_for_selector('body > app-root > div > div:nth-child(2) > app-checker-home > div > div > app-checker-item > mat-card > item-float-bar > div > div:nth-child(1) > span > span');
        wp_float = float(await page2.locator('body > app-root > div > div:nth-child(2) > app-checker-home > div > div > app-checker-item > mat-card > item-float-bar > div > div:nth-child(1) > span > span').text_content())
        if wp_float < max_float:
            print(f"({weapon_index}) >>> FLOAT: {wp_float} | {price}")
        weapon_index+=1
        
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
