# gharty03/Conti-Ransomware

- **Category:** [Ransomware & Threat Actor Tracking](../../../by-category/ransomware-threat-actor-tracking/README.md)
- **Type:** [research-project](../../../by-type/research-project/README.md)
- **Status:** `indexed`
- **URL:** <https://github.com/gharty03/Conti-Ransomware>
- **Sources:** `github-search:topic:malware-analysis`, `github-search:topic:ransomware`, `github-search:topic:threat-intelligence`
- **Reviewed:** 2026-11-23

Full source of the Conti Ransomware Including the missing Locker files from the original leak. I have fixed some of the errors intentionally introduced by the leaker to prevent the locker from being built. The Queue header file which implements a few linked list data structures that Conti uses for task scheduling in the Threadpool had several missing commas, there are still errors which I believe to be the result of a missing #ifdef pre-processsor macro in one of the header files but haven't had

[← Category index](../../../by-category/ransomware-threat-actor-tracking/README.md) · [← Master index](../../../README.md)
