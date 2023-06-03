Using module "./Tree.psm1"

param (
    [Parameter(Mandatory=$true)]
    [int]$amount
)

function Get-Numbers {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Path,
        [Parameter(Mandatory=$true)]
        [int]$Amount
    )

    $reader = New-Object System.IO.StreamReader($Path)
    $counter = 0
    $numbers = New-Object System.Collections.ArrayList

    while ($null -ne ($line = $reader.ReadLine()) -and $counter -lt $Amount) {
        $numbers.Add([int]$line) | Out-Null
        $counter++
    }

    $reader.Close()
    return $numbers
}


$addNumbersPath = "/datasets/add.txt"
$checkNumbersPath = "/datasets/check.txt"

$addNumbers = Get-Numbers -Path $addNumbersPath -Amount $amount
$checkNumbers = Get-Numbers -Path $checkNumbersPath -Amount $amount

$tree = [Tree]::new()

# Add elements
$startTime = Get-Date
foreach ($i in $addNumbers) {
    $tree.Add($i) | Out-Null
}
$endTime = Get-Date
Write-Host ("ADD_TEST:{0}" -f ($endTime - $startTime).TotalSeconds)

# Check elements
$startTime = Get-Date
foreach ($i in $checkNumbers) {
    $tree.Contain($i) | Out-Null
}
$endTime = Get-Date
Write-Host ("CHECK_TEST:{0}" -f ($endTime - $startTime).TotalSeconds)

# Length elements
$startTime = Get-Date
for ($i = 0; $i -lt 10; $i++) {
    $tree.Length() | Out-Null
}
$endTime = Get-Date
Write-Host ("LEN_TEST:{0}" -f (($endTime - $startTime).TotalSeconds / 10))

# Height elements
$startTime = Get-Date
for ($i = 0; $i -lt 10; $i++) {
    $tree.Height() | Out-Null
}
$endTime = Get-Date
Write-Host ("HEIGHT_TEST:{0}" -f (($endTime - $startTime).TotalSeconds / 10))

Write-Host ("VALIDATION:{0}:{1}" -f $tree.Length(), $tree.Height())
