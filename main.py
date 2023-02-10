import uvicorn
from fastapi import FastAPI, Response
from starlette.responses import RedirectResponse

from config import HOST, PORT, DEBUG
from link_shortner import get_link, get_link_v2

app = FastAPI()


@app.get('/')
async def get_root():
    return RedirectResponse('/docs')


@app.get('/link')
async def get_shortened_link(project_name: str, targets_base: str):
    link = get_link(utm_source=targets_base, utm_campaign=project_name)
    return Response(content=link)


@app.get('/link_v2')
async def get_shortened_link_v2(project_name: str, targets_base: str):
    link = get_link_v2(utm_source=targets_base, utm_campaign=project_name)
    return Response(content=link)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=DEBUG)
