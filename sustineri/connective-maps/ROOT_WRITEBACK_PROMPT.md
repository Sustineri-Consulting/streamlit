# Handoff Prompt — ROOT Write-Back (run in a WRITE-ENABLED local OneDrive/ROOT session)

> Copy everything in the fenced block below into a new session that has **write access**
> to the canonical OneDrive ROOT (`00_System_Core/AI_Operating_System/`). This session
> was read-only and could not perform the write-back; all rows are pre-staged.

---

```
You have WRITE access to the Sustineri canonical ROOT OneDrive:
  /Users/angeline/Library/CloudStorage/OneDrive-SustineriConsultingGroup/00_System_Core/AI_Operating_System/

TASK: Apply the pre-staged ROOT write-back for connective-map asset MAP-WORKARCH-002
(Sustineri_Connective_Map_002_AI_Work_Architecture). Do NOT design or re-render anything.
Apply the rows EXACTLY as written in the repo file:
  repo: sustineri-consulting/streamlit
  branch: claude/shrm-ai-connective-map-hci72b
  file: sustineri/connective-maps/ROOT_WRITEBACK_PAYLOAD.md
(Pull that branch first; open ROOT_WRITEBACK_PAYLOAD.md and use its rows verbatim.)

HARD CONSTRAINTS
- Do NOT fake, recreate, redraw, or substitute the Sustineri protected logo. The asset
  stays FINAL-PENDING-LOGO. If the real mark (sustineri-mark.png) is composited, note it;
  otherwise leave the logo slot pending and say so.
- Only mark a tracker "updated" AFTER the write actually lands. No pre-emptive status.
- Do NOT merge the PR and do NOT change it from Draft.
- Append (never overwrite) existing tracker content. Match each tracker's existing
  column/heading format; adapt the staged row to that format if needed.

STEPS
1. Copy the two final PNGs into the appropriate ROOT output/archive lane, keeping the
   series name Sustineri_Connective_Map_002_AI_Work_Architecture_*:
     - .../output/shrm_ai_work_architecture_connective_map_watermarked_brandv2.png  (primary)
     - .../output/shrm_ai_work_architecture_connective_map_watermarked_brandv2_alt.png (alt)
2. Append the staged rows to:
     - 04_Trackers/Master_Output_Index.md
     - 04_Trackers/Master_Change_Log.md
     - 04_Trackers/01_Daily_Work_Logs/2026-07-01_Daily_Work_Log.md
     - 06_Validation_Systems/Agent_Output_Proof_Log.md
     - _closeout_runlog.md  (only if a closeout flow is active)
3. In each row, keep status = "brandv2 / FINAL-PENDING-LOGO" and reference PR #1:
     https://github.com/Sustineri-Consulting/streamlit/pull/1

REPORT BACK (with proof paths)
- ROOT PNGs written: Yes/No + exact ROOT paths
- Master Output Index updated: Yes/No + path + appended line
- Master Change Log updated: Yes/No + path + appended line
- Daily Work Log updated: Yes/No + path + appended line
- Agent Output Proof Log updated: Yes/No + path + appended line
- Closeout runlog updated: Yes/No/NA + path
- Logo composited: Yes/No (must be No unless the real protected mark was used)
- Asset status: Final-pending-logo (unless logo composited)
- Loop closed: Partial until logo + all tracker writes have proof paths
```

---

## After the write-back returns proof paths
1. Paste the returned ROOT paths/line-refs into `CANONICAL_VALIDATION.md` (flip the tracker
   items to "updated" **with** proof paths).
2. Loop can move from **Partial → Closed** only when BOTH are true: the real protected logo
   is composited into the assets, and all tracker writes have proof paths in ROOT.
3. PR stays **Draft** until founder approval to merge.
