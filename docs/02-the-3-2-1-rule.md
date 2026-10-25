# The 3-2-1 Rule, No Jargon

Every serious backup guide eventually says "3-2-1" and then buries it in
storage-engineer language. Here's the friendly version.

## The rule

Keep:

- **3 copies** of anything you care about,
- on **2 different kinds** of thing,
- with **1 copy somewhere else** entirely.

That's it. Now let's make sure each number makes sense, because the logic is
what makes the rule stick.

## Why 3 copies?

Because stuff happens **twice, at the same time**, more often than you'd
think. Your laptop dies **while** your external drive is unplugged and useless.
The cloud account won't sync **while** your house's internet is down. One
backup is a spare. Two backups are a system.

The original copy counts as number one. So "3 copies" usually means:
original + one drive + one cloud account.

## Why 2 different kinds?

Because two copies on the same "kind" of thing tend to die together. Two
folders on the same laptop = one coffee spill. Two drives from the same
delivery box that sit next to each other = one lightning strike, one theft,
one surge. Different *kinds* might be:

- the original on your computer, plus
- an external drive, plus
- an online account (cloud).

The "different kind" idea is really about **not putting eggs in one basket
shape**. A USB stick and an external drive both count as drives, but they're
different physical objects and that already helps.

## Why 1 somewhere else?

Because some disasters eat everything in the room: fire, flood, theft, the
notorious lightning strike. If your spare drive lives in the same drawer as
the laptop, a burglar gets a two-for-one.

"Somewhere else" can be low-tech and free-ish: a relative's closet, your
desk drawer at work, a fireproof box in the garage, or — easiest of all — a
cloud account, which is "somewhere else" by definition.

## What counts, what doesn't

| This... | Counts as a 3-2-1 copy? |
| --- | --- |
| Original file on your laptop | Yes — it's copy #1 |
| Copy on an external drive | Yes |
| Copy in a cloud account | Yes |
| Copy on the same laptop, "in a different folder" | **No** — one basket |
| Copy on a drive that lives in the same bag as the laptop | Half — better than nothing, dies in the fire |
| Two cloud accounts | Yes — genuinely independent |
| A sync folder (file deleted here = deleted there) | It's a mirror, not a history — see the warning box |

> **Friendly warning:** a *syncing* folder keeps the latest version, both
> ways. That's great for convenience and terrible for "I deleted it last
> Tuesday and want it back." That's why at least one of your copies should
> be a plain, dumb copy — a drive you plug in and copy to — that doesn't
> know or care what you deleted elsewhere.

## A real-life example

Meet Pat. Pat's treasures: 60 GB of family photos, tax PDFs, a resume, and
the spreadsheet that runs the household. Pat's 3-2-1:

- **Copy 1** — lives on the laptop (original).
- **Copy 2** — an external drive, plugged in Sunday nights, one folder
  copied over. Label says "PHOTOS+PAPERS."
- **Copy 3** — phone photos auto-upload to a free cloud tier; Pat also drops
  the Documents folder into a free cloud drive once a month.

Total cost: one drive, zero dollars of software, ten minutes a week. Pat is
not a genius. Pat just started.

## Cheat-sheet version

> **Three copies. Two kinds. One elsewhere. Test it.**
> (The "test it" part is chapter 7 — restore drills — and it's the half
> everyone skips. Not you, though.)

## Do this today

1. Look at yesterday's top-three folder.
2. Decide its home #2 and home #3: an external drive (chapter 3 has buying
   advice) and either a cloud account or a second drive that lives elsewhere.
3. Write those two homes on your worksheet. That's your 3-2-1 plan — the
   actual copying is just recipes waiting to be run.
