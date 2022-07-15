import asyncio
import aiohttp
import aiofiles


async def fetch_content(url: str) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            return content


async def save(filename: str, data: bytes) -> None:
    async with aiofiles.open(filename, 'wb') as file:
        await file.write(data)


async def download_pep(url: str, filename: str):
    content = await fetch_content(url)
    await save(filename, content)


async def main(pep_list: list):
    task_list = []
    for pep_num in pep_list:
        url = f"https://www.python.org/dev/peps/pep-{pep_num}/"
        task_list.append(download_pep(url=url, filename=f'pep-{pep_num}.html'))
    coros = await asyncio.gather(*task_list)
    return coros

if __name__ == '__main__':
    pep_list = []

    for i in range(8010, 8016):
        pep_list.append(i)

    asyncio.run(main(pep_list))
