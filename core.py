import asyncio
from random import random

class Pype:
    async def execute(self, data):
        #import ipdb; ipdb.set_trace()
        if (self.conduits()):
            data = await self.run(data)
            asyncio.ensure_future(*(pype().execute(data) for pype in self.conduits()))
        else:
            await self.run(data)

    def conduits(self):
        return ()

class PypeIn(Pype):
    async def run(self, data):
        print("#In: " , id(self), data)

    def conduits(self):
        return (PypeOut,)

class PypeOut(Pype):
    async def run(self, data):
        await asyncio.sleep(random() * 3)
        print("#Out: " , id(self), data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*(PypeIn().execute({"data": "data"}) for _ in range(1, 10))))
    pending_tasks = [
        task for task in asyncio.Task.all_tasks() if not task.done()]
    loop.run_until_complete(asyncio.gather(*pending_tasks))
    loop.close()