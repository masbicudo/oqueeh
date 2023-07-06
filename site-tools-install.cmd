@if (@X)==(@Y) @end /* ---------------- Batch code ----------------

@Echo Off

::
:: Main
::
GoTo :Main_End
:Main

    SET G=[92m
    SET N=[0m
    Set "EchoElev=Echo.%G%"

    Call :Elevate %* || (
        Echo.%N%
        Exit /B
    )
    Echo.%N%


    :: WINGET or CHOCO
    where winget || (
        where choco && (
            choco upgrade -y chocolatey
        ) || (
            powershell "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        )
    )


    :: RUBY
    where ruby && (
        (
            where choco && choco upgrade -y ruby
        ) || (
            where winget && winget upgrade -h RubyInstallerTeam.Ruby
        )
    ) || (
        (
            where choco && choco install -y ruby
        ) || (
            where winget && winget install -h RubyInstallerTeam.Ruby
        )
    )


    :: GEM
    where gem && (
        gem update bundler
    ) || (
        gem install bundler
    )

Exit /B
:Main_End

::
:: Elevate
::
GoTo :Elevate_End
:Elevate

    ::::::::::::::::::::::::::::::::::::::::::::
    :: Automatically check & get admin rights V2
    ::::::::::::::::::::::::::::::::::::::::::::
    %EchoElev%=============================
    %EchoElev%Running Admin shell
    %EchoElev%%~dpnx0 %*
    %EchoElev%=============================

    :init
    SetLocal DisableDelayedExpansion
    Set "batchPath=%~dpnx0"
    For %%K In (%batchPath%) Do Set batchName=%%~nK
    Set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
    Set "cmdGetPrivileges=%temp%\OEgetPriv_%batchName%.cmd"
    SetLocal EnableDelayedExpansion
    
    %EchoElev%vbsGetPrivileges=%vbsGetPrivileges%
    %EchoElev%cmdGetPrivileges=%cmdGetPrivileges%
    %EchoElev%batchPath=%batchPath%
    %EchoElev%ELEV_%batchName%=!ELEV_%batchName%!
    %EchoElev%=============================

    :checkPrivileges
    NET FILE 1>Nul 2>Nul
    If '%errorlevel%' == '0' (
      GoTo gotPrivileges
    ) Else (
      GoTo getPrivileges
    )

    :getPrivileges
    %EchoElev%:getPrivileges
    If "!ELEV_%batchName%!" == "1" (
        GoTo gotPrivileges
    )
    %EchoElev%
    %EchoElev%**************************************
    %EchoElev%Invoking UAC for Privilege Escalation
    %EchoElev%**************************************

    (
        Echo Set UAC = CreateObject^("Shell.Application"^)
        Echo UAC.ShellExecute "!cmdGetPrivileges!", "", "", "runas", 1
    ) > "%vbsGetPrivileges%"
    
    (
        Echo @Echo Off
        Echo Set "ELEV_%batchName%=1"
        Echo Call "%batchPath%" %*
    ) > "%cmdGetPrivileges%"

    "%SystemRoot%\System32\WScript.exe" "%vbsGetPrivileges%" %*
    Exit /B 1

    :gotPrivileges
    %EchoElev%:gotPrivileges
    SetLocal & PushD .
    CD /d %~dp0
    If "!ELEV_%batchName%!" == "1" (
        Del "%vbsGetPrivileges%" 1>Nul 2>Nul
        Del "%cmdGetPrivileges%" 1>Nul 2>Nul
    )
    Exit /B 0

Exit /B
:Elevate_End


:: Call main function
Call :Main %*

REM ---------------- JScript Code ----------------*/
