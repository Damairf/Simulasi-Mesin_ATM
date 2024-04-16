import time
print('Simulasi mesin ATM')

saldoAwal = 1200000

while True:
    user = int(input('Transaksi apa yang ingin anda lakukan :\n(1) Informasi Saldo\n(2) Setor Tunai\n(3) Penarikan Tunai\n(4) Transfer\nPILIH KODE MENU: '))
    if user < 1 or user > 4:
        print('Kode tidak valid. Silahkan masukan kode menu')
        print()
    else:
        print()
        break

if user == 1:
    print('Informasi Saldo')
    print('Saldo anda:')
    print('Rp. 1200000')

if user == 2:
    print('Setor Tunai')
    setor = int(input('Silahkan masukkan nominal uang yang ingin anda setorkan: Rp. '))
    print('Menunggu proses')
    time.sleep(1.5)
    print('Transaksi berhasil')
    print('Anda berhasil menyetor uang sebanyak Rp.', setor, 'ke rekening anda')
    print('Saldo di rekening anda: Rp.', saldoAwal + setor)

if user == 3:
    print('Penarikan Tunai')
    while True:
        tarik = int(input('Nominal uang yang ingin anda tarik: Rp. '))
        if tarik > 1200000:
            print('Saldo anda tidak cukup')
            print('Anda memiliki saldo sebesar Rp. 1200000')
            print()
        else:
            print('Menunggu proses')
            time.sleep(1.5)
            print('Transaksi berhasil')
            print('Anda telah berhasil melakukan penarikan tunai sebesar: Rp.',tarik)
            print('Sisa saldo anda: Rp.',saldoAwal - tarik)
            break

if user == 4:
    print('Transfer')
    while True:
        norek = input('Silahkan masukkan nomor rekening (6 digit): ')
        if len(norek) != 6 or not norek.isdigit():
            print('Nomor tidak valid. Nomor rekening harus terdiri dari 6 digit angka')
            print()
        else:
            print('Nomor rekening ditemukan')
            while True:
                transfer = int(input('Masukkan nominal transfer: Rp. '))
                if transfer > saldoAwal:
                    print('Saldo anda tidak cukup')
                    print('Anda memiliki saldo sebesar Rp. 1200000')
                    print()
                else:
                    print('Menunggu proses')
                    time.sleep(1.5)
                    print('Transaksi berhasil')
                    print('Anda berhasil mentransfer uang sebesar Rp.', transfer, 'ke nomor rekening', norek)
                    break
            break
