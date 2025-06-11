:: surpress variable
@echo off

set folder_path=..\fonts\TTF
::make folder
if not exist %folder_path% (
    mkdir %folder_path%
    echo Folder created at %folder_path%
)

echo === Modifying MONO average width... ===
py fix_mono.py %folder_path%
echo === END ===
echo