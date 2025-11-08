# My Solution

- Recommend the developers switch to a more secure hashing algorithm, such as Bcrypt or PBKDF2 (note that SHA256 is NOT recommended for passwords!).

- Make sure to use an appropriate work factor. The idea is that you make password hashing intentionally slow so that bruteforcing becomes significantly harder (imagine it takes 0.01s to test one password whereas, if you make it intentionally slow, it takes 0.5s - that's 120 passwords per minute vs. 6000 passwords per minute).

And this is exactly the problem with e.g. SHA256 - it is fast, and we don't want this for passwords 😊.

A good rule of thumb is to use a work factor so that hashing the password takes like 0.5 seconds (slow enough to make bruteforcing hard, fast enough to not annoy legitimate users that want to log in).

Example Code (uses Bouncy Castle's BCrypt):

`BCrypt.generate(password, salt, 10)`

Here, `password` is the user's password, `10` is the work factor (performs 2^10 iterations) and `salt` is a cryptographically secure random number generated using Java's `SecureRandom`.

On top of this, you should also apply a pepper. A pepper is a secret value (as compared to a salt, which doesn't need to be secret) that is appended to the password before hashing. The idea is that if people provide bad passwords, the password is inherently more secure.

Simplified example:

- Someone uses as password "Winter2023"
- Our pepper is "asdklaje|132"
- Now, the password becomes "Winter2023asdklaje|132"

Thanks for coming to my TED talk on password hashing! 😊

(mechkle hon mesta5dmin MD5 lezem nesta3mel BCrypt with salt, bcrypt its latest)
