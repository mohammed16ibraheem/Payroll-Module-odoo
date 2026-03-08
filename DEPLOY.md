# Deploy to GitHub & Vercel

## Push to GitHub

Run these commands from the **Payroll Module** folder (the one containing `index.html`, `README.md`, images, etc.):

```bash
git init
git add .
git commit -m "Payroll module report - Odoo fixes"
git branch -M main
git remote add origin https://github.com/mohammed16ibraheem/Payroll-Module-odoo.git
git push -u origin main
```

## Deploy to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click **Add New Project**
3. Import `mohammed16ibraheem/Payroll-Module-odoo`
4. Vercel will detect it as a static site (no build needed)
5. Click **Deploy**

Your report will be live at `https://your-project.vercel.app`

## What Gets Deployed

- **index.html** — Main report (served as homepage)
- **1.png – 100.png** — Screenshots
- **PDFs** — Payslip documents
- **hr_payroll_payslip_fix/** — Odoo module for Fix 2
