# Recipe 3 — Turn On Automatic Backups

**Goal:** your operating system quietly making copy #2 for you, forever.
**You need:** your computer and an external drive. Ten minutes.

This is the "set it once and stop thinking about it" option — your OS's
built-in backup tool keeps versioned backups on an always-plugged-in drive
(accidentally deleted a file last Thursday? Tuesday's copy is right there).

## macOS — Time Machine

1. Plug the drive in.
2. Apple menu → **System Settings** → **General** → **Time Machine**.
3. **Add Backup Disk**, pick your drive, switch backups on.
4. Optional but friendly: exclude folders you don't need backed up (Options
   → Exclude), so the drive stays lean.
5. First backup runs for a while (it's copying your whole life, be kind).
   Later ones happen hourly, in the background, for about an hour after
   each time you plug in.

**Check your work:** the Time Machine settings page shows the latest
backup's time and size growing. Also try it once: click the Time Machine
icon → "Enter Time Machine" → flip back to yesterday → restore one file.
That's a drill done for free.

## Windows — File History

1. Plug the drive in and open **Settings** → search for **File History**
   (Control Panel's "Save backup copies of your files with File History").
2. Make sure the drive is listed, and **Turn on**.
3. Under **Advanced settings**, choose how often it copies (hourly is the
   default; hourly or nightly, both are fine — the point is that it isn't
   off).
4. Start a first run with **Run now** so you can watch it work.

**Check your work:** after an hour+, use **Restore personal files** from
the same panel and flip to a previous version of a folder. See a file from
Tuesday sitting there? Pass.

## The friendly notes

- Set it and *forget it correctly*: these tools keep **version history**
  (the memory of past copies), which plain drag-copy doesn't — that's the
  mirror-vs-history idea from chapter 2, implemented for you.
- **Menu names drift.** System settings get reorganized as often as kitchen
  cabinets. If names don't match, search the settings for the words
  "Time Machine" or "File History" — the features keep their names even
  when the shelves move.
- This recipe covers copy #2 (a local, versioned copy). You still want
  copy #3 offsite — recipe 1's rotated drive or recipe 4's cloud account.
- Laptops on the move: these tools still work — backup runs when the
  drive's attached; keep the drive in your *home*, not in the same bag.

**Honest tested-note:** this recipe was written from each OS's own help
documentation and checked against current menus as of writing; we
couldn't run Time Machine or File History on the machine this handbook
was built on. If a menu name has moved, the feature hasn't.
