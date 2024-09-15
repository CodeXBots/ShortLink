from configs import *
from aiohttp import web
from shortzy import Shortzy
import asyncio, logging, aiohttp, traceback
from database import db

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("RahulReviewsYT")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def ping_server():
    while True:
        await asyncio.sleep(600)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(BASE_URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()


async def short_link(link, uid):
    usite = await db.get_value("shortner", uid=uid)
    uapi = await db.get_value("api", uid=uid) 
    shortzy = Shortzy(api_key=uapi, base_site=usite)
    return await shortzy.convert_from_text(link)

async def save_data(tst_url, tst_api, uid):
    shortzy = Shortzy(api_key=tst_api, base_site=tst_url)
    link=f"https://telegram.me/CodeXBro"
    short = await shortzy.convert(link)        
    if short.startswith("http"):
        await db.set_shortner(uid, shortner=tst_url, api=tst_api)
        return True
    else:
        return False
