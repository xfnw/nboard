# Nboard

Python curses based YourWallOftext clone

## Help
Read the --help text lol


## Managing Remotes
To get more remotes, you can

```bash
for i in $(cat remotes.txt); do echo $i | xargs git remote add 2>/dev/null || echo $i | xargs git remote set-url ; done
```
(Command stolen from gitbbs lol)

Which will go through all the remotes in remotes.txt and add them to git


