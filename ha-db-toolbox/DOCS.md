# HA DB Toolbox

A read-only look at what Home Assistant has stored about your devices, and a
check for device replacements. This version does not copy, change or delete
any data.

## Using the app

Start the app and open its web UI. There are no options to set. The UI is in
German and has three areas.

### Übersicht (overview)

Shows what the Toolbox can see:

- **Home Assistant:** the Core version and whether the Toolbox has been
  verified against exactly this version. On any other version the displays
  still work, but the results are not verified.
- **Geräte und Entities:** number of devices, entities, disabled entities and
  long-term statistics.
- **Recorder-Datenbank:** size, schema version and SQLite version of
  `home-assistant_v2.db`.
- **Installation:** a shortened fingerprint of this installation.

Only counts are shown, never states or history values.

### Gerätewechsel (device swap check)

For a device you have replaced:

1. Select the old device on the left and the new device on the right. The
   filter field narrows long device lists.
2. Choose **Übernahme prüfen**.

For every entity of the old device the result shows the proposed entity of
the new device, the number of stored history rows, and one of four results:

| Result | Meaning |
| --- | --- |
| übernehmbar | Type, device class, unit and state class match. |
| prüfen | A pair was found, but something differs or needs a human decision, for example a different unit or a meter reading. |
| nichts zu übernehmen | The old entity is disabled and has no stored history. |
| kein Gegenstück | The new device has no matching entity. |

Entities that exist only on the new device are listed separately. The check
is a proposal: equal device class and unit are hints, not proof.

### Diagnose (diagnostics)

Runs each check on its own and shows the raw answer, which you can copy into
a bug report. The answers contain no tokens, full identifiers or history
values.

## What the app does not do yet

- It does not copy history or statistics from the old to the new entity.
- It does not clean up or delete anything.
- It has no licensing and sends no telemetry.
- InfluxDB and other external databases are not supported yet.
- The history row count and the database overview need the default SQLite
  Recorder. With MariaDB or PostgreSQL these two displays are unavailable;
  the device swap check still works without row counts.

## Permissions

| Permission | Why |
| --- | --- |
| `homeassistant_api` | Read device registry, entity registry, states and statistic metadata through the documented Core API. Only an allow-list of read-only commands is used. |
| `addon_config` (read/write) | Stores the app's own installation identity in `/config/installation-id`. |
| `homeassistant_config` (read-only) | Read the Recorder SQLite file. The AppArmor profile limits access to `home-assistant_v2.db` and its `-wal`/`-shm` files; no other file of your Home Assistant configuration is readable. |

The app runs as an unprivileged user (UID/GID 10001) under an enforced custom
AppArmor profile, uses the default Supervisor role and exposes no host port.
The web UI and API accept traffic only from Home Assistant's ingress proxy
(`172.30.32.2`); the local `/api/health` endpoint remains available to the
container health check. The Recorder database is opened with `mode=ro` and
`query_only`.

## Installation identity

The app keeps its own identity in Home Assistant's official writable
`addon_config` mapping. Home Assistant stores this folder below
`/addon_configs/{REPO}_ha_db_toolbox` on the host and mounts it at `/config`
inside the container. The identity survives restarts, updates and a
backup/restore that includes the app configuration.

Do not edit or delete `/config/installation-id` unless you intentionally want
to reset the app identity.

## Troubleshooting

- **"Nicht erreichbar" / "Nicht verfügbar" in the overview:** Home Assistant
  did not answer. Wait until Home Assistant has finished starting, then choose
  **Neu laden**. If it persists, restart the app.
- **Recorder-Datenbank "Nicht sichtbar":** Home Assistant does not use the
  default SQLite Recorder, or the database file is missing.
- **Home Assistant version "noch nicht geprüft":** the Toolbox ships a fixed
  list of verified versions. An update of the app adds newer versions.
- **AppArmor:** from a Home Assistant terminal app, read the host audit
  journal with `ha host logs -t audit -n 1000` and look for entries
  containing `apparmor="DENIED"` and the `ha_db_toolbox` profile. Any denial
  is a compatibility or security event: capture the complete record and
  report it; do not broaden the profile.

When you report a problem, add the app version from the footer of the web UI,
your Home Assistant version and the relevant answer from **Diagnose**.
