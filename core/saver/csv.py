# Created By: Virgil Dupras
# Created On: 2010-10-26
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

import csv

from ..model.amount import format_amount
from ..model.date import format_date

def save(filename, accounts):
    fp = open(filename, 'wt', encoding='utf-8')
    writer = csv.writer(fp, delimiter=';', quotechar='"')
    HEADER = ['Account', 'Date', 'Description', 'Payee', 'Check #', 'Transfer', 'Amount', 'Currency']
    writer.writerow(HEADER)
    for account in accounts:
        for entry in account.entries:
            date_str = format_date(entry.date, 'dd/MM/yyyy')
            transfer = ', '.join(a.name for a in entry.transfer)
            amount_fmt = format_amount(entry.amount, entry.amount.currency)
            row = [account.name, date_str, entry.description, entry.payee, entry.checkno, transfer,
                amount_fmt, entry.amount.currency.code]
            writer.writerow(row)
    fp.close()
