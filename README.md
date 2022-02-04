# check
Checklists on the go


## generating password hashes and secrets

Password hash generated using:
>>> from passlib.hash import pbkdf2_sha256
>>> pbkdf2_sha256.hash("password")


Secret generated with:
>>> import secrets
>>> secrets.token_hex())
