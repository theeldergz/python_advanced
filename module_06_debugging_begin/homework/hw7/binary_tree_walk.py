"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    with open(path_to_log_file, 'r', encoding='utf-8') as log_file:
        data = log_file.readlines()

    node_info_dict = {}
    root_num = int(data[0][30:36])
    binary_tree_root = BinaryTreeNode(val=root_num, left=None, right=None)

    for log in data:
        if log.startswith('INFO'):
            node_value = int(log[30:36])
            node_info_dict[node_value] = BinaryTreeNode(val=node_value)

        if log.startswith('DEBUG') and 'left' in log:
            node_value = int(log[73:79])
            node_info_dict[node_value] = BinaryTreeNode(val=node_value,
                                                        left=BinaryTreeNode(node_value))

        if log.startswith('DEBUG') and 'right' in log:
            node_value = int(log[74:80])
            node_info_dict[node_value] = BinaryTreeNode(val=node_value,
                                                        right=BinaryTreeNode(node_value))
    return binary_tree_root


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_6.txt",
    )

    root = get_tree(7)
    walk(root)