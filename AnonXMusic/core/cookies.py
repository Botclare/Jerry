import aiohttp


from config import COOKIES

async def fetch_cookies():
    if not COOKIES:
        return None
    id = COOKIES.split("/")[-1]
    url = f"https://batbin.me/raw/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                raw_content = await response.text()
                with open("cookies/cookies.txt", "w") as file:
                    file.write(raw_content)
                
                print(f"Content successfully written")
            else:
                print(f"Failed to fetch the URL. Status code: {response.status}")
