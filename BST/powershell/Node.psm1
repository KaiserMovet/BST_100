
class Node {
    [int]$value
    [Node]$left
    [Node]$right

    Node([int]$value){
        $this.value = $value
        $this.left = $null
        $this.right = $null
    }

    [bool] Add([int]$value){
        if ($value -lt $this.value){
            if($null -eq $this.left){
                $this.left = [Node]::new($value)
                return $true
            }
            return $this.left.Add($value)
        }
        if ($value -gt $this.value){
            if($null -eq $this.right){
                $this.right = [Node]::new($value)
                return $true
            }
            return $this.right.Add($value)
        }
        return $false
    }

    [bool] Contain([int]$value){
        if ($value -lt $this.value){
            if($null -eq $this.left){
                return $false
            }
        }
        if ($value -gt $this.value){
            if($null -eq $this.right){
                return $false
            }
        }
        return $true
    }

    [int] Length(){
        $a = 0
        $b = 0
        if ($null -ne $this.left) {
            $a = $this.left.Length()
        }
        if ($null -ne $this.right) {
            $b = $this.right.Length()
        }
        return $a + $b + 1
    }
    
    [int] Height(){
        $a = 1
        $b = 1
        if ($null -ne $this.left) {
            $a = $this.left.Height() + 1
        }
        if ($null -ne $this.right) {
            $b = $this.right.Height() + 1
        }
        if ($a -gt $b) {
            return $a
        } else {
            return $b
        }
    }
}
