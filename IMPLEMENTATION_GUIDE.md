# Payroll Module — Implementation Guide

Based on the blue-marked images in your Payroll Module folder, here is what each fix requires and how to implement it.

---

## ✅ Blue-Marked Images — Summary

| Image | Blue Marking | Action |
|-------|--------------|--------|
| 1 | Payroll module icon | Open Payroll module |
| 3 | Configuration tab | Go to Configuration |
| 14 | Configuration + Work Entry Types | Open Work Entry Types |
| 16 | Paid Time Off row | Edit Paid Time Off |
| 19, 20, 21, 100 | Time Off checkbox (unchecked) | **Fix 1 — Uncheck Time Off** |
| 22–29 | Generic, Compensatory, Unpaid | Same: uncheck Time Off for each |
| 50 | Views list | Go to report views |
| 60 | **Line 4 of report template** | **Fix 2 — Change heading code** |
| 11 | AAVEZ DALVI — January 2026 | Test result (Fix 2) |

---

## Fix 1 — Disable Time Off → Payroll Link

**Navigation:** Payroll → Configuration → Work Entry Types

**Action:** For each leave-type work entry, **uncheck the "Time Off" checkbox** under **TIME OFF OPTIONS**:

| Work Entry Type | Code | Action |
|-----------------|------|--------|
| Generic Time Off | LEAVE100 | ☐ Uncheck Time Off |
| Compensatory Time Off | LEAVE105 | ☐ Uncheck Time Off |
| Unpaid | LEAVE90 | ☐ Uncheck Time Off |
| Sick Time Off | LEAVE110 | ☐ Uncheck Time Off |
| Paid Time Off | LEAVE120 | ☐ Uncheck Time Off |

**Result:** Time Off is no longer auto-imported into payslip Worked Days. Salary is not reduced by leave unless you adjust it manually.

---

## Fix 2 — Payslip Report Month Heading

**Option A — Odoo UI (temporary, may be overwritten by updates):**

1. Settings → Technical → User Interface → Views  
2. Search: `report_payslip`  
3. Open: `hr_payroll.report_payslip`  
4. In the **Architecture** tab, change line 4:

   **BEFORE:**
   ```html
   <h2 id="payslip_name"><span t-field="o.name">August 2023 Payslip</span></h2>
   ```

   **AFTER:**
   ```html
   <h2 id="payslip_name"><span t-esc="o.date_to.strftime('%B %Y') + ' Payslip'"/></h2>
   ```

5. Save

**Option B — Odoo module (permanent, upgrade-safe):**

1. Copy the `hr_payroll_payslip_fix` folder into your Odoo addons path.  
2. Update the addons list and install the module **Payroll Payslip Report Fix**.  
3. The heading will use the period end date for the month (e.g. "December 2025" for period 21/11/2025–20/12/2025).

---

## Test Checklist

- [ ] **Time Off:** Paid Time Off work entry has Time Off **unchecked** (see images 19, 20, 21, 100).  
- [ ] **Report heading:** RAM LAL (21/11–20/12) shows **"December 2025 Payslip"** (not November).  
- [ ] **Report heading:** AAVEZ DALVI (01/01–31/01) shows **"January 2026 Payslip"** (see image 11).
