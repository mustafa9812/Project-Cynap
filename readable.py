import xml.etree.ElementTree as ET

# FULL path to your file — adjust as needed!
xml_path = "C:/Users/Mustafa/Documents/GitHub/Project-Cynap/pahdb-complete-theoretical-v4.00-alpha.xml"

print("Checking:", xml_path)

try:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    print("✅ XML file is readable!")
    print("Root element:", root.tag)
except ET.ParseError as e:
    print("❌ XML Parse Error:", e)
except FileNotFoundError:
    print("❌ File not found at that path.")
except Exception as e:
    print("❌ Other error:", e)
