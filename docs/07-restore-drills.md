# Restore Drills: Backups Only Count If You Can Restore

Here's the uncomfortable little secret of the backup world: most "backups"
are feelings, not systems. The drive blinks. The cloud icon is blue.
Everything *seems* backed up. Nobody has ever tried getting a file back.

This chapter turns your backup from a feeling into a tested system, the way
fire drills turn alarm bells into muscle memory. Every three months:
**one file, one restore, one verify.** Fifteen minutes, tops.

## The drill, universal version

1. **Pick a test file.** Choose a real file from the middle of your treasure
   folder — a photo, a spreadsheet, whatever. Pick a *real* one, not a
   throwaway doc; the point is confidence, and fake drills breed fake calm.
2. **Copy it to a temp spot** (the "original, still safe" copy — we're not
   being brave here; we're being smart).
3. **Delete the file from its home folder.** Deep breath — the temp copy
   means nothing can actually hurt you.
4. **Empty trash/Recycle Bin too**, if you want the full-clear drill (skip
   for round one — no shame).
5. **Restore it.** Here's where the actual backup gets to show what it
   knows:
   - **Drive copy:** open the drive, find the matching file in your dated
     folders, drag it back.
   - **Cloud/mirror:** log in (a *different device* is a fairer test —
     phone instead of computer) and download it.
   - **Phone photos:** open the photo app on another device and *see* the
     photo exists there; ideally, download/save one to be sure.
6. **Verify, don't squint.** Open the restored file. For anything with
   two-copy trick, check the checksum/screening step from recipe 2 — on
   Linux/Mac that's one `cksum`/`shasum` command, as shown there.
7. **Log it.** Date a line in your worksheet's drill log: "2026-10-25,
   restored lease.pdf from drive A, opened fine." Three satisfied checkmarks
   a year beats a nagging feeling of *maybe*.

## What the drill actually tests

This is why it works — each restore path has a different failure mode, and
the drill catches the real one:

- **The setup failed silently.** A backup app that hasn't actually backed
  anything up since the last OS update (the classic).
- **You can't get in.** Password expired, auth app lost, account locked
  out. Discovering this from your couch is vastly better than discovering
  it from the worst possible day.
- **The restore path is missing or wrong.** The file's *there* but no app
  opens it, or the drive's dated-folders structure didn't match what your
  muscle memory assumed.
- **The entire drive is dead.** Yes, drives die even while sitting in
  drawers. Better to learn it on drill day.

## Cloud-only drill, extra version (twice a year)

Log in *from another device entirely*, and actually download — no peeking,
real download:

1. On a different device (your phone, or a friend's computer logged into a
   **private** window — never a shared/public computer), open the cloud
   folder.
2. Download one file. Open it. It's identical? Pass.
3. Also check the free-space and account-status pages once: limits, billing,
   password freshness.

## Phone-photos drill (the one with the feelings)

Twice a year, on your computer's browser:

1. Open the photo site and search for a specific memory ("beach 2023").
2. Download one photo.
3. If you keep a paper/archive copy: flip through your latest dated photo
   folder for a minute and confirm it looks sane.

This one drill is what stops the 3 a.m. thought — "wait, does the baby
album ACTUALLY exist anywhere else?" — from ever coming back.

## Keeping score on the worksheet

The worksheet has a small drill log on it. Use it like this:

| Date | What I restored | From where | Opened OK? |
| --- | --- | --- | --- |
| 2026-10-25 | lease PDF | drive A | yes |

A quarter with no entry means the rhythm slipped. Gently
restart the rhythm; the recipes in the back make each session mechanical.

## Do this today

1. Open recipe 2 ("Prove You Can Restore") — it's the drill, command
   versions included, with your first log line ready to write.
2. Run it once. Right now. Yeah — you, today, now. It's fifteen minutes.
3. Fill the first row of your drill log. First one's free; the second is
   scheduled three months out.

> **Make it quarterly, not someday.** Calendar it now: first Saturday of
> the next two quarters, name it "backup drill + coffee." The coffee is
> load-bearing.
