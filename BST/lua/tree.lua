require "node"

Tree = {}

function Tree.new()
    local tree = {root = nil}
    tree.add = Tree.add
    tree.contain = Tree.contain
    tree.length = Tree.length
    tree.height = Tree.height
    return tree
end

function Tree:add(value)
    if self.root == nil then
        self.root = Node.new(value)
        return true
    end
    return self.root:add(value)
   
end

function Tree:contain(value)
    if self.root == nil then
        return false
    end
    return self.root:contain(value)
end

function Tree:length(value)
    if self.root == nil then
        return 0
    end
    return self.root:length(value)
end

function Tree:height(value)
    if self.root == nil then
        return 0
    end
    return self.root:height(value)
end