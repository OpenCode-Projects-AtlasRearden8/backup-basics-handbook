# Recipe 1 — Make Your First Real Copy

**Goal:** the treasure folder ends up on an external drive, verified.
**You need:** your computer, an external drive with room to spare, 10–20
minutes. The drive should already be formatted and have a `Backups` folder
(chapter 3's ten-minute setup).

## Option A — by dragging (any operating system)

1. Plug the drive in. Open it so you can see the `Backups` folder.
2. Open your treasure folder in another window.
3. Select everything in it and **copy** (right-click → Copy; Ctrl/Cmd-C),
   then paste into `Backups`. Copy, never move — cut is how treasures
   become fugitives.
4. First time: wait it out, all of it, progress bar honorably watched.
   Later runs only copy what changed, so this gets faster.

> **Windows tip:** use **Copy**, not "Send to," so you can paste into the
> folder of your choosing.

## Option B — one reliable command (Linux)

In a terminal, replacing the paths with yours:

```sh
cp -aut /media/YOURDRIVE/Backups/treasures/ \
        ~/Documents/my-treasures/.
```

- `cp` — the file-copying command that ships with every Linux system; no
  installing anything.
- `-a` — copies faithfully, keeping dates and folder structure.
- `-t` — "target": copy *into* the destination you name.
- `-u` — only copies files that are new or changed, so re-running this
  next week takes seconds.
- The `/.` means "the contents of that folder," not the folder itself.
- The destination folder must already exist (your ten-minute setup in
  chapter 3 made it) — otherwise start with
  `mkdir -p /media/YOURDRIVE/Backups/treasures`.

**macOS variation:** `ditto ~/Documents/my-treasures /media/YOURDRIVE/Backups/treasures`
(native, keeps everything faithfully), or the plain drag version above.

## Option C — Windows classic, one command

In Command Prompt (press Start, type `cmd`):

```bat
robocopy "C:\Users\you\Documents\my-treasures" "E:\Backups\treasures" /E /XJ /FFT /DCOPY:T
```

`/E` copies folders-within-folders, `/XJ` politely skips system pseudo-
links, and the rest keeps timestamps tidy. Re-run the same line weekly;
robocopy also only copies what changed.

**Tested:** option B's exact command (with a stand-in drive folder)
was run end to end in this handbook's test shell — first copy, re-run,
and file counts all checked out — and the same harness proves the restore
drill in recipe 2. Option A's clicks and option C's one-liner follow each
system's own documentation; menu names drift, commands don't.

## Check your work

1. On the drive, open the copied folder — files are there, dates look right.
2. Spot-check: open one photo and one document **from the drive** and see
   they open fine.
3. Compare counts (rough is fine): same-ish number of items in both
   folders.
4. Write the date on the drive's masking tape.

## If something's off

- **"No space left"** → drive too small for the treasure; get a bigger
  drive, or archive last year's dated folders to a second drive.
- **Copy fails partway / drive vanishes mid-copy** → different cable/port
  first; if it insists, treat the drive as unreliable (chapter 3).
- **"Access denied" on some files** → don't chase it tonight; note which
  folder misbehaved and check tomorrow with a fresh boot.

---

*Next: recipe 2, where we delete one of these on purpose, just to prove we
can get it back. That's where backups become backups.*
