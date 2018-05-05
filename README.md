# as-set-to-prefixes
## About
Uses [RADb whois](http://www.radb.net/) and [RIPEstat RIS Prefixes](https://stat.ripe.net/docs/data_api#RISPrefixes) API to translate an `as-set` name to a list of ASNs, enumerate those AS's prefixes, and summarize those prefixes for brevity.

## Usage
Use [PeeringDB](https://www.peeringdb.com/) to discover valid as-set names.

`docker run nlopez/astp as-github`

Larger organizations will take more time to query. Be patient! >1 minute is not unusual.