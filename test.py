import unittest
from pype.pype import *
from random import random

class PypeIn(AsyncPype):
    async def run(self, data):
        print("#In: " , id(self), data)
        return data

    def conduits(self):
        return (PypeOut, PypeEnd)


class PypeEnd(AsyncPype):
    async def run(self, data):
        print("#End")


class PypeOut(AsyncPype):
    async def run(self, data):
        await asyncio.sleep(random() * 3)
        data["data"] = data["data"][::-1]
        print("#Out: " , id(self), data)

        return data

    def conduits(self):
        return (PypeEnd,)


class PypeTestCase1(unittest.TestCase):
    def setUp(self):
        self.plumbing = Plumbing()


    def testPypeReturnAPipe(self):
        self.plumbing.flush(PypeIn, {"data": "test data"})


if __name__ == '__main__':
    unittest.main()