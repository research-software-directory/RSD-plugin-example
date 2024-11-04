# RSD settings

This is customized settings.json file that implements plugin-01 into RSD.

## Plugins entry

The initial entry point for the plugin is defined in settings.json, section host. The plugin can be referenced by service name or by url.

**Note! When service name is defined the location to settings endpoint of the plugin is constructed using the following . When url is provided RSD will use the url to reach config endpoint.**

```json
{
  ...
  "plugins":["plugin-01","http://nginx/plugin/plugin-02"]
  ...
}
```

For more information examine setting.json in this folder.

For more information about the implementation in the RSD [see the source code](https://github.com/research-software-directory/RSD-as-a-service/blob/main/frontend/config/getPlugins.ts#L24).
