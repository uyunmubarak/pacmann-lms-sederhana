import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    """Membuat koneksi ke server MySQL.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
    except Error as err:
        print(f"Error: {err}")
        
    return connection


def create_database(connection, query):
    """Membuat database baru.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Error as err:
        print(f"Error: {err}")


def create_connect(host_name, user_name, user_password, db_name):
    """Memodifikasi fungsi create_server_connection untuk terhubung langsung ke database.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db
        )
        print("MySQL Database connection succesfull")
    except Error as err:
        print(f"Error: {err}")
        
    return connection


def execute_query(connection, query):
    """Fungsi untuk mengeksekusi query.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: {err}")
      
    
def read_query(connection, query):
    """Fungsi untuk membaca data dari database.
    """
    cursor = connection.cursor(buffered=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")
        
        
create_users_table = """
CREATE TABLE IF NOT EXISTS anggota (
    id_user INT AUTO_INCREMENT, 
    u_name VARCHAR(25), 
    tgl_lahir DATE, 
    pekerjaan VARCHAR(30), 
    alamat VARCHAR(35), 
    PRIMARY KEY (id_user)
) 
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS buku (
    id_buku VARCHAR(10),
    nama_buku VARCHAR(50),
    kategori VARCHAR(25),
    stock INT,
    PRIMARY KEY (id_buku)
)
"""

create_lending_table = """
CREATE TABLE IF NOT EXISTS peminjaman (
    id_user INT,
    id_buku VARCHAR(10),
    nama_user VARCHAR(25),
    nama_buku VARCHAR(50),
    tanggal_pinjam DATE,
    tgl_pengembalian DATE
)
"""

kurangi_stock = """
    CREATE TRIGGER IF NOT EXISTS pinjam_buku 
        AFTER INSERT ON peminjaman
        FOR EACH ROW 
    BEGIN
        UPDATE buku
        SET stock = stock - 1
        WHERE id_buku = NEW.id_buku; 
    END
"""

tambah_stock = """
    CREATE TRIGGER IF NOT EXISTS kembalikan_buku 
        AFTER DELETE ON peminjaman
        FOR EACH ROW 
    BEGIN
        UPDATE buku
        SET stock = stock + 1
        WHERE id_buku = OLD.id_buku; 
    END
"""        

host = "localhost"
user = "root"
pw = "xxxxx"
db = "lms_sederhana"

connection = create_server_connection(host, user, pw)
create_database_query = "CREATE DATABASE IF NOT EXISTS lms_sederhana"
create_database(connection, create_database_query)
connection = create_connect(host, user, pw, db)
execute_query(connection, create_users_table)
execute_query(connection, create_books_table)
execute_query(connection, create_lending_table)
execute_query(connection, kurangi_stock)
execute_query(connection, tambah_stock)


def main():
    """Menampilkan menu utama dari program.
    """
    print("""............LIBRARY MANAGEMENT............
    1. Pendaftaran User Baru
    2. Pendaftaran Buku Baru
    3. Peminjaman
    4. Tampilkan Daftar Buku
    5. Tampilkan Daftar User
    6. Tampilkan Daftar Peminjam
    7. Cari Buku
    8. Pengembalian
    9. Exit
    """)
    
    input_tugas = input("Masukkan Nomor Tugas:")
    print("...........................................")
    if(input_tugas == '1'):
        tambah_user()
    elif(input_tugas == '2'):
        tambah_buku()
    elif(input_tugas == '3'):
        pinjam_buku()
    elif(input_tugas == '4'):
        tampil_buku()
    elif(input_tugas == '5'):
        tampil_user()
    elif(input_tugas == '6'):
        tampil_peminjam()
    elif(input_tugas == '7'):
        cari_buku()
    elif(input_tugas == '8'):
        kembali_buku()
    elif(input_tugas == '9'):
        print("Sampai jumpa")
        quit()
    else:
        print("Nomor tugas tidak valid \n")
        main()
        
        
def tambah_user():
    """Menambahkan data anggota perpustakaan ke dalam database.
    """
    u_name = input("Masukkan nama user: ")
    tgl_lahir = input("Masukkan tanggal lahir(YYYY-MM-DD): ")
    pekerjaan = input("Pekerjaan: ")
    alamat = input("Alamat: ")
    data = (u_name, tgl_lahir, pekerjaan, alamat)
    
    query_insert_data = "INSERT INTO anggota VALUES(id_user,%s,%s,%s,%s)"
    cursor = connection.cursor(buffered=True)
    cursor.execute(query_insert_data, data)
    connection.commit()
    print("...........................................")
    print("Data berhasil ditambahkan!")
    print("...........................................")
    main()
    
    
def tambah_buku():
    """Menambahkan data buku perpustakaan ke dalam database.
    """
    id_buku = input("Masukkan kode buku: ")
    nama_buku = input("Enter book name: ")
    kategori = input("Masukkan kategori buku: ")
    stock = input("Stok buku: ")
    data = (id_buku, nama_buku, kategori, stock)
    
    query_insert_data = "INSERT INTO buku VALUES(%s,%s,%s,%s)"
    cursor = connection.cursor(buffered=True)
    cursor.execute(query_insert_data, data)
    connection.commit()
    print("...........................................")
    print("Data entered succesfully")
    print("...........................................")
    main()

    
def pinjam_buku():
    """Menambahkan data peminjaman buku ke dalam database.
    """
    id_user = input("Masukkan id peminjam: ")
    id_buku = input("Masukkan id buku: ")
    nama_user = input("Masukkan nama peminjam: ")
    nama_buku = input("Masukkan nama buku: ")
    data = (id_user, id_buku, nama_user, nama_buku)
    
    query_insert_data = """
        INSERT INTO peminjaman
        VALUES(%s,%s,%s,%s,CURDATE(),CURDATE()+3)
    """
    cursor = connection.cursor(buffered=True)
    cursor.execute(query_insert_data, data)
    connection.commit()
    print("...........................................")
    print("Buku dipinjamkan ke : ", nama_user)
    print("...........................................")
    main()
    
    
def tampil_buku():
    """Menampilkan daftar buku perpusatakaan.
    """
    query_tampil_data = "SELECT * FROM buku"
    results = read_query(connection, query_tampil_data)
    
    from_db = []
    for result in results:
        result = list(result)
        from_db.append(result)
    columns = ["id_buku", "nama_buku", "kategori", "stock"]
    df = pd.DataFrame(from_db, columns=columns)
    print(df)
    print("...........................................")
    main()  
    

def tampil_user():
    """Menampilkan anggota perpustakaan.
    """
    query_tampil_data = "SELECT * FROM anggota"
    results = read_query(connection, query_tampil_data)
    
    from_db = []
    for result in results:
        result = list(result)
        from_db.append(result)
    columns = ["id_user", "u_name", "tgl_lahir", "pekerjaan", "alamat"]
    df = pd.DataFrame(from_db, columns=columns)
    print(df)
    print("...........................................")
    main()


def tampil_peminjam():
    """Menampikan data peminjaman buku.
    """
    query_tampil_data = "SELECT * FROM peminjaman"
    results = read_query(connection, query_tampil_data)
    
    from_db = []
    for result in results:
        result = list(result)
        from_db.append(result)
    columns = ["id_user", "id_buku", "nama_user", "nama_buku",
               "tanggal_pinjam", "tgl_pengembalian"]
    df = pd.DataFrame(from_db, columns=columns)
    print(df)
    print("...........................................")
    main()

    
def cari_buku():
    """Melakukan pencarian buku perpustakaan.
    """
    kode = input("Masukkan nama buku yang ingin dicari: ")
    cursor = connection.cursor(buffered=True)
    cursor.execute("""
        SELECT * FROM buku
        WHERE nama_buku LIKE \'%' %s '%\'
    """, (kode,))
    
    from_db = []
    for row in iter(cursor.fetchone, None):
        row = list(row)
        from_db.append(row)     
    columns = ["id_buku", "nama_buku", "kategori", "stock"]
    df = pd.DataFrame(from_db, columns=columns)
    print(df)
    print("...........................................")
    main()
    

def kembali_buku():
    """Menghapus data peminjaman buku.
    """
    id_user = input("Masukkan id peminjam: ")
    id_buku = input("Masukkan id buku: ")
    data = (id_buku, )
    
    query_insert_data = """
        DELETE FROM peminjaman
        WHERE id_buku = %s
    """
    cursor = connection.cursor(buffered=True)
    cursor.execute(query_insert_data, data)
    connection.commit()
    print("...........................................")
    print("Buku telah dikembalikan")
    print("...........................................")
    main()
    
       
main()