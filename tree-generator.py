class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class treegenerator():
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.l = len(self.nodelist)

    def gen(self):
        root = TreeNode(self.nodelist[0])
        i = 1
        q = [root]
        while (q) and i < self.l:
            while not q[0].val:
                q.pop(0)
            cur = q.pop(0)
            if i < self.l:
                t1 = TreeNode(self.nodelist[i]) if self.nodelist[i] else None
                cur.left = t1

            if i < self.l - 1:
                t2 = TreeNode(self.nodelist[i + 1]) if self.nodelist[i] else None
                cur.right = t2

            q += [cur.left, cur.right]
            i += 2
        return root

if __name__ == "__main__":
    tg = treegenerator([1,2,3,4,None,2,4,None,None,4])
    root = tg.gen()
    print()