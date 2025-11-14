# My Solution

Note that multiple solutions exist, as the challenge was based solely on the provided code without additional context.

## How I would approach it:

Clarify with the developers if the whole URL needs to be dynamic. If not: Hardcode as much of the URL as possible, and validate the remaining part appropriately (e.g., say the only attacker-controlled part is an ID, then you could validate it to be alphanumeric using a regex like `^[a-zA-Z0-9]{1,30}$`).

If it needs to be dynamic, ask the developers what pages they want the app to send requests to. Based on this, recommend the devs implement an allow-list for these domains.

(SSRF server side request forgery ex: we change url internal network of server, //192.168.// we can change all IP. CSRF client we obligate to change,CSRF btojbor client ya3mol action ma bado ya3mela, SSRF btojbor server ya3mol action ma bado ya3mela; server y3ayet leh specific url or IP in internal network ma bi choufa 8eir server bi redele response bi 2alb body fi men 1.2 lel 255 all IP)
