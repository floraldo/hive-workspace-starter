# Packages

A package contains reusable implementation logic with a stable contract. This folder is
intentionally empty at first.

Promote logic here when it serves at least two workflows or needs tests, schemas,
versioning, or reliable error handling. Likely candidates might later include document
intake, content transformation, reporting, or deterministic Drive synchronization.

Do not create a package merely because a SaaS connector exists. Each package should have
a README, public contract, tests, and named owner.
