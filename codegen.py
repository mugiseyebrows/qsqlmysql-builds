import json
import textwrap

with open("aqt.json", encoding='utf-8') as f:
    data = json.load(f)

qts = []

wrap_width = 120

MINGW_11_2_0 = "mingw11.2.0"
MINGW_8_1_0 = "mingw8.1.0"
MINGW_7_3_0 = "mingw7.3.0"
MINGW_5_3_0 = "mingw5.3.0"
MINGW_4_9_2 = "mingw4.9.2"

MINGW_4_9_1 = "mingw4.9.1"
MINGW_4_8_2 = "mingw4.8.2"
MINGW_4_8_0 = "mingw4.8.0"
MINGW_4_7_2 = "mingw4.7.2"

def to_qt_list(qts):
    return "[" + ", ".join([qt_to_const(qt) for qt in qts]) + "]"

def qt_to_const(qt):
    return "QT_" + "_".join(qt.replace("qt","").split("."))

mm = dict()
kv = list(globals().items())
for k,v in kv:
    if k.startswith('MINGW_'):
        mm[v] = k

def mingw_to_const(v):
    return mm[v]

def to_mingw_dict(d):
    res = []
    for qt, mingw in d.items():
        res.append('{}: {}'.format(qt_to_const(qt), mingw_to_const(mingw)))
    return "{" + ", ".join(res) + "}"

with open("tmp.txt", 'w') as f:
    for v in data['versions']:
        maj, min, fix = v.split(".")
        qt = "QT_{}_{}_{}".format(maj, min, fix)
        qts.append(qt)
        f.write('{} = "qt{}"\n'.format(qt, v))

    qts_ = "\n".join(textwrap.wrap("QTS = [{}]\n".format(", ".join(qts)), width=wrap_width, replace_whitespace=False, drop_whitespace=False))

    f.write(qts_)
    m = {
        "mingw81": MINGW_8_1_0,
        "mingw73": MINGW_7_3_0,
        "mingw53": MINGW_5_3_0,
        "mingw": MINGW_11_2_0,
    }

    mingw32 = dict()
    mingw64 = dict()

    msvc2019_32 = []
    msvc2019_64 = []

    for v in data['versions']:
        for c in data['arch'][v]:
            if 'msvc' in c:
                if c == 'win64_msvc2019_64':
                    msvc2019_64.append(v)
                elif c == 'win32_msvc2019':
                    msvc2019_32.append(v)
            elif 'mingw' in c:
                a, cv = c.split('_')
                if a == 'win32':
                    mingw32[v] = m[cv]
                else:
                    mingw64[v] = m[cv]

    msvc2019_32_ = "\n".join(textwrap.wrap("QT_TO_MSVC2019_32 = " + to_qt_list(msvc2019_32), width=wrap_width, replace_whitespace=False, drop_whitespace=False))
    msvc2019_64_ = "\n".join(textwrap.wrap("QT_TO_MSVC2019_64 = " + to_qt_list(msvc2019_64), width=wrap_width, replace_whitespace=False, drop_whitespace=False))

    f.write("""
{}
{}
def is_msvc2019_optimal(qt, compiler, arch):
    if arch == ARCH_32:
        return qt in QT_TO_MSVC2019_32
    else:
        return qt in QT_TO_MSVC2019_64
""".format(msvc2019_32_, msvc2019_64_))

    mingw32_ = "\n".join(textwrap.wrap("QT_TO_MINGW32 = " + to_mingw_dict(mingw32), width=wrap_width, replace_whitespace=False, drop_whitespace=False))
    mingw64_ = "\n".join(textwrap.wrap("QT_TO_MINGW64 = " + to_mingw_dict(mingw64), width=wrap_width, replace_whitespace=False, drop_whitespace=False))

    f.write("""
{}
{}
def qt_mingw_compiler(qt, arch):
    if arch == ARCH_32:
        return QT_TO_MINGW32.get(qt)
    else:
        return QT_TO_MINGW64.get(qt)
    """.format(mingw32_, mingw64_))

    