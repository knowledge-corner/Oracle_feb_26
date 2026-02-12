import asyncio
import aiohttp
import pandas as pd
import tkinter as tk
from tkinter import messagebox

OUTPUT_FILE = "shipments.xlsx"


async def fetch_shipments(api_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            response.raise_for_status()
            data = await response.json()
            return data


async def save_to_excel(api_url):
    shipments = await fetch_shipments(api_url)
    df = pd.DataFrame(shipments)
    df.to_excel(OUTPUT_FILE, index=False)


def run_fetch():
    api_url = url_entry.get().strip()

    if not api_url:
        messagebox.showerror("Error", "Please enter an API URL")
        return

    try:
        asyncio.run(save_to_excel(api_url))
        messagebox.showinfo("Success", f"Saved to {OUTPUT_FILE}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Shipment Fetcher")
root.geometry("420x160")

label = tk.Label(root, text="Enter API URL:")
label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)
url_entry.insert(0, "Enter API URL here...")

fetch_button = tk.Button(root, text="Fetch & Save to Excel", command=run_fetch)
fetch_button.pack(pady=20)

root.mainloop()
