import asyncio
from pydoll.browser.chromium import Chrome
from time import sleep

async def bypass_cloudflare_example():
    async with Chrome() as browser:
        tab = await browser.start()

    # The context manager will wait for the captcha to be processed
    # before continuing execution
        async with tab.expect_and_bypass_cloudflare_captcha():
            await tab.go_to('https://servicos.pf.gov.br/epol-sinic-publico/')
        print("Waiting for captcha to be handled...")
        sleep(60)
    # This code runs only after the captcha is successfully bypassed
    print("Captcha bypassed! Continuing with automation...")
    # protected_content = await tab.find(id='protected-content')
    # content_text = await protected_content.text
    # print(f"Protected content: {content_text}")

asyncio.run(bypass_cloudflare_example())