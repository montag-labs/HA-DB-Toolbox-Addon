# Changelog

## 0.0.9

- Restrict app HTTP access to the official Home Assistant ingress proxy; only the local container health check bypasses this restriction.
- Add a custom AppArmor profile in audit-only complain mode for validation on DEV-HA before enforcement.
- Remove legacy image mode and publish architecture-specific, signed images with the official Home Assistant builder actions.

## 0.0.8

- Enable the minimal `homeassistant_api` permission required by the official Core WebSocket proxy.

## 0.0.7

- Add a strictly read-only Home Assistant registry and Recorder statistics inventory.
- Return aggregate counts only; registry identifiers, database rows, and tokens stay internal.
- Support Home Assistant child devices and the current Recorder `mean_type` metadata.

## 0.0.6

- Store the app-owned installation identity in Home Assistant's official writable `addon_config` mapping.
- Migrate a valid legacy identity from `/data` without overwriting an existing config identity.
- Keep the Home Assistant configuration mount read-only.

## 0.0.5

- Validation release for identity persistence across an app update.
