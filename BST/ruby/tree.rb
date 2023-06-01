require_relative 'node'

class Tree 
    @root

    def initialize()
    end

    def add(value)
       if @root.nil?
            @root = Node.new(value)
            return true
       end
       return @root.add(value)
    end

    def contain(value)
        if @root.nil?
            return false
        end
        return @root.contain(value)
     end

     def length()
        if @root.nil?
            return 0
        end
        return @root.length()
     end

     def height()
        if @root.nil?
            return 0
        end
        return @root.height()
     end

end
