### preorder/inorder/postorder
recusive算法
通过函数栈及代码中的调用顺序保证便利顺序，使用non-recusive方法时需要保证这两者，即显示stack和访问状态（保证处理顺序）

non-recusive算法
- preorder
    1. stack上保留path和访问状态（避免right节点多次访问），根据两者来判断
    2. 遍历某节点时按right、left顺序放入stack，当前节点visit后pop。该方法相当于对前者的简化，省略了状态，path中的父节点只是用来根据状态插入right
- inorder：
    1. stack上保留path和访问状态（避免right节点多次访问），但visit后保留下的节点可以去掉，简化为方法2
    2. 不保留path
        1. 先走到leftmost节点；
        2. pop元素、visit；
        3. 针对right回到步骤1。
    3. 不保留path, 方法2中的“leftmost节点”的内循环可以跟外循环合并为一个, 参考wikipedia
- postorder：遍历顺序决定了都需要存储完整path
    1. stack保留path和访问状态（避免right节点多次访问），处理过right才能visit，类似inorder，需要leftmost优先。
    2. stack保留path，通过一个lastVisitedNode节点，来识别当前遍历顺序是往下、从左边往上或从右边往上
    3. 方法1中的“leftmost节点”的内循环可以跟外循环合并为一个，类似方法2，但lastVisitedNode只需判断是否是右节点，参考wikipedia
