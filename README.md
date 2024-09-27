# RSD-plugin-example

This repo contains an example of how to create RSD plugins.

## How to use

1) Copy `.env.example ` to `.env`
2) Check the network of the RSD and replace the network name in the plugin `docker-compose.yml`, if necessary.
3) Modify nginx configuration in RSD and add a new location:

   ```nginx
   	location /plugin/dummyplugin/api {
   		resolver 127.0.0.11 valid=30s ipv6=off;
   		set $pluginBackend dummy-plugin-backend;
   		proxy_pass http://$pluginBackend:8081;
   	}
   ```

4) Modify `settings.json` in RSD-as-a-service:

   ```json
   {
    "host": {
        "plugins": ["dummyplugin"]
    }
   }
   ```

5) Rebuild nginx and frontend and start the RSD

   ```bash
   # In RSD-as-a-service repository
   docker compose build nginx frontend
   docker compose up
   ```

6) Build and start the plugin backend
   
   ```bash
   # In the plugin repository
   docker compose build
   docker compose up
   ```
