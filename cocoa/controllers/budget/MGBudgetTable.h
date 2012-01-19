/* 
Copyright 2011 Hardcoded Software (http://www.hardcoded.net)

This software is licensed under the "BSD" License as described in the "LICENSE" file, 
which should be included with this package. The terms are also available at 
http://www.hardcoded.net/licenses/bsd_license
*/

#import <Cocoa/Cocoa.h>
#import "PyBudgetTable.h"
#import "MGTable2.h"

@interface MGBudgetTable : MGTable2 {}
- (id)initWithPy:(id)aPy tableView:(MGTableView *)aTableView;
- (void)initializeColumns;
- (PyBudgetTable *)model;
@end
