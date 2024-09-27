# SPDX-FileCopyrightText: 2024 Christian Meeßen (GFZ) <christian.meessen@gfz-potsdam.de>
# SPDX-FileCopyrightText: 2024 Helmholtz Centre Potsdam - GFZ German Research Centre for Geosciences
#
# SPDX-License-Identifier: Apache-2.0

FROM python:3.12-slim

ARG DUID=1000
ARG DGID=1000

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv sync -d

CMD ["pipenv", "run", "fastapi", "run", "main.py", "--port", "8081"]
