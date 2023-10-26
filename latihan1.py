def convert_menit(minggu, hari, jam, menit):
    total_menit = (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
    return total_menit

def curry_convert_menit(minggu):
    def curry_hari(hari):
        def curry_jam(jam):
            def curry_menit(menit):
                return convert_menit(minggu, hari, jam, menit)
            return curry_menit
        return curry_jam
    return curry_hari

def higher_order_function(data, curry_function):
    output_data = []
    for item in data:
        parts = item.split()
        minggu = int(parts[0])
        hari = int(parts[2])
        jam = int(parts[4])
        menit = int(parts[6])
        result = curry_function(minggu)(hari)(jam)(menit)
        output_data.append(result)
    return output_data

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

output_data = higher_order_function(data, curry_convert_menit)

print(output_data)