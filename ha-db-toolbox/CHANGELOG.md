# Changelog

## 0.0.6

- Store the app-owned installation identity in Home Assistant's official writable `addon_config` mapping.
- Migrate a valid legacy identity from `/data` without overwriting an existing config identity.
- Keep the Home Assistant configuration mount read-only.

## 0.0.5

- Validation release for identity persistence across an app update.
