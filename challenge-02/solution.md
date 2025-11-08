# My Solution

Note that multiple solutions exist, as the challenge was based solely on the provided code without additional context.

How I would approach it:

- Clarify if the developers want to redirect to external pages

- If so, they should strictly allow-list the external domains

- If they only want local redirects, they can do e.g.

* use a safer function that only does internal redirects, such as Flask's url_for (best solution IMO)

* parse the URL to redirect to using a URL library and then validate that the protocol is HTTPS and that the domain is the domain of their app

* mimic a function like IsUrlLocalToHost from ASP.NET which is designed for that purpose (the code is available here: https://github.com/aspnet/AspNetWebStack/blob/main/src/System.Web.WebPages/RequestExtensions.cs)

PS: Bonus points if you saw the Log Injection on line 20 which I accidentally put in there 😊. To fix Log Injections, please refer to this article (which I wrote when I was still an Application Security Consultant): https://community.veracode.com/s/article/How-to-Fix-CWE-117-Improper-Output-Neutralization-for-Logs

[These characters are typically represented as \r and \n respectively, or in hex 0x0D, 0x0A. ]

(mesckle ykoun haded wayn redirect yemken ykoun fi vulnerability redirect_url be3eta bi get)
