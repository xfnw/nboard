# nboard

python curses based yourwalloftext clone

## help
read the --help text lol


## managing remotes
to get more remotes, you can

```bash
for i in $(cat remotes.txt); do echo $i | xargs git remote add 2>/dev/null || echo $i | xargs git remote set-url ; done
```
(command stolen from gitbbs lol)

which will go through all the remotes in remotes.txt and add them to git

:D

