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

## Security validation

The app accepts UI and API traffic only from Home Assistant's ingress proxy (`172.30.32.2`). The local `/api/health` endpoint remains available to the container health check. Forwarding headers are not trusted for this decision.

Version 0.0.11 enforces the custom AppArmor profile. Its minimal permissions were validated on DEV-HA in complain mode with app startup, shutdown, restart, identity, inventory, ingress, and health-check traffic. From a Home Assistant terminal app, retrieve the host audit journal through the Supervisor CLI with:

```shell
ha host logs -t audit -n 1000
```

Look for entries containing `apparmor="DENIED"` and the `ha_db_toolbox` profile. The `journalctl _TRANSPORT="audit" -g 'apparmor="DENIED"'` variant is only available from a direct Home Assistant OS host shell, not from a terminal app or the `ha >` CLI prompt.

Any denial is a compatibility or security event: stop the affected operation, capture the complete audit record, and do not broaden the profile without understanding and testing the exact access requirement.

The Home Assistant configuration remains a separate read-only mount at `/homeassistant`.

The container image must be published by the private core repository before this app can be installed.
