
# to be used with NSIS 2.0 and up

SetCompressor lzma

!define VER_NUMBER "0.3.5a1"

# HEADER CONFIGURATION COMMANDS
Name "QuantLib"
Caption "QuantLib - Setup"
#do not change the name below
OutFile "..\QuantLib-${VER_NUMBER}-full-inst.exe"

InstType "Full (w/ Source Code)"
InstType Typical
InstType Minimal

ComponentText "This will install QuantLib ${VER_NUMBER} on your computer"

SilentInstall normal
CRCCheck on
LicenseText "You must agree with the following license before installing:"
LicenseData License.txt
;DirShow show
DirText "Please select a location to install QuantLib (or use the default):"
InstallDir $PROGRAMFILES\QuantLib
InstallDirRegKey HKEY_LOCAL_MACHINE SOFTWARE\QuantLib "Install_Dir"
AutoCloseWindow false
ShowInstDetails hide
SetDateSave on

# INSTALLATION EXECUTION COMMANDS



Section "-QuantLib"
SectionIn 1 2 3
# this directory must be created first, or the CreateShortCut will not work
    CreateDirectory "$SMPROGRAMS\QuantLib"
    SetOutPath $INSTDIR
    File "Authors.txt"
    File "Contributors.txt"
    File "History.txt"
    File "LICENSE.txt"
    File "News.txt"
    File "README.txt"
    File "TODO.txt"

    SetOutPath  $INSTDIR\ql
    File /r "ql\*.hpp"
    File /r "ql\*.h"
    File /r "ql\*.cpp"
    File /r "ql\*.c"
    File /r "ql\makefile.mak"

    WriteRegStr HKEY_LOCAL_MACHINE \
                "Software\Microsoft\Windows\CurrentVersion\Uninstall\QuantLib" \
                "DisplayName" "QuantLib (remove only)"
    WriteRegStr HKEY_LOCAL_MACHINE \
                "Software\Microsoft\Windows\CurrentVersion\Uninstall\QuantLib" \
                "UninstallString" '"QuantLibUninstall.exe"'
    WriteRegStr HKEY_LOCAL_MACHINE \
                "SOFTWARE\QuantLib" \
                "Install_Dir" "$INSTDIR"
    WriteRegStr HKEY_CURRENT_USER \
                "Environment" \
                "QL_DIR" "$INSTDIR"
    CreateShortCut "$SMPROGRAMS\QuantLib\Uninstall QuantLib.lnk" \
                   "$INSTDIR\QuantLibUninstall.exe" \
                   "" "$INSTDIR\QuantLibUninstall.exe" 0
    CreateShortCut "$SMPROGRAMS\QuantLib\README.txt.lnk" \
                   "$INSTDIR\README.txt"
    CreateShortCut "$SMPROGRAMS\QuantLib\LICENSE.txt.lnk" \
                   "$INSTDIR\LICENSE.txt"
    CreateShortCut "$SMPROGRAMS\QuantLib\What's new.lnk" \
                   "$INSTDIR\News.txt"

    CreateShortCut "$SMPROGRAMS\QuantLib\QuantLib project workspace.lnk" \
                   "$INSTDIR\QuantLib.dsw"

    WriteUninstaller "QuantLibUninstall.exe"
SectionEnd


Section "test-suite"
SectionIn 1 2 3
    SetOutPath $INSTDIR\test-suite
    File /r "test-suite\*.txt"
    File /r "test-suite\*.mak"
    File /r "test-suite\*.cpp"
    File /r "test-suite\*.hpp"
    File /r "test-suite\*.dsp"
    File /r "test-suite\CPPUNIT-COPYING"

SectionEnd

Section "Examples"
SectionIn 1 2
    SetOutPath $INSTDIR\Examples
    File /r "Examples\*.cpp"
    File /r "Examples\*.dsp"
    File /r "Examples\*.txt"
    File /r "Examples\*.mak"
    File /r "Examples\*.dsw"

    IfFileExists $SMPROGRAMS\QuantLib 0 NoSourceShortCuts
        CreateShortCut "$SMPROGRAMS\QuantLib\Examples workspace.lnk" \
                       "$INSTDIR\Examples\Examples.dsw"
    NoSourceShortCuts:
SectionEnd

Section "WinHelp documentation"
SectionIn 1 2
  SetOutPath "$INSTDIR\Docs"
  File "Docs\html\index.chm"
  CreateShortCut "$SMPROGRAMS\QuantLib\Documentation (WinHelp).lnk" \
                 "$INSTDIR\Docs\index.chm"
SectionEnd

Section "PDF documentation"
SectionIn 1
  SetOutPath "$INSTDIR\Docs"
  File "Docs\latex\refman.pdf"
  CreateShortCut "$SMPROGRAMS\QuantLib\Documentation (PDF).lnk" \
                 "$INSTDIR\Docs\refman.pdf"
SectionEnd

Section "PS documentation"
SectionIn 1
  SetOutPath "$INSTDIR\Docs"
  File "Docs\latex\refman.ps"
  CreateShortCut "$SMPROGRAMS\QuantLib\Documentation (PS).lnk" \
                 "$INSTDIR\Docs\refman.ps"
SectionEnd

Section "Start Menu Group"
SectionIn 1 2 3
  SetOutPath $SMPROGRAMS\QuantLib

#it doesn't work
#  CreateShortCut "$SMPROGRAMS\QuantLib\QuantLib Home Page.lnk" \
#                 "http://quantlib.org/index.html"
#this works
  WriteINIStr "$SMPROGRAMS\QuantLib\QuantLib Home Page.url" \
              "InternetShortcut" "URL" "http://quantlib.org/"

  CreateShortCut "$SMPROGRAMS\QuantLib\QuantLib Directory.lnk" \
                 "$INSTDIR"
SectionEnd

Function .onInit
  SetOutPath $TEMP
  File /oname=spltmp.bmp "Docs\images\QL.bmp"
  splash::show 2000 $TEMP\spltmp
  Pop $0 ; $0 has '1' if the user closed the splash screen early,
         ;        '0' if everything closed normal,
         ;        '-1' if some error occured.
  Delete $TEMP\spltmp.bmp
FunctionEnd

UninstallText "This will uninstall QuantLib. Hit next to continue."


Section "Uninstall"
    DeleteRegKey HKEY_LOCAL_MACHINE \
        "Software\Microsoft\Windows\CurrentVersion\Uninstall\QuantLib"
    DeleteRegKey HKEY_LOCAL_MACHINE SOFTWARE\QuantLib
    DeleteRegValue HKEY_CURRENT_USER  "Environment" "QL_DIR"
    Delete "$SMPROGRAMS\QuantLib\*.*"
    RMDir "$SMPROGRAMS\QuantLib"
    RMDir /r "$INSTDIR\Examples"
    RMDir /r "$INSTDIR\Docs"
    RMDir /r "$INSTDIR\ql"
    RMDir /r "$INSTDIR\lib"
    RMDir /r "$INSTDIR"
SectionEnd
