# Security Policy

## Supported versions

open-detect is pre-1.0. Only the **latest released `0.y.z` version** (see the
[releases page](https://github.com/arman1371/open-detect/releases)) receives security fixes.
Fixes ship as a new patch release; older versions are not backported.

## Reporting a vulnerability

**Do not open a public issue, pull request or discussion for a security problem.**

Use GitHub's private vulnerability reporting instead:

1. Go to <https://github.com/arman1371/open-detect/security/advisories/new>
   (repository **Security** tab, **Report a vulnerability**).
2. Describe the issue, the affected version or commit, and steps to reproduce. A minimal
   proof of concept helps. Do not include real customer data.

## What to expect

- Acknowledgement within **5 business days**.
- An initial assessment (accepted, needs more information, or out of scope) within **10 business days**.
- For accepted reports, a fix and coordinated disclosure through a GitHub security advisory.
  We aim to release a fix within **90 days** of the report, sooner for high-severity issues,
  and will credit reporters who want credit.

## Scope

In scope: the `open-detect` Python package and the CI/CD configuration in this repository
(`.github/`). Out of scope: vulnerabilities in third-party dependencies that are not
exploitable through open-detect (report those upstream), and findings that need a
pre-compromised environment.
