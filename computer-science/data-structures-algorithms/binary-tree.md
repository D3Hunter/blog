### tree traversal iterative method
在三种traversal方式里，stack里的节点顺序，不一定是一个tree-path
stack里是已经遍历但还未visit的节点，按顺序排列；node是还未遍历的节点

preorder
- 栈上留着当前节点，需要一种方式判断该节点是否是第一次遇到，recusive方法通过执行流即可知道，iterative就需要额外判断
- 栈上留当前节点仅是为了把right放进来，可以扔掉该节点直接把right放进来
inorder
- 一直往左走，走到头visit，往右
- 代码能简化成只有一个循环
postorder
- 需要一种方式判断处理当前节点时，其right是否处理过。lastVisited
- postorder和preorder是很像的，只是对于任意子树，结果顺序为左右Root，而preorder为Root左右。对于特殊的visit如获取其值，可以对preorder算法适当调整得到postorder的算法。

