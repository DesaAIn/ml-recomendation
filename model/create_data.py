import json
import random

def generate_data_entry():
    kesesuaian_rencana = round(random.uniform(0.5, 1.0), 2)
    persentase_dana = round(random.uniform(0.5, 1.0), 2)
    selisih_hari = random.randint(-30, 30)

    # Default "saran" and specific issue trackers
    saran = ""
    penyimpangan = []

    # Check for each factor's compliance with thresholds and collect specific feedback
    if kesesuaian_rencana < 0.7:
        penyimpangan.append("Kesesuaian dengan rencana di bawah standar, perlu perhatian khusus.")
    if persentase_dana < 0.8:
        penyimpangan.append("Penggunaan dana di bawah batas optimal.")
    if persentase_dana > 1:
        penyimpangan.append("Penggunaan dana di atas batas optimal.")
    if selisih_hari > 15:
        penyimpangan.append("Waktu pelaksanaan proyek melebihi batas toleransi keterlambatan.")
    if selisih_hari < -15:
        penyimpangan.append("Waktu pelaksanaan proyek melebihi batas toleransi keterlambatan.")

    # Determine overall "saran" based on conditions
    if kesesuaian_rencana > 0.9 and persentase_dana > 0.9 and selisih_hari <= 5:
        saran = "Proyek berjalan sangat baik sesuai perencanaan."
    elif kesesuaian_rencana > 0.8 and persentase_dana > 0.85 and selisih_hari <= 10:
        saran = "Proyek sedikit menyimpang, namun masih dalam batas wajar."
    elif kesesuaian_rencana > 0.7 and persentase_dana > 0.8 and selisih_hari <= 20:
        saran = "Terdapat beberapa penyimpangan yang perlu diperhatikan."
    elif kesesuaian_rencana > 0.6 and persentase_dana > 0.75 and selisih_hari <= 30:
        saran = "Proyek cukup menyimpang dari rencana, memerlukan evaluasi."
    else:
        saran = "Penyimpangan signifikan, evaluasi mendalam diperlukan."

    # Combine the overall "saran" with specific "penyimpangan" details
    if penyimpangan:
        saran += " Penyimpangan yang teridentifikasi: " + "; ".join(penyimpangan)

    return {
        "Kesesuaian_Rencana": kesesuaian_rencana,
        "Persentase_Dana": persentase_dana,
        "Selisih_Hari": selisih_hari,
        "Saran": saran
    }


# Generate 500 entries
dataset = [generate_data_entry() for _ in range(1000)]

# Save dataset to JSON file
file_path = "dataset_1000_entries.json"
with open(file_path, 'w') as json_file:
    json.dump(dataset, json_file)

file_path
