# SPDX-FileCopyrightText: 2024 Christian Meeßen (GFZ) <christian.meessen@gfz-potsdam.de>
# SPDX-FileCopyrightText: 2024 Helmholtz Centre Potsdam - GFZ German Research Centre for Geosciences
#
# SPDX-License-Identifier: Apache-2.0

import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from os import environ
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path=environ.get("API_ROOT_PATH", "/"))

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PluginSlot(BaseModel):
    slot: str
    icon: str
    href: str
    title: str
    subtitle: str

@app.get("/config")
async def config_endpoint(request: Request) -> list[PluginSlot]:
    # For informative purposes
    print(request)
    pluginSlots = [
        PluginSlot(
            slot="editSoftwareNav",
            icon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 12.75c1.63 0 3.07.39 4.24.9 1.08.48 1.76 1.56 1.76 2.73V18H6v-1.61c0-1.18.68-2.26 1.76-2.73 1.17-.52 2.61-.91 4.24-.91M4 13c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2m1.13 1.1c-.37-.06-.74-.1-1.13-.1-.99 0-1.93.21-2.78.58C.48 14.9 0 15.62 0 16.43V18h4.5v-1.61c0-.83.23-1.61.63-2.29M20 13c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2m4 3.43c0-.81-.48-1.53-1.22-1.85-.85-.37-1.79-.58-2.78-.58-.39 0-.76.04-1.13.1.4.68.63 1.46.63 2.29V18H24zM12 6c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3"></path></svg>',
            href="http://localhost/plugin/plugin-01/software.html",
            title="Plugin 01 link",
            subtitle="",
        ),
        PluginSlot(
            slot="userMenu",
            icon='<svg viewBox="0 0 24 24"><path d="M12 12.75c1.63 0 3.07.39 4.24.9 1.08.48 1.76 1.56 1.76 2.73V18H6v-1.61c0-1.18.68-2.26 1.76-2.73 1.17-.52 2.61-.91 4.24-.91M4 13c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2m1.13 1.1c-.37-.06-.74-.1-1.13-.1-.99 0-1.93.21-2.78.58C.48 14.9 0 15.62 0 16.43V18h4.5v-1.61c0-.83.23-1.61.63-2.29M20 13c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2m4 3.43c0-.81-.48-1.53-1.22-1.85-.85-.37-1.79-.58-2.78-.58-.39 0-.76.04-1.13.1.4.68.63 1.46.63 2.29V18H24zM12 6c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3"></path></svg>',
            href="http://localhost/plugin/plugin-01/",
            title="User Plugin 01",
            subtitle="",
        ),
    ]
    return pluginSlots


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
