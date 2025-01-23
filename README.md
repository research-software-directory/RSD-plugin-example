# RSD-plugin-example

This repo contains examples of how to implement RSD plugins.

## Quick start

1. Copy `.env.example ` to `.env`
2. Build docker compose image

   ```bash
   # In RSD-as-a-service repository
   docker compose build
   ```

3. Start all services

```bash
docker compose up
```

At this point, if you open [http://localhost](http://localhost), the plugin-01 should be integrated into RSD. Login with the local account, eg. test user, and create an software entry. In the software edit section you should see "Plugin 01" menu option. In the user menu, additional options of Plugin 01 will appear twice.

**Note! The plugin 01 will appear twice in this example because we defined same plugin twice in the settings.json. We did this to demonstrate that you can refer to a plugin by plugin path (short name) or by url in the settings.json.**

## Integration points

Following definitions are required during the plugin integration:

- implement `{plugin}/api/v1/config` endpoint: see plugin-01/backend folder for basic example of implementation of the required config endpoint.
- docker-compose.yml: the plugin image(s) should be included in the docker-compose.yml (see how plugin-01 services are integrated in docker-compose.yml)
- nginx.config: the plugin services should be exposed in the nginx.config in order to be accessed from the core RSD frontend service
- settings.json: the plugin should be included in the plugins array, see rsd-settings/settings.json and [README.md](rsd-settings/README.md). Plugin listing will trigger the RSD frontend to send request to config endpoint of the plugin.

## Folder structure

Here we explain the folder structure of this repo.

- debug: debug service containing ubuntu and curl. It can be used to inspect docker network and validate config url that should be provided in the settings.json
- nginx: web server that connects all RSD services including plugins under one domain (localhost in this example)
- plugin-01: contains basic example of backend and frontend implementation of an plugin
- rsd-settings: contains customised settings.json that defines two plugins. Note that the second plugin is defined but it is not working properly

For more information see the README files in the folders. In addition, you can check [RSD documentation](https://research-software-directory.org/documentation/rsd-instance/)

## Official RSD SAAS images

In the example we use officially released RSD SAAS images that support the plugins. First version that supports plugins was v2.22.0. This repo is tested with v2.23.0.

## Using local RSD SAAS images

You can try using different official RSD SAAS images. However in some cases, during the development, it could be beneficial to use locally build images. In this case you can follow these steps:

- Clone core [RSD repo](https://github.com/research-software-directory/RSD-as-a-service)
- Copy `.env.example ` to `.env`
- Provide secrets at the bottom of the .env file
- Build core RSD images `docker compose build`
- Update the docker-compose file in this repo with the proper image and versions (you can copy this info from the docker compose file of core RSD repo).
