# Changelog

## 0.0.20

- DEV-HA test branch only (not for main): Core 0.0.20 pairs numbered entities
  (for example `eingang_0` / `eingang_1`) reliably and reports disabled
  entities without stored history as "nothing to transfer".

## 0.0.19

- DEV-HA test branch only (not for main): Core 0.0.19 adds a read-only check
  that compares the entities of an old and a new device and counts stored
  history rows (start page, "Uebernahme pruefen"). Nothing is copied or
  changed. Keeps the read-only `homeassistant_config` mapping from the test
  build 0.0.18.

## 0.0.18

- Rename the internal Core package to `ha_db_toolbox` and the runtime
  environment variables to `HA_DB_TOOLBOX_*`. The Add-on now sets
  `HA_DB_TOOLBOX_DATA_PATH` and `HA_DB_TOOLBOX_INGRESS_ONLY`.
- Installation identity, fingerprints and the `/config` data location are
  unchanged; no re-binding or data migration is needed.
- Requires Core image `0.0.18`; older images ignore the new variable names.
- DEV-HA test branch only (not for main): add a read-only `homeassistant_config` mapping and a
  matching AppArmor rule limited to `home-assistant_v2.db` and its WAL/SHM
  files. The Core image 0.0.18 exposes `/api/poc/sqlite`, which returns only
  aggregate metadata. Nothing is written; direct SQL writes stay blocked.

## 0.0.17

- Add a read-only compatibility preflight. It reads the documented Home
  Assistant Core version through the existing Core API proxy and compares it
  with the locally shipped, fail-closed compatibility matrix.
- Return only version, compatibility status, stable blocker codes and a
  shortened report digest. No database operation or write endpoint exists.
- Align the Core package, Health API and Add-on release version on `0.0.17`.

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
