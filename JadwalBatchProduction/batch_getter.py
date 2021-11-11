# 1, max, max, list, sk
def get_batch(hari_kerja, durasi_produksi, durasi_setup, data_produksi, jam_kerja):
    # Fungsi pencari faktor
    def faktor(number):
        div = set()
        for jd in range(1, number+1):
            if number % jd == 0:
                div.add(jd)
        return div

    # Cari max setup sehari
    durasi_setup_total = (jam_kerja*hari_kerja-sum(data_produksi)*durasi_produksi)//durasi_setup
    max_setup = durasi_setup_total//hari_kerja

    # Cari max produksi sehari
    produksi_sehari = (jam_kerja-max_setup*durasi_setup)//durasi_produksi

    # Pengurutan data produksi kecil ke besar
    # data_produksi.sort()

    # Pencarian faktor
    faktor_persekutuan_total = []
    for i in range(len(data_produksi)):
        faktor_persekutuan_total.append(faktor(data_produksi[i]))

    # Pencarian faktor persekutuan
    faktor_persekutuan = set(faktor_persekutuan_total[0])
    for s in faktor_persekutuan_total:
        faktor_persekutuan.intersection_update(s)

    faktor_persekutuan = list(faktor_persekutuan)
    faktor_persekutuan.sort()
    # faktor_persekutuan jumlah tiap jenis dengan faktor persekutuan disimpan ke list isi list
    hasil_bagi_dummy = []
    for i in faktor_persekutuan:
        calc = []
        for j in data_produksi:
            calc.append(j//i)
        hasil_bagi_dummy.append(calc)

    hasil_bagi_dummy.reverse()
    hasil_bagi = hasil_bagi_dummy.copy()
    # hasil_bagi = []
    # Jika total batch tiap jenis < maks. produksi_sehari sehari_kerja, otomatis dilewati
    # for i in range(len(hasil_bagi_dummy)):
    #     if sum(hasil_bagi_dummy[i]) >= produksi_sehari:
    #         hasil_bagi.append(hasil_bagi_dummy[i])
    #
    # if not hasil_bagi:
    #     hasil_bagi.append(hasil_bagi_dummy[0])

    # Pemilihan batch
    p = 0
    q = 0
    setup = 0
    pilihan = 0
    jenis = 0
    pilihannya = hasil_bagi[-1]
    for i in range(sum(data_produksi)):
        p += 1
        q += 1
        if p % produksi_sehari == 0:
            setup = 0
        if q == hasil_bagi[pilihan][jenis]:
            if p % produksi_sehari == 0:
                setup = 0
                jenis += 1
                q = 0
                if jenis > len(hasil_bagi[pilihan]) - 1:
                    jenis = 0
                if setup > max_setup:
                    pilihan += 1
            else:
                setup += 1
                jenis += 1
                q = 0
                if jenis > len(hasil_bagi[pilihan])-1:
                    jenis = 0
                if setup > max_setup:
                    pilihan += 1
        if p == sum(data_produksi):
            pilihannya = hasil_bagi[pilihan]
    return pilihannya
