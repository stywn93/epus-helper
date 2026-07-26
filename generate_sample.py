from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Data Pasien"

headers = ["nama", "no_rm", "keluhan", "diagnosa", "tindakan", "resep"]
ws.append(headers)

patients = [
    ["febby ridwan zaelani", "001234", "Sakit kepala", "Migrain", "Pemeriksaan umum", "Paracetamol 3x1"],
    ["andi saputra", "001235", "Batuk pilek", "ISPA", "Pemeriksaan tenggorokan", "Amoxicillin 3x1"],
]

for patient in patients:
    ws.append(patient)

wb.save("data-pasien.xlsx")
print("data-pasien.xlsx created successfully")
