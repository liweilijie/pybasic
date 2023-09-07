import asyncio
import time

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return "bobby"

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.baidu.com") for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-start_time)