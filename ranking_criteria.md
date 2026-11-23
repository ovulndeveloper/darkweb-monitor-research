# Ranking Criteria

Every tool is scored from 1 to 5 on five equally weighted criteria. Each score must be supported by a primary source or an explicitly labeled cross-check in [`rsearch/SOURCES.md`](rsearch/SOURCES.md).

## Criteria

1. **Feature completeness** — capabilities, automation, integrations, and documentation of actually shipped features.
2. **Platform compatibility** — quality of Windows, Linux, web, API, or container support.
3. **Community adoption** — GitHub stars/forks, reported users, or documented deployments.
4. **Update frequency** — recent commits/releases and evidence of active maintenance.
5. **Documentation quality** — clarity of official docs, API references, tutorials, and safety guidance.

## Scale

| Score | Meaning |
|---|---|
| 5 | Excellent across all criteria; primary-source verified and actively maintained |
| 4 | Strong in most criteria; minor limitations or incomplete evidence |
| 3 | Useful niche tool; narrower scope or unstable addresses |
| 2 | Orientation/directory value rather than a full tool |
| 1 | Experimental or very specialized |

## Rules

- Rankings are editorial and evidence-linked, not vendor scores.
- A tool with no primary source cannot score above 3.
- An archived repository or dead primary URL must be downgraded or marked `inactive`.
- `.onion` address availability does not by itself prove tool quality.
- Conflicts with legacy rankings are recorded in [`rsearch/RECONCILIATION.md`](rsearch/RECONCILIATION.md).

*Last verified: 2026-11-23 (UTC)*
