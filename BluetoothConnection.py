import asyncio
from bleak import BleakClient

address = "a0:6c:65:cf:7f:8f"
MODEL_NBR_UUID = "0000AAA0-0000-1000-8000-00805F9B34FB"

async def main(address):
    client = BleakClient(address)
    try:
        await client.connect()
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))
    except Exception as e:
        print(e)
    finally:
        await client.disconnect()

asyncio.run(main(address))