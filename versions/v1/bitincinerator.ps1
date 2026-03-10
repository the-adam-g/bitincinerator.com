
param(
    [string]$path,
    [Int]$passes
)
Write-Host @"
    ____  _ __     ____           _                       __                                    
   / __ )(_) /_   /  _/___  _____(_)___  ___  _________ _/ /_____  _____    _________  ____ ___ 
  / __  / / __/   / // __ \/ ___/ / __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/   / ___/ __ \/ __ `__ \
 / /_/ / / /_   _/ // / / / /__/ / / / /  __/ /  / /_/ / /_/ /_/ / /     _/ /__/ /_/ / / / / / /
/_____/_/\__/  /___/_/ /_/\___/_/_/ /_/\___/_/   \__,_/\__/\____/_/     (_)___/\____/_/ /_/ /_/ 
                                                                                                    
"@
if (-not $path) {
    $path = Read-Host -Prompt "Enter the path of your file"
}
$path = $path.Replace('"', '')
$contentslength = (Get-Item $path).Length
if (-not $passes) {
    Write-Host $contentslength " bytes changed"
    $bytes = New-Object byte[] $contentslength
    [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
    [System.IO.File]::WriteAllBytes($path, $bytes)
    Write-Host "File sucessfully incinerated"
} else {
    for ($i = 1; $i -le $passes; $i++) {
        $bytes = New-Object byte[] $contentslength
        [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
        [System.IO.File]::WriteAllBytes($path, $bytes)
    }
    Write-Host "File sucessfully incinerated. " $passes "passes performed"
    Write-Host "Thank you for using BitIncinerator"
}