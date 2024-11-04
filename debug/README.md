# Debug service

This service use ubuntu image with curl installed. It can be used to make http requests using curl within docker network.
See docker-compose.yml file where this debug service is used.

## Open debug service

```bash
docker compose exec debug bash
```

## Make request

```bash
# try plugin 01 config api endpoint within the docker network (internal docker network traffic)
# NOTE! the request to config api endpoint is performed using the internal docker network (REQUIRED)
curl http://plugin-01-be:8081/config
```
