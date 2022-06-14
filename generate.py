import argparse
from itertools import product
import os
import yaml
from packaging import version
import subprocess
import re

QT_5_9_0 = "qt5.9.0"
QT_5_9_1 = "qt5.9.1"
QT_5_9_2 = "qt5.9.2"
QT_5_9_3 = "qt5.9.3"
QT_5_9_4 = "qt5.9.4"
QT_5_9_5 = "qt5.9.5"
QT_5_9_6 = "qt5.9.6"
QT_5_9_7 = "qt5.9.7"
QT_5_9_8 = "qt5.9.8"
QT_5_9_9 = "qt5.9.9"
QT_5_10_0 = "qt5.10.0"
QT_5_10_1 = "qt5.10.1"
QT_5_11_0 = "qt5.11.0"
QT_5_11_1 = "qt5.11.1"
QT_5_11_2 = "qt5.11.2"
QT_5_11_3 = "qt5.11.3"
QT_5_12_0 = "qt5.12.0"
QT_5_12_1 = "qt5.12.1"
QT_5_12_2 = "qt5.12.2"
QT_5_12_3 = "qt5.12.3"
QT_5_12_4 = "qt5.12.4"
QT_5_12_5 = "qt5.12.5"
QT_5_12_6 = "qt5.12.6"
QT_5_12_7 = "qt5.12.7"
QT_5_12_8 = "qt5.12.8"
QT_5_12_9 = "qt5.12.9"
QT_5_12_10 = "qt5.12.10"
QT_5_12_11 = "qt5.12.11"
QT_5_12_12 = "qt5.12.12"
QT_5_13_0 = "qt5.13.0"
QT_5_13_1 = "qt5.13.1"
QT_5_13_2 = "qt5.13.2"
QT_5_14_0 = "qt5.14.0"
QT_5_14_1 = "qt5.14.1"
QT_5_14_2 = "qt5.14.2"
QT_5_15_0 = "qt5.15.0"
QT_5_15_1 = "qt5.15.1"
QT_5_15_2 = "qt5.15.2"
QT_6_0_0 = "qt6.0.0"
QT_6_0_1 = "qt6.0.1"
QT_6_0_2 = "qt6.0.2"
QT_6_0_3 = "qt6.0.3"
QT_6_0_4 = "qt6.0.4"
QT_6_1_0 = "qt6.1.0"
QT_6_1_1 = "qt6.1.1"
QT_6_1_2 = "qt6.1.2"
QT_6_1_3 = "qt6.1.3"
QT_6_2_0 = "qt6.2.0"
QT_6_2_1 = "qt6.2.1"
QT_6_2_2 = "qt6.2.2"
QT_6_2_3 = "qt6.2.3"
QT_6_2_4 = "qt6.2.4"
QT_6_3_0 = "qt6.3.0"
QTS = [QT_5_9_0, QT_5_9_1, QT_5_9_2, QT_5_9_3, QT_5_9_4, QT_5_9_5, QT_5_9_6, QT_5_9_7, QT_5_9_8, QT_5_9_9, QT_5_10_0, QT_5_10_1, QT_5_11_0, QT_5_11_1, QT_5_11_2, QT_5_11_3, QT_5_12_0, QT_5_12_1, QT_5_12_2, QT_5_12_3, QT_5_12_4, QT_5_12_5, QT_5_12_6, QT_5_12_7, QT_5_12_8, QT_5_12_9, QT_5_12_10, QT_5_12_11, QT_5_12_12, QT_5_13_0, QT_5_13_1, QT_5_13_2, QT_5_14_0, QT_5_14_1, QT_5_14_2, QT_5_15_0, QT_5_15_1, QT_5_15_2, QT_6_0_0, QT_6_0_1, QT_6_0_2, QT_6_0_3, QT_6_0_4, QT_6_1_0, QT_6_1_1, QT_6_1_2, QT_6_1_3, QT_6_2_0, QT_6_2_1, QT_6_2_2, QT_6_2_3, QT_6_2_4, QT_6_3_0]

#DEFAULT_QTS = [QT_6_3_0, QT_5_15_2]

MINGW = 'mingw'

MSVC = 'msvc'

MSVC_2017 = 'msvc2017'
MSVC_2019 = 'msvc2019'
MSVC_2022 = 'msvc2022'

ARCH_32 = "i686"
ARCH_64 = "x86_64"

#DEFAULT_COMPILERS = [MINGW, MSVC_2019]

"""
COMPILER_PREFIXES = {
    QT_5_15_2: {MINGW: 'mingw81_64', MSVC_2019: 'msvc2019_64'},
    QT_6_3_0: {MINGW: 'mingw1120_64', MSVC_2019: 'msvc2019_64'}
}
"""

"""
COMPILER_PREFIXES_ = {
    QT_5_15_2: {MINGW64: 'mingw8.1.0_64', MSVC2019: 'msvc2019_64'},
    QT_6_3_0: {MINGW64: 'mingw11.2.0_64', MSVC2019: 'msvc2019_64'}
}
"""

MINGW_11_2_0 = "mingw11.2.0"
MINGW_8_1_0 = "mingw8.1.0"
MINGW_7_3_0 = "mingw7.3.0"
MINGW_5_3_0 = "mingw5.3.0"
MINGW_4_9_2 = "mingw4.9.2"

MINGW_4_9_1 = "mingw4.9.1"
MINGW_4_8_2 = "mingw4.8.2"
MINGW_4_8_0 = "mingw4.8.0"
MINGW_4_7_2 = "mingw4.7.2"

MYSQL_WIN32_URL = "https://cdn.mysql.com//Downloads/MySQL-5.5/mysql-5.5.62-win32.zip"
MYSQL_WIN64_URL = "https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.29-winx64.zip"

def to_version(s):
    prefixes = ["qt", "mingw", "msvc"]
    for prefix in prefixes:
        if s.startswith(prefix):
            return version.parse(s[len(prefix):])

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# https://wiki.qt.io/MinGW
def qt_mingw_compiler(qt, arch):
    v = to_version(qt)

    if arch == ARCH_32:
        if v >= to_version(QT_6_2_0):
            return None

    if v >= to_version(QT_6_2_2):
        return MINGW_11_2_0
    elif v >= to_version(QT_5_15_0):
        return MINGW_8_1_0
    elif v >= to_version(QT_5_12_0):
        return MINGW_7_3_0
    elif v >= to_version(QT_5_9_0):
        return MINGW_5_3_0
    """
    elif v >= to_version(QT_5_7_0):
        return MINGW_5_3_0
    """

# query result
def qt_msvc_compiler(qt):
    v = to_version(qt)
    if v >= to_version(QT_5_15_0):
        return MSVC_2019

def is_msvc_optimal(qt, compiler, arch):
    v = to_version(qt)
    if compiler == MSVC_2019:
        if arch == ARCH_32:
            return v >= to_version(QT_5_15_0) and v < to_version(QT_6_0_0)
        return v >= to_version(QT_5_15_0)
    return False

def qtbase_src_url(qt):
    v = to_version(qt)
    maj, min, fix = v.major, v.minor, v.micro
    official = [(5,12),(5,15),(6,0),(6,1),(6,2),(6,3)]
    if (maj, min) in official:
        # https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtbase-everywhere-src-5.15.2.zip
        return "https://download.qt.io/official_releases/qt/{}.{}/{}.{}.{}/submodules/qtbase-everywhere-src-{}.{}.{}.zip".format(maj, min, maj, min, fix, maj, min, fix)
    else:
        # https://download.qt.io/archive/qt/5.13/5.13.2/submodules/qtbase-everywhere-src-5.13.2.zip
        return "https://download.qt.io/archive/qt/{}.{}/{}.{}.{}/submodules/qtbase-everywhere-src-{}.{}.{}.zip".format(maj, min, maj, min, fix, maj, min, fix)

# https://wiki.qt.io/MinGW
def mingw_compiler_url(compiler, arch):
    
    if arch == ARCH_64:
        return {
            MINGW_11_2_0: "https://github.com/cristianadam/mingw-builds/releases/download/v11.2.0-rev1/x86_64-11.2.0-release-posix-seh-rt_v9-rev1.7z",
            MINGW_8_1_0: "https://versaweb.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z",
            MINGW_7_3_0: "https://cfhcable.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/7.3.0/threads-posix/seh/x86_64-7.3.0-release-posix-seh-rt_v5-rev0.7z"
        }[compiler]
    else:
        return {
            MINGW_7_3_0: "https://kumisystems.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/7.3.0/threads-posix/dwarf/i686-7.3.0-release-posix-dwarf-rt_v5-rev0.7z",
            MINGW_8_1_0: "https://cytranet.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/8.1.0/threads-posix/dwarf/i686-8.1.0-release-posix-dwarf-rt_v6-rev0.7z",
            MINGW_5_3_0: "https://versaweb.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/5.3.0/threads-posix/dwarf/i686-5.3.0-release-posix-dwarf-rt_v4-rev0.7z",
            MINGW_4_9_2: "https://cfhcable.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.9.2/threads-posix/dwarf/i686-4.9.2-release-posix-dwarf-rt_v3-rev1.7z",
            MINGW_4_9_1: "https://master.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.9.1/threads-posix/dwarf/i686-4.9.1-release-posix-dwarf-rt_v3-rev2.7z?viasf=1",
            MINGW_4_8_2: "https://cytranet.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.8.2/threads-posix/dwarf/i686-4.8.2-release-posix-dwarf-rt_v3-rev3.7z",
            MINGW_4_8_0: "https://master.dl.sourceforge.net/project/mingwbuilds/host-windows/releases/4.8.0/32-bit/threads-posix/dwarf/x32-4.8.0-release-posix-dwarf-rev2.7z?viasf=1",
            MINGW_4_7_2: "https://master.dl.sourceforge.net/project/mingwbuilds/host-windows/releases/4.7.2/32-bit/threads-posix/sjlj/x32-4.7.2-release-posix-sjlj-rev8.7z?viasf=1"
        }[compiler]

def arch_suffix(arch):
    return {
        ARCH_32: '',
        ARCH_64: '_64',
    }[arch]

def compiler_prefix(compiler, arch, dot = False):
    if dot:
        return compiler + "-" + arch
    if is_msvc(compiler):
        return compiler + arch_suffix(arch)
    v = to_version(compiler)
    return 'mingw' + str(v.major) + str(v.minor) + arch_suffix(arch)

class folded_str(str): pass
class literal_str(str): pass
def folded_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='>')
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
yaml.add_representer(folded_str, folded_str_representer)
yaml.add_representer(literal_str, literal_str_representer)

def pack(cmds, name, local):
    if local:
        return "rem {}\n".format(name) + "\n".join(cmds) + "\n"
    else:
        return {
            "name": name, 
            "shell": "cmd", 
            "run": literal_str("\n".join(cmds) + "\n")
        }

def testenv_step(local):
    cmds = []
    cmds.append('where cmake || exit /b 0')
    cmds.append('where perl || exit /b 0')
    cmds.append('where curl || exit /b 0')
    cmds.append('where 7z || exit /b 0')
    #cmds.append('where ninja')
    return pack(cmds, "test env", local)

def install_ninja_step(local):
    cmds = []
    if local:
        python_path = ["C:\\Miniconda3","C:\\Miniconda3\\Scripts"]
    else:
        python_path = ["C:\\Miniconda","C:\\Miniconda\\Scripts"]
    cmds.append(set_path(python_path))
    cmds.append("pip install aqtinstall")
    cmds.append("aqt install-tool windows desktop tools_ninja qt.tools.ninja")
    return pack(cmds, "install ninja", local)

def upload_step(qt, compiler, arch):
    return {
        "uses": "actions/upload-artifact@v3",
        "with": {
            "name": flavour_dir_name(qt, compiler, arch),
            "path": flavour_dir_name(qt, compiler, arch),
        }
    }


"""
def release_step(qt, compiler):
    return {
        "uses": "ncipollo/release-action@v1",
        "if": "startsWith( github.ref, 'refs/tags/')",
        "with": {
            "artifacts": flavour_dir_name(qt, compiler) + ".zip",
            "token": "${{ secrets.GITHUB_TOKEN }}"
        }
    }
"""

class ReleaseStep:
    def __init__(self):
        self._artifacts = []
        self._artifacts2 = set()
    def add(self, qt, compiler, arch):
        self._artifacts.append(flavour_dir_name(qt, compiler, arch) + ".zip")

    def add_once(self, path):
        self._artifacts2.add(path)

    def github(self):
        return {
            "uses": "ncipollo/release-action@v1",
            "if": "startsWith( github.ref, 'refs/tags/')",
            "with": {
                "artifacts": literal_str("\n".join(self._artifacts + list(self._artifacts2)) + "\n"),
                "token": "${{ secrets.GITHUB_TOKEN }}"
            }
        }

def unix_path(path):
    return path.replace("\\","/")

class MySql:
    def __init__(self, path):
        # "C:/mysql/include"
        self.include = unix_path(os.path.join(path, "include"))
        # C:/mysql/lib
        self.lib = unix_path(os.path.join(path, "lib"))
        # C:/mysql/lib/libmysql.lib
        self.libmysql_lib = unix_path(os.path.join(path, "lib", "libmysql.lib"))
        self.libmysql_dll = unix_path(os.path.join(path, "lib", "libmysql.dll"))
        # C:/mysql/bin
        self.bin = unix_path(os.path.join(path, "bin"))

def download(url, name = None):
    if name is None:
        name = os.path.basename(url)
    return 'if not exist "{}" curl -L -o {} "{}"'.format(name, name, url.replace("%", "%%"))

def set_path(*args):
    paths = []
    for arg in args:
        if isinstance(arg, str):
            paths.append(arg)
        elif arg is None:
            pass
        elif isinstance(arg, list):
            for arg_ in arg:
                paths.append(arg_)
        else:
            raise ValueError('not list none or string', arg)
    paths.append('%PATH%')
    return "set PATH={}".format(";".join(paths))

def mkdir(path):
    return "if not exist \"{}\" mkdir \"{}\"".format(path,path)

def copy_file(src, dst):
    return "copy /y \"{}\" \"{}\"".format(src.replace("/","\\"), dst.replace("/","\\"))

def rmdir(path):
    return 'if exist {} rmdir /q /s {}'.format(path, path)

def extract(path, test = None):
    if test:
        return 'if not exist \"{}\" 7z x -y \"{}\"'.format(test, path)
    return '7z x -y \"{}\"'.format(path)

def archive(dst, src):
    return "7z a \"{}\" \"{}\"".format(dst, src)

def is_mingw(compiler):
    if compiler is None:
        return False
    return compiler.startswith("mingw")

def is_msvc(compiler):
    if compiler is None:
        return False
    return compiler.startswith("msvc")

def flavour_dir_name(qt, compiler, arch):
    return "{}-{}-{}".format("qsqlmysql", qt, compiler_prefix(compiler, arch, dot = True))

def mingw_bin_path(compiler, arch):
    if is_mingw(compiler):
        if arch == ARCH_64:
            return "%CD%\\mingw64\\bin"
        else:
            return "%CD%\\mingw32\\bin"

COMMUNITY = "Community"
ENTERPRISE = "Enterprise"

def vcvars_path(compiler, edition, arch):
    """
    compilers = {
        MSVC_2019: {
            ENTERPRISE: "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Enterprise\\VC\\Auxiliary\\Build\\vcvars64.bat",
            COMMUNITY: "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Auxiliary\\Build\\vcvars64.bat"
        },
        MSVC_2022: {
            COMMUNITY: "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Auxiliary\\Build\\vcvars64.bat",
            ENTERPRISE: "C:\\Program Files\\Microsoft Visual Studio\\2022\\Enterprise\\VC\\Auxiliary\\Build\\vcvars64.bat"
        }
    }
    """
    if compiler == MSVC_2019:
        return "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\{}\\VC\\Auxiliary\\Build\\vcvars{}.bat".format(edition, "32" if arch == ARCH_32 else "64")
    elif compiler == MSVC_2022:
        return "C:\\Program Files\\Microsoft Visual Studio\\2022\\{}\\VC\\Auxiliary\\Build\\vcvars{}.bat".format(edition, "32" if arch == ARCH_32 else "64")

def mysql_url(arch):
    return {
        ARCH_64: MYSQL_WIN64_URL,
        ARCH_32: MYSQL_WIN32_URL
    }[arch]
    
def build_step(qt, compiler, arch, local):
    cmds = []


    # clear env
    cmds.append("if exist clear-env.bat call clear-env.bat")

    # download mysql
    url = mysql_url(arch)    
    cmds.append(download(url))
    name = os.path.basename(url)
    name_ = os.path.splitext(name)[0]
    cmds.append(extract(name, name_))

    mysql_ = MySql(os.path.join("%CD%","..",name_))
    mysql = MySql(os.path.join("%CD%",name_))

    # download qt sources
    url = qtbase_src_url(qt)
    name = os.path.basename(url)
    qt_dir_name = os.path.splitext(name)[0]
    cmds.append(download(url))
    cmds.append(rmdir(qt_dir_name))
    cmds.append(extract(name))
    
    ninja_path = "%CD%\\Tools\\Ninja"
    
    # download compiler
    if is_mingw(compiler):
        url = mingw_compiler_url(compiler, arch)
        name = os.path.basename(url)
        cmds.append(download(url))
        if arch == ARCH_64:
            cmds.append(rmdir("mingw64"))
        else:
            cmds.append(rmdir("mingw32"))
        cmds.append(extract(name))
    else:
        vcvars = vcvars_path(compiler, COMMUNITY if local else ENTERPRISE, arch)
        cmds.append("set INCLUDE=")
        cmds.append("call \"{}\"".format(vcvars))

    cmds.append(set_path(mysql.lib, mysql.bin, mingw_bin_path(compiler, arch), ninja_path))

    dst_name = flavour_dir_name(qt, compiler, arch)
    cmds.append(mkdir(dst_name))

    # build
    cmds.append("pushd {}".format(qt_dir_name))

    prefix = os.path.join("C:\\", "Qt", qt.replace("qt",""), compiler_prefix(compiler, arch, dot = False))
    if is_mingw(compiler):
        platform = 'win32-g++'
    else:
        platform = 'win32-msvc'
    #mode = '-release'
    
    # https://doc.qt.io/qt-6/configure-options.html

    if to_version(qt) >= to_version(QT_6_0_0):

        def no_feature(feature):
            return "-DINPUT_{}=no".format(feature)

        mode = "Release;Debug"
        if is_mingw(compiler):
            cc = "gcc"
            ccx = "g++"
        else:
            cc = "cl"
            ccx = "cl"
        flags = " ".join(["-DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=" + prefix, 
            "-DQT_QMAKE_TARGET_MKSPEC=" + platform, 
            "-DCMAKE_C_COMPILER=" + cc, 
            "-DCMAKE_CXX_COMPILER=" + ccx,
            "-DQT_BUILD_TESTS=FALSE -DQT_BUILD_EXAMPLES=FALSE -DCMAKE_CONFIGURATION_TYPES=" + mode, 
            "-DQT_EXTRA_DEFINES=MySQL_INCLUDE_DIR=" + mysql_.include + ";MySQL_LIBRARY=" + mysql_.libmysql_lib, 
            "-DINPUT_opengl=desktop -G \"Ninja Multi-Config\"", 
            #no_feature("gui"),
            #no_feature("widgets"),
            #no_feature("network"),
            #no_feature("dbus"),
            #no_feature("test"),
            #no_feature("xml"),
            #no_feature("concurrent"),
            #no_feature("sql_sqlite"),
            #no_feature("sql_odbc"),
            "."])
        cmds.append("cmake " + flags)
        #cmds.append('cmake --build .')
        cmds.append("ninja qsqlmysql.dll")
        
    else:
        def no_feature(feature):
            return "-no-feature-{}".format(feature)

        mode = '-debug-and-release'
        nomake_flags = "-nomake tests -nomake examples"
        flags = " ".join(["-prefix", prefix, 
            "-opensource -confirm-license -shared -platform", platform, "-opengl desktop", mode, nomake_flags, 
            no_feature("gui"),
            no_feature("widgets"),
            no_feature("network"),
            #"-no-dbus",
            "MYSQL_INCDIR=" + mysql_.include, " MYSQL_LIBDIR=" + mysql_.lib])
        cmds.append("call configure " + flags)
        if is_mingw(compiler):
            cmds.append('mingw32-make')
        else:
            cmds.append('nmake')
    
    cmds.append(copy_file("plugins\\sqldrivers\\qsqlmysql.dll", "..\{}".format(dst_name)))
    cmds.append(copy_file("plugins\\sqldrivers\\qsqlmysqld.dll", "..\{}".format(dst_name)))

    cmds.append("popd")

    url = mysql_url(arch)
    mysql = MySql(os.path.splitext(os.path.basename(url))[0])
    dst = "libmysql-{}".format(arch)
    cmds.append(mkdir(dst))
    cmds.append(copy_file(mysql.libmysql_dll, dst))
    cmds.append(copy_file(mysql.libmysql_lib, dst))
    cmds.append(archive(dst + ".zip", dst))

    name = flavour_dir_name(qt, compiler, arch)
    #cmds.append("7z a {}.zip {}".format(name, name))
    cmds.append(archive(name + ".zip", name))
    return pack(cmds, "flavour {} {} {}".format(qt, compiler, arch), local)


def is_qt6_or_greater(qt):
    return int(qt.split('.')[0]) > 5

class Dumper(yaml.Dumper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # disable resolving on as tag:yaml.org,2002:bool (disable single quoting)
        cls = self.__class__
        cls.yaml_implicit_resolvers['o'] = []

def query():
    output = subprocess.check_output('aqt list-qt windows desktop').decode('utf-8')
    #print(output)
    versions = re.split('[ \r\n]+', output)
    
    with open("tmp1.txt","w",encoding="utf-8") as f:
        qts = []
        for v in versions:
            if v == '':
                continue
            maj, min, fix = v.split(".")
            qt = "QT_{}_{}_{}".format(maj, min, fix)
            qts.append(qt)
            f.write('{} = "qt{}"\n'.format(qt, v))
        f.write("QTS = [{}]".format(", ".join(qts)))

    #return        
    #versions = versions[-5:]

    with open("tmp2.txt", "w", encoding="utf-8") as f:
        for v in versions:
            if v == '':
                continue
            output = subprocess.check_output('aqt list-qt windows desktop --arch {}'.format(v)).decode('utf-8')
            f.write(v + "\n")
            f.write(output)

import textwrap

def main():
    #query(); return

    parser = argparse.ArgumentParser(prog="generate.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog="""specify triples of QT_VERSION, COMPILER, ARCH you want to build 
or use --qt --arch --compiler to build all combinations

examples:
  python generate.py 5.15.2 mingw 64 6.3.0 msvc 64
  python generate.py --qt 6.3.0
  python generate.py --qt 5.15.2 --compiler msvc
  python generate.py --qt 5.15.2 --arch 64
  python generate.py --set1
  python generate.py --recent-qt 3
      """)
    parser.add_argument('--set1', action='store_true', help="build {} and {}".format(QT_6_3_0, QT_5_15_2))
    parser.add_argument('--set2', action='store_true', help="build all qt versions")
    parser.add_argument('--qt', nargs='+', help="qt versions to build")
    parser.add_argument('--arch', nargs='+', help="architectures to build (32 or 64 or both)")
    parser.add_argument('--compiler', nargs='+', help="compiler(s) to use (msvc, mingw)")
    parser.add_argument('--recent-qt', type=int, help="build N recent qt versions")
    parser.add_argument('args', nargs='*')
    
    args = parser.parse_args()

    #print(args); exit(0)
    
    steps_local = []
    steps_github = []

    steps_local.append(testenv_step(True))
    steps_github.append(testenv_step(False))
    steps_local.append(install_ninja_step(local=True))
    steps_github.append(install_ninja_step(local=False))

    release_step = ReleaseStep()
    
    def to_qt(qt):
        if not qt.startswith("qt"):
            return "qt" + qt
        return qt

    def to_compiler(qt, compiler, arch):
        if compiler == MSVC:
            return MSVC_2019
        if compiler == MINGW:
            return qt_mingw_compiler(qt, arch)
        return compiler

    def to_arch(arch):
        return {
            "32": ARCH_32,
            "64": ARCH_64,
            ARCH_32: ARCH_32,
            ARCH_64: ARCH_64
        }[arch]

    flavours = []

    def filter_optimal(flavours):
        res = []
        for qt, compiler, arch in flavours:
            qt = to_qt(qt)
            arch = to_arch(arch)
            compiler = to_compiler(qt, compiler, arch)
            if compiler == MSVC_2019:
                if is_msvc_optimal(qt, compiler, arch):
                    res.append((qt, compiler, arch))
            elif is_mingw(compiler):
                try:
                    url = mingw_compiler_url(compiler, arch)
                    res.append((qt, compiler, arch))
                except:
                    print("dont know download url for {} {}".format(compiler, arch))
            else:
                print("filtered out", qt, compiler, arch)
        return res

    for qt, compiler, arch in chunks(args.args, 3):
        qt = to_qt(qt)
        arch = to_arch(arch)
        compiler_ = compiler
        compiler = to_compiler(qt, compiler, arch)
        if compiler is None:
            if compiler_ == MINGW:
                print("failed to guess mingw version for {} {} {}, please specify mingw version".format(qt, compiler_, arch))
            else:
                print("unexpected compiler {} {} {}".format(qt, compiler_, arch))
            continue
        flavours.append((qt, compiler, arch))

    if args.arch is None:
        arg_arch = [ARCH_32, ARCH_64]
    else:
        arg_arch = args.arch

    if args.compiler is None:
        arg_compiler = [MSVC, MINGW]
    else:
        arg_compiler = args.compiler

    if args.set1:
        flavours = filter_optimal(product([QT_6_3_0, QT_5_15_2], arg_compiler, arg_arch))
    
    if args.set2:
        flavours = filter_optimal(product(QTS, arg_compiler, arg_arch))
    
    if args.qt is not None:
        flavours = filter_optimal(product(args.qt, arg_compiler, arg_arch))

    if args.recent_qt is not None:
        qts = QTS[-args.recent_qt:]
        print(qts)
        flavours = filter_optimal(product(qts, arg_compiler, arg_arch))

    if len(args.args) == 0 and args.recent_qt is None and args.qt is None:
        flavours = filter_optimal(product([QT_6_3_0, QT_5_15_2], arg_compiler, arg_arch))

    for qt, compiler, arch in flavours:
        #qt = to_qt(qt)
        #arch = to_arch(arch)
        #compiler = to_compiler(qt, compiler, arch)
        print(qt, compiler, arch)
        steps_local.append(build_step(qt, compiler, arch, local=True))
        steps_github.append(build_step(qt, compiler, arch, local=False))
        steps_github.append(upload_step(qt, compiler, arch))
        release_step.add(qt, compiler, arch)
        release_step.add_once("libmysql-{}.zip".format(arch))

    steps_github.append(release_step.github())

    wrokflow_path = os.path.join(os.path.dirname(__file__), ".github", "workflows", "main.yml")

    batch_path = os.path.join(os.path.dirname(__file__), "main.bat")

    os.makedirs(os.path.dirname(wrokflow_path), exist_ok=True)

    data = {"name":"main","on":"push","jobs":{"main": {"runs-on":"windows-2019","steps":steps_github}}}
    with open(wrokflow_path, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(data, None, Dumper=Dumper, sort_keys=False))
    with open(batch_path, 'w', encoding='utf-8') as f:
        f.write("@echo off\n" + "\n".join(steps_local) + "\n")

if __name__ == "__main__":
    main()