require "tree"

function read_numbers_from_file(file_name, amount)
    local numbers = {}
    local file = io.open(file_name, "r")
    if file then
        for line in file:lines() do
            if #numbers >= amount then
                break
            end
            local number = tonumber(line)
            if number then
                table.insert(numbers, number)
            end
        end
        file:close()
    end
    return numbers
end


function main ()

    local amount = tonumber(arg[1])

    local add_numbers = read_numbers_from_file("/datasets/add.txt", amount)
    local check_numbers = read_numbers_from_file("/datasets/check.txt", amount)

    
    local tree = Tree.new()
    local start_time, end_time
    
    -- Add elements
    start_time = os.clock()
    for _, value in ipairs(add_numbers) do
        tree:add(value)
    end
    end_time = os.clock()
    print("ADD_TEST:"..(end_time - start_time))

    -- Check elements
    start_time = os.clock()
    for _, value in ipairs(add_numbers) do
        tree:contain(value)
    end
    end_time = os.clock()
    print("CHECK_TEST:"..(end_time - start_time))

    -- Len elements
    start_time = os.clock()
    for i=1,10 do
        tree:length()
    end
    end_time = os.clock()
    print("LEN_TEST:"..(end_time - start_time))

    -- height elements
    start_time = os.clock()
    for i=1,10 do
        tree:height()
    end
    end_time = os.clock()
    print("HEIGHT_TEST:"..(end_time - start_time))

    print("VALIDATION:"..tree:length()..":"..tree:height())



end
main()