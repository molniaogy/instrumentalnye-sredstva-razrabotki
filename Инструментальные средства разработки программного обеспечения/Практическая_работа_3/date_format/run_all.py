import json
import os
import msgpack
import cbor2
import yaml
import xml.etree.ElementTree as ET
import profile_pb2
from data import PROFILE

os.makedirs("received", exist_ok=True)
results = []

# JSON
j = json.dumps(PROFILE, ensure_ascii=False).encode("utf-8")
results.append(("JSON", len(j)))


# XML
def dict_to_xml(tag, d):
    elem = ET.Element(tag)
    for k, v in d.items():
        if isinstance(v, dict):
            elem.append(dict_to_xml(k, v))
        elif isinstance(v, list):
            le = ET.SubElement(elem, k)
            for i in v:
                ET.SubElement(le, "item").text = str(i)
        else:
            ET.SubElement(elem, k).text = str(v)
    return elem


xml = ET.tostring(dict_to_xml("profile", PROFILE), encoding="utf-8")
results.append(("XML", len(xml)))

# YAML
y = yaml.dump(PROFILE, allow_unicode=True).encode("utf-8")
results.append(("YAML", len(y)))

# MessagePack
m = msgpack.packb(PROFILE, use_bin_type=True)
results.append(("MessagePack", len(m)))

# CBOR
c = cbor2.dumps(PROFILE)
results.append(("CBOR", len(c)))

# Protobuf
p = profile_pb2.Profile()
p.id = PROFILE["id"]
p.name = PROFILE["name"]
p.age = PROFILE["age"]
p.is_student = PROFILE["is_student"]
p.courses.extend(PROFILE["courses"])
p.address.city = PROFILE["address"]["city"]
p.address.zip = PROFILE["address"]["zip"]
pb = p.SerializeToString()
results.append(("Protobuf", len(pb)))

print(f"\n{'Формат':<14} {'Размер (байт)':>14} {'Читаем?':>10}")
print("-" * 42)
for name, size in results:
    readable = "да" if name in ("JSON", "XML", "YAML") else "нет"
    print(f"{name:<14} {size:>14} {readable:>10}")

# Сохраняем JSON-отчет
report = [{"format": n, "wire_size_bytes": s} for n, s in results]
json.dump(report, open("received/report.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
