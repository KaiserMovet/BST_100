Using module "./Node.psm1"

class Tree{
    [Node]$root

    Tree(){
        $this.root = $null
    }

    [bool] Add([int]$value){
        if($null -eq $this.root){
            $this.root = [Node]::new($value)
            return $true
        }
        return $this.root.Add($value)
    }

    [bool] Contain([int]$value){
        if($null -eq $this.root){
            return $false
        }
        return $this.root.Contain($value)
    }

    [int] Length(){
        if($null -eq $this.root){
            return 0
        }
        return $this.root.Length()
    }

    [int] Height(){
        if($null -eq $this.root){
            return 0
        }
        return $this.root.Height()
    }
}
