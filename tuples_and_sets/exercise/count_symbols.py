text = input()
ch_times = {}
for ch in text:
    if ch not in ch_times:
        ch_times[ch] = 0
    ch_times[ch] += 1

for key, value in sorted(ch_times.items()):
    print(f"{key}: {value} time/s")
