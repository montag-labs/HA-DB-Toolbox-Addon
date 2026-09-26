# HA DB Toolbox

This private proof-of-concept wrapper runs the HA DB Toolbox core image as a Home Assistant app.

## Current scope

- Reads the Home Assistant configuration mount without write access.
- Queries the documented Supervisor `/info` endpoint when available.
- Exposes only shortened, domain-separated identity fingerprints.
- Performs no database cleanup, migration, licensing, or telemetry.

## Persistent app identity

The app uses Home Assistant's official writable `addon_config` mapping. Home Assistant stores this folder below `/addon_configs/{REPO}_ha_db_toolbox` on the host and mounts it at `/config` inside the app container.

The file `/config/installation-id` is managed by the app. Do not edit or delete it unless you intentionally want to reset the app identity. App version 0.0.6 migrates a valid legacy identity from `/data` when the config identity does not exist and never overwrites an existing config identity.

The Home Assistant configuration remains a separate read-only mount at `/homeassistant`.

The container image must be published by the private core repository before this app can be installed.
