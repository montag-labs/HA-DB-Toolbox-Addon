# Changelog

## 0.0.16

- Permit `dac_override` only during the root bootstrap so the protected
  container can initialize its own Supervisor-provided writable mappings.
  The service then immediately drops to UID/GID 10001; no Home Assistant
  configuration folder is mounted.

## 0.0.15

- Remove the unnecessary `homeassistant_config` mount. The internal Core UUID
  is not a supported app contract; registry and Recorder reads already use
  documented APIs.
- Reserve `/config` exclusively for the official writable `addon_config`
  mapping, eliminating the restore-time mount collision with `/homeassistant`.

## 0.0.14

- Keep an existing restored `installation-id` untouched during startup. The
  app still prepares its own config directory for new identities, but no
  longer requires ownership-changing access to a backup-restored identity.

## 0.0.13

- Explicitly map the official read-only `homeassistant_config` folder to
  `/homeassistant` and the app's writable `addon_config` folder to `/config`.
- Fix startup after backup/restore by preparing the target config directory
  before migrating a legacy identity and only correcting ownership of the
  app-owned identity file.

## 0.0.12

- Add a strictly bounded read-only Recorder probe using Home Assistant's History REST and Recorder WebSocket APIs.
- Limit the probe to five entities, five statistic IDs, one hour, and fixed response-size/time limits.
- Return aggregate counts and advertised Recorder capabilities only; raw IDs, states, attributes, and values stay internal.
- Keep all write-capable Recorder commands blocked by the Core allowlist.

## 0.0.11

- Enforce the custom AppArmor profile after the complete DEV-HA audit produced no new policy exceptions.
- Retain only the narrowly scoped runtime, ingress, Supervisor/Core proxy, and mapped-storage permissions validated in 0.0.10.

## 0.0.10

- Add the four read-only paths observed during the v0.0.9 AppArmor audit.
- Keep AppArmor in complain mode for one final DEV-HA verification before enforcement.

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
