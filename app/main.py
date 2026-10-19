"""
Startup file
"""

import asyncio
from core.worker import Worker

async def app():
    """
    Began the process in async method
    """
    job = Worker()
    await job.run()
    
    

asyncio.run(app())