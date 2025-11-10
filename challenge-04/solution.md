# My Solution

💡

The problem here is that the app implements authentication but no authorization. Consequently, any logged-in user can edit the profile of any other logged-in user, which is most likely unintended and a serious vulnerability.

To remediate this, implement a check ensuring users can only edit their own profile. This can be accomplished e.g. by taking the username from the session (not directly attacker-controlled) instead of the request (directly under the attacker's control).

(user_profile.get_username() problem of validation check same username of form same username get in database no authorisation)
(be2dar 8ayer profile leh hayalla user bade yeh bi request)
