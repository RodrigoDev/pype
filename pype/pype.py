import asyncio

class Pype:
    pass


class AsyncPype(Pype):
    async def execute(self, data):
        if (self.conduits()):
            data = await self.run(data)
            for pype in self.conduits():
                await asyncio.ensure_future(pype().execute(data))
        else:
            await self.run(data)

    def conduits(self):
        return ()


class Plumbing:
    def flush(self, input_pipe: Pype, data: dict):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(input_pipe().execute(data)))
        while True:
            pending_tasks = [task for task in asyncio.all_tasks() if not task.done()]
            if pending_tasks:
                loop.run_until_complete(asyncio.gather(*pending_tasks))
            else:
                print("no pending tasks.")
                loop.run_until_complete(asyncio.gather(asyncio.sleep(1)))
        loop.close()
