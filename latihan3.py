random_list = [195, 3.1, "Halo", 737, "Python", 2.7, "Dunia", 412, 5.5, "AI"]

float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

def map_int_to_dict(value):
    def curry_mapping(satuan):
        def map_internal(puluhan):
            ratusan = value // 100
            return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}
        return map_internal
    return curry_mapping

int_mapped = list(map(lambda x: x(0)(0), map(map_int_to_dict, int_values)))

print("Data Float:", tuple(float_values))
print("Data Int:")
for data in int_mapped:
    print(data)
print("Data String:", [s.lower() for s in string_values])
 