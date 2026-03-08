# -*- coding: utf-8 -*-
{
    'name': 'Payroll Payslip Report Fix',
    'version': '1.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Fixes payslip report month heading to use End Date instead of Start Date',
    'description': """
Payroll Payslip Report Fix
==========================
Fixes Bug #2: Wrong Month Heading in Payslip Report

- **BEFORE:** Payslip title used o.name (Start Date) - e.g. "November 2025 Payslip" for period 21/11/2025-20/12/2025
- **AFTER:** Payslip title uses o.date_to (End Date) - e.g. "December 2025 Payslip" for period 21/11/2025-20/12/2025

This inherited view replaces the payslip heading to display the correct month based on the period end date.
    """,
    'author': 'Namma',
    'depends': ['hr_payroll'],
    'data': [
        'views/report_payslip_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
