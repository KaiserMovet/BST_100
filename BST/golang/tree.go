package main


type Tree struct {
	root *Node
}


func (self *Tree) Add(value int) bool {
	if self.root == nil {
		self.root = &Node{value: value, left:nil, right:nil}
		return true
	}
	return self.root.Add(value)
}

func (self *Tree) Contain(value int) bool {
	if self.root == nil {
		return false
	}
	return self.root.Contain(value)
}

func (self *Tree) Length() int {
	if self.root == nil {
		return 0
	}
	return self.root.Length()
}

func (self *Tree) Height() int {
	if self.root == nil {
		return 0
	}
	return self.root.Height()
}