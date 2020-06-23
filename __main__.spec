# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ('src\\assets\\sprites\\*.png','src\\assets\\sprites'),
    ('src\\assets\\audio\\*.wav','src\\assets\\audio')
]

a = Analysis(['__main__.py'],
             pathex=['C:\\Users\\fagun\\Documents\\projetos\\flap-bird'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='__main__',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='flappy.ico')
