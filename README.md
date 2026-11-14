# HA DB Toolbox Add-on

Home Assistant app (add-on) for the HA DB Toolbox: a read-only look at what
Home Assistant has stored about your devices, and a check that tells you which
entities of a replaced device match the entities of its successor.

This version only reads. It does not copy, change or delete any data.

![HA DB Toolbox](ha-db-toolbox/logo.png)

## What you can do with it

- **Overview:** Home Assistant version and whether the Toolbox has been
  verified against it, number of devices, entities and long-term statistics,
  size and schema version of the Recorder SQLite database.
- **Device swap check:** pick the old and the new device. The Toolbox proposes
  entity pairs, shows how many history rows the old entity has, and flags
  pairs that need a closer look (different unit, meter readings, disabled
  entities, no counterpart).
- **Diagnostics:** the raw answer of every check, for bug reports.

Copying history from the old to the new entity is not part of this version.

## Installation

1. In Home Assistant open **Settings → Apps → App store**, open the menu in
   the top right corner and choose **Repositories**.
2. Add `https://github.com/montag-labs/HA-DB-Toolbox-Addon`.
3. Install **HA DB Toolbox** from the store and start it.
4. Open the web UI. Enable **Show in sidebar** if you want a permanent entry.

There is nothing to configure. Requirements, permissions and troubleshooting
are described in the [app documentation](ha-db-toolbox/DOCS.md).

## About this repository

The repository contains only the Home Assistant wrapper: permissions,
AppArmor profile and the reference to the versioned, signed core image
`ghcr.io/montag-labs/ha-db-toolbox`. The application itself lives in the
private [HA DB Toolbox core](https://github.com/montag-labs/HA-DB-Toolbox).
The add-on version always equals the core image version; CI verifies that the
referenced image exists and carries a valid signature.

Copyright (c) 2026 Montag Labs. All rights reserved.
