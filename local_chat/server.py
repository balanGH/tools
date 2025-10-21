import asyncio
import websockets
import json

clients = {}

async def handler(websocket):
    username = await websocket.recv()
    clients[username] = websocket
    print(f"[+] {username} connected")

    try:
        async for data in websocket:
            try:
                obj = json.loads(data)
            except json.JSONDecodeError:
                print(f"[!] Invalid message from {username}: {data}")
                continue

            # Message sending
            if obj["type"] == "message":
                target = obj["to"]
                if target in clients:
                    await clients[target].send(json.dumps({
                        "type": "message",
                        "from": username,
                        "msg": obj["msg"],
                        "id": obj["id"]
                    }))
                else:
                    await websocket.send(json.dumps({
                        "type": "system",
                        "msg": f"❌ User {target} not found"
                    }))

            # Seen status
            elif obj["type"] == "seen":
                sender = obj["to"]
                if sender in clients:
                    await clients[sender].send(json.dumps({
                        "type": "seen",
                        "id": obj["id"]
                    }))

    finally:
        if username in clients:
            del clients[username]
        print(f"[-] {username} disconnected")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8080):
        print("[SERVER] Running on port 8080...")
        await asyncio.Future()

asyncio.run(main())
