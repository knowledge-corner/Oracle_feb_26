import asyncio
import aiohttp
import pandas as pd

API_URL = "https://shipment-tracker-ehfh.onrender.com/api/shipments"
OUTPUT_FILE = "shipments.xlsx"


async def fetch_shipments():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            response.raise_for_status()
            data = await response.json()
            return data


async def save_to_excel():
    print("Fetching shipment data...")
    shipments = await fetch_shipments()

    print("Converting to DataFrame...")
    df = pd.DataFrame(shipments)

    print("Saving to Excel...")
    df.to_excel(OUTPUT_FILE, index=False)

    print(f"Done! File saved as {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(save_to_excel())


# Dummy example on multiple API requests - 

"""
import asyncio
import aiohttp

BASE_URL = "https://shipment-tracker-ehfh.onrender.com/api/shipments"


async def fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def fetch_all():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, BASE_URL),
            fetch(session, BASE_URL),
            fetch(session, BASE_URL)
        ]

        results = await asyncio.gather(*tasks)
        return results


async def main():
    data = await fetch_all()


if __name__ == "__main__":
    asyncio.run(main())

"""