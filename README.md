# nboard

python curses based yourwalloftext clone

## managing remotes
to get more remotes, you can

```bash
for i in $(cat remotes.txt); do echo $i | xargs git remote add 2>/dev/null || echo $i | xargs git remote set-url ; done
```
(command stolen from gitbbs)

which will go through all the remotes in remotes.txt and add them to git
