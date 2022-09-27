Private-public repo merge pending

# MeepSuite
meep-made malware, tools, etc. 
This houses the meeptools designated for use in RvB competitions and are not developed to the higher standard for real-life use as tools the private repo. 
OSINT tools pending legal questions before development. 

### Latest Updates:
- C2 (detects different kinds of meepware & creates unique loot folders)
- Keyloggers (basic & plus, advanced in development)
### Categories
- Implants
- Droppers
- Keyloggers
- C2

## Implants
- meepshell
  - executes received commands & sends output to c2

## Keyloggers
- meeplogger
  - stores keys to a local log file
  - log cannot be viewed in file explorer
- meeploggerplus
  - sends keys to c2 (previously meeploggerlistener)
- meeploggeradvanced (in development, no public version)
  - will send keys to private server with HTTPS
- meeploggerlistener (deprecated)
  - listens for meeploggers and uses multi-threading to simultaneously write to multiple files

## C2
- meepc2
  - Handles connections from all kinds of meepsuite tools 
  - Session switching and handling for shells
  - Unique loot folders
