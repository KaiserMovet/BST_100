
Node = {}

function Node.new (value)
    local self = {value = value, left=nil, right=nil}
    self.add = Node.add
    self.contain = Node.contain
    self.length = Node.length
    self.height = Node.height
    return self
end

function Node:add(value)
    if value<self.value then
        if self.left == nil then
            self.left = Node.new(value)
            return true
        end
        return self.left:add(value)
    end

    if value>self.value then
        if self.right == nil then
            self.right = Node.new(value)
            return true
        end
        return self.right:add(value)
    end

    return false
end

function Node:contain(value)
    if value < self.value then
        if self.left == nil then
            return false
        end
        return self.left:contain(value)
    end

    if value > self.value then
        if self.right == nil then
            return false
        end
        return self.right:contain(value)
    end

    return true
end

function Node:length()
    local left_len = 0
    if self.left ~= nil then
        left_len = self.left:length()
    end

    local right_len = 0
    if self.right ~= nil then
        right_len = self.right:length()
    end

    return left_len + right_len + 1
end

function Node:height()
    local left_height = 0
    if self.left ~= nil then
        left_height = self.left:height()
    end

    local right_height = 0
    if self.right ~= nil then
        right_height = self.right:height()
    end

    return 1 + math.max(left_height, right_height)
end