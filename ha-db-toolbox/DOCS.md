# HA DB Toolbox

This private proof-of-concept wrapper runs the HA DB Toolbox core image as a Home Assistant app.

## Current scope

- Reads the Home Assistant configuration mount without write access.
- Queries the documented Supervisor `/info` endpoint when available.
- Exposes only shortened, domain-separated identity fingerprints.
- Performs no database cleanup, migration, licensing, or telemetry.

The container image must be published by the private core repository before this app can be installed.
