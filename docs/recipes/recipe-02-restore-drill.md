# Recipe 2 — Prove You Can Restore

**Goal:** run a real restore drill, then log it on the worksheet. The one
recipe that makes all the others worth it.

**You need:** your backup copy (drive or cloud) and 15 minutes. Nothing can
be lost here — we make a safety copy of the victim before touching it.

## The drill (click version, any OS)

1. Choose a real file from your treasure folder — say, `2026-05-01-lease.pdf`.
2. **Safety first:** copy that file to your Desktop or a temp folder. This
   copy means the drill literally cannot destroy anything.
3. Delete the file from its home. (Round two: empty the trash, too.)
4. Open your backup — the drive, or the cloud folder on a *different device*
   if it's cloud.
5. Find the file in backup and copy it back to its home folder.
6. **Open it.** All the way, not just the icon. The point is a working file,
   not a smug file.
7. Write a line in the worksheet's drill log: date, what, from where,
   "opened: yes."

That's the whole drill. Here's the same thing in shell commands, if you
like seeing the machinery.

## The drill (command version — Linux / macOS)

**Tested:** every command in this section was run on Linux as written,
with the checksum step confirming the restored file matched the original
byte for byte.

```sh
# 1. make a victim and the daily "work" it belongs to
mkdir -p ~/drill-demo/treasures
echo "the trilogy draft" > ~/drill-demo/treasures/trilogy-draft.txt

# 2. back it up (the recipe-1 pattern, tiny edition)
mkdir -p /tmp/drill-drive/Backups/treasures
cp -aut /tmp/drill-drive/Backups/treasures/ ~/drill-demo/treasures/.

# 3. copy the victim to a safe temp spot, then delete the original
cp ~/drill-demo/treasures/trilogy-draft.txt /tmp/trilogy-safe.txt
rm ~/drill-demo/treasures/trilogy-draft.txt

# 4. confirm the loss is real
ls ~/drill-demo/treasures/          # empty, and that's allowed to sting

# 5. restore from backup
cp -aut ~/drill-demo/treasures/ /tmp/drill-drive/Backups/treasures/.

# 6. verify: byte-for-byte identical?
cksum /tmp/trilogy-safe.txt ~/drill-demo/treasures/trilogy-draft.txt
#   on macOS use: shasum -a 256 both-files
```

`cksum` prints a fingerprint for each file; the two numbers matching means
the restored copy is exactly the file you lost. Numbers differ? Then the
backup copy wasn't what you thought — go one level back (is it copying at
all? did the "drive" folder get deleted?) and be glad you found out on
drill day.

## For phone-photos people

Quarterly, twice at most while you're new: open the photo site on your
computer, search a specific memory, and **download one photo**. Optionally
save it to your dated photos folder. Log it. (The feelings version is
explained in chapter 7.)

## Check your work

- [ ] File was deleted from home folder
- [ ] File was restored from backup (drive or cloud)
- [ ] File opened, and its checksum/screening matched (commands or your own squint)
- [ ] Drill log got a row

## If something's off

- **File isn't in the backup at all** → your backup missed it. Check which
  folders your recipe/app actually copies — this discovery is the drill
  earning its entire annual salary.
- **Restore copy won't open** → see chapter 6: is a PDF/plain copy sitting
  next to it? If all copies of that file are in one rotting format, that
  file just taught you the lesson of chapter 6 for free.
- **The "drive" turned out to be junk** → good thing it was a drill. Say
  something kind about the drive's service, buy a new one, re-run recipe 1.
