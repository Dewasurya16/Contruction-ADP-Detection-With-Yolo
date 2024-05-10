# Contruction-ADP-Detection-With-Yolo

### dataset
*dataset saya menggunakan daataset Publik : https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow

Saya memilih dataset public ini karena mudah diakses, datanya berkualitas dan terstruktur, menghemat waktu dan biaya, serta mendukung kolaborasi dan reproduksibilitas penelitian. Selain itu, dataset ini memungkinkan pelatihan model yang lebih cepat, standarisasi performa, dan pembelajaran yang efektif dengan dukungan komunitas yang aktif.

### MODEL
Pelatihan model menggunakan YoloV8

### hasil Model
Hasil deteksi model menggunakan YOLOV8 Bisa dilihat di https://drive.google.com/file/d/1xsY-tl4BbsPvGcToizMX1cEgmggwGlaV/view?usp=sharing
  

  
### Akurasi Model
<img align ="Center" alt="coding" width="400"   src="https://github.com/Dewasurya16/wowok/blob/master/Screenshot_2.png">

- Install despendecies 
    ```terminal 
    git clone https://github.com/Dewasurya16/-Contruction-ADP-Detection-With-Yolo
    ```

- Go to the project folder

    ```Terminal
    cd Contruction-ADP-Detection-With-Yolo


- Install required dependencies

    ```Terminal 
    pip install -r /path/to/requirements.txt
    ```
- Run the server

    
    ```Terminal
     python app.py
    ```
    - Open <http://127.0.0.1:5000/> with your browser to run

  ### Cara kerja
Untuk menjalankan model bisa melakukan upload video yang akan di deteksi dengan menekan tombol upload di bagian Halaman Video. jika sudah terupload maka akan tampil video dengan deteksi secara realtime. Disarankan menggunakan video yang Landcsape.
