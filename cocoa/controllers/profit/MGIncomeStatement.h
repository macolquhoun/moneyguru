/* 
Copyright 2011 Hardcoded Software (http://www.hardcoded.net)

This software is licensed under the "BSD" License as described in the "LICENSE" file, 
which should be included with this package. The terms are also available at 
http://www.hardcoded.net/licenses/bsd_license
*/

#import <Cocoa/Cocoa.h>
#import "MGReport.h"
#import "MGPieChart.h"
#import "MGBarGraph.h"
#import "MGDoubleView.h"

@interface MGIncomeStatement : MGReport {}
- (id)initWithPy:(id)aPy view:(HSOutlineView *)aOutlineView;
- (void)initializeColumns;
@end