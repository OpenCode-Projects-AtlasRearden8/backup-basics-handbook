# Recipe 5 — The Yearly Archive Check

**Goal:** once a year, prove your whole archive still opens, fix weird
names, and migrate anything in formats going stale. Thirty minutes in,
decades of quiet confidence out.

**You need:** your archive (drive, cloud, or both), your current computer,
and a refill of whatever beverage keeps you at the desk.

## The yearly pass

**1. Open the archive itself.** Browse the drive — is the folder structure
readable? Cloud folder — does everything still say "synced"?

**2. The open test: three files, at random.**

- One **PDF** — opens, renders, looks right.
- The **oldest file** in the whole archive — this is the canary. If the
  ten-year-old text/photo opens, your formats are aging gracefully.
- One **spreadsheet/CSV or document** — opens with real data, not garbage
  characters.

**3. Name sweep.** Scroll for a minute. Anything you can't *exactly*
identify from its name alone gets renamed with the date pattern
(`YYYY-MM-DD-what-it-is.pdf`). Future-you writes thank-you notes.

**4. Format migrations.** Move anything living on old media — CD/DVDs,
camera cards, unlabeled USB sticks — into your normal folders, in modern
formats (chapter 6's table). Write "migrated the old camera-card files into the archive"
on the worksheet so you know it happened.

**5. Location sanity.** Offsite copy still offsite? (Drive B still at
Aunt Rosa's? Cloud account still logged in from your phone?) Twenty
seconds, and this is the check that normally catches the *one* physical
copy that wandered into been-lost-land.

**6. Version hygiene.** If you keep dated backup folders
(`Backups-2024-11`, `Backups-2025-08`, `Backups-2026-10`), keep them
until the drive is nearly full, then delete the *oldest* only. Never
delete the newest. That's the whole retention policy. Officials would
call it "grandfather-father-son"; you can call it "keep a few."

## Check your work, mechanically

On Linux/macOS, list your archive with sizes and sanity checks:

```sh
# what's actually in the archive, biggest things first
du -ah /media/YOURDRIVE/Backups/  | sort -rh | head -20

# every PDF and JPEG there, counted by type
find /media/YOURDRIVE/Backups/ -type f \( -iname "*.pdf" -o -iname "*.jpg" \) | wc -l

# text files that might actually be empty or corrupt (zero bytes)
find /media/YOURDRIVE/Backups/ -type f -empty
```

**Tested:** these three commands were run in this handbook's test shell
against a built backup tree — they behave exactly as described.

Zero-byte surprises (`-empty`) are rare but real; if any appear, check
their twins in a newer backup folder before panicking, and copy over the
healthy version.

## If something's off

- **An old file won't open** → find its plain twin (PDF next to the
  fancy app file; text/.md next to the rich document). Update the alive
  copy, re-save, and write the lesson on the worksheet.
- **Archive looks scrambled or names are hopeless** → don't fix it all
  today. Set a monthly 20-minute "archive tidying" block; four months of
  gentle renaming beats one heroic night.
- **You found files that exist nowhere else** → congratulations: the
  yearly check just did exactly what it's for. Copy them into the
  treasure folder, run recipe 1, and enjoy having dodged a small tragedy
  on purpose.

---

*That's the last recipe. After it: give your worksheet a date, pour
something nice, and go tell someone they should borrow this book.*
