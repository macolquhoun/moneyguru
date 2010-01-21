/* 
Copyright 2010 Hardcoded Software (http://www.hardcoded.net)

This software is licensed under the "HS" License as described in the "LICENSE" file, 
which should be included with this package. The terms are also available at 
http://www.hardcoded.net/licenses/hs_license
*/

#import <Cocoa/Cocoa.h>
#import "PyGUI.h"

@interface PyGUIContainer : PyGUI {}
// Rather than having a 3km long method name (this is objc, remember), we're passing a list of
// instances here. However, they *have* to be in the right order. See the corresponding core class
// for the correct order.
- (id)initWithCocoa:(id)cocoa pyParent:(id)pyParent children:(NSArray *)children;
@end