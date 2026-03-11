# Lynx OSINT for Tor and Jackett


**Client:** Law Enforcement Agency

**Context:** We want to decrease dependence on commercial scrapers or opaque open-source tools.

BitTorrent seems to have become the number one P2P protocol with an increase in API connectivity. We consider it an untapped source of OSINT, that could complement the traditional
Wget and Google Search operators with filetype handles.

**Aim:**
Develop a safe text based probing variant of Lynx24. But first, perform a light source code review
to ensure nothing fishy is in place. Then, we need integration with Tor as well as Jackett with a
CLI interface inheriting the Google Search operators and a couple of custom handles merging up
to three typical operational OSINT scenarios. Social media is not in scope for this project.

**Technical:**
⎯ Keyword metadata search and AI enhanced DHT25 scanning to review duplicate findings.
⎯ Must be equal or more performant than Wget26 and initiated as a PowerShell27 module.
⎯ If it would simplify the project, keep Lynx for Tor searches and make a custom client for
qBittorrent28 and another one for Tixati29, preferably running headless with HTTPS access.
⎯ If relevant, add I2P30 to the scope of the project.
Functional:
⎯ Reverse image search across torrents file hashes without having to download actual files.
⎯ Mass file metadata probing, AI analysis and reporting.
⎯ Centralized keyword searching and highlighting in generated DOCX or PPTX reports.
⎯ Let us know whether eMule31, DC++32, Usenet33 or IRC34 would be relevant to include.

24 https://github.com/ThomasDickey/lynx-snapshots
25 https://www.bittorrent.org/beps/bep_0005.html
26 https://www.gnu.org/software/wget/
27 https://github.com/PowerShell
28 https://github.com/qbittorrent/qBittorrent
29 https://forum.tixati.com/offtopic/112
30 https://i2p.net/en/
31 https://www.emule-project.com/home/perl/general.cgi?l=29
32 https://hg.code.sf.net/p/dcplusplus/code
33 https://web.archive.org/web/20170717031029/http://www.usenet4you.net/
34 https://datatracker.ietf.org/doc/html/rfc1459
