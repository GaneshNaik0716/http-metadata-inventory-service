import httpx


async def fetch_metadata(url: str):

    async with httpx.AsyncClient(
        timeout=15,
        follow_redirects=True
    ) as client:

        response = await client.get(url)

        headers = dict(response.headers)

        cookies = dict(response.cookies)

        page_source = response.text

        return {
            "url": url,
            "headers": headers,
            "cookies": cookies,
            "page_source": page_source
        }