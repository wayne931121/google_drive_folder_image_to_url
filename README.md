# Google Drive Folder Images To Website URL
將Google雲端硬碟資料夾圖片轉成可以放置網站中的圖片連結<br>

使用方法:
```cmd
C:\> python google_drive_folder_image_to_url.py -h
usage: google_drive_folder_image_to_url.py [-h] [-url URL] [-single SINGLE]

Google雲端硬碟資料夾圖片轉成可以放置網站中的圖片連結 Google drive image to website url, Test on 2023.06.08 zh_TW.

optional arguments:
  -h, --help            show this help message and exit
  -url URL, -u URL      輸入一個只有放圖片的公開Google雲端硬碟資料夾連結。 Please input a public google drive folder which
                        only place images.
  -single SINGLE, -s SINGLE
                        輸入一個單一圖片的公開Google雲端硬碟連結。 Please input a public google drive single image link.
```
將一個只有放圖片的公開Google雲端硬碟資料夾內的所有圖片轉成網址:<br>
示範: https://drive.google.com/drive/folders/1ilEyZoa7jn4emMF9PV4oAHtTnxbSV0rA?usp=drive_link
```cmd
C:\> python google_drive_folder_image_to_url.py -u https://drive.google.com/drive/folders/1ilEyZoa7jn4emMF9PV4oAHtTnxbSV0rA?usp=drive_link
轉成的網頁圖片連結，最高提供1600畫素乘以1200畫素。
20200731_142953.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81oEd_ZVjyRqjuMMP7ZpQnq9sBNXhVUdbTKjZd7X4Cy6Zj3Qyp73srsJ5jlITC2wKCriGFWFzzERNi5MPEOBnKfBsf0hlA=s1600
20200731_143003.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81ptH3DMn67BofO6mCOMlPzi5Z126cKekRyQuJ3K_zf_RzholFSKYPLKGBEh4GuXQKvTaNM1hq3ExIafv1wOKFWOk_k2EA=s1600
20200731_143006.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81oP-tGKlT_8QyE9UV0ODjhjw8fDTks6soSJdKMaR1wuTOJcYVf3MXlNI7COJBfreKznrWN7eI6U9DbQBSbrEsEUTVCy3Q=s1600
20200731_143007.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qt880DixREsRQQGegsqMHuHcIlNTAEfR13GV7Mb1ye36BFyW212aRI3pqJM6uaZzaCR7JwLsd27Dr2e6s6o2mpzc1O=s1600
20200731_143009.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81pJow9VJf668OzlW_vUC9aZS0IXTz9XymVQ1q4xisAQ6R3aE4cXhmhMzb9f_ZNPTvXFZdhPBc9qYIQPNk0m7-fTD86loQ=s1600
20200731_143015.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81rl3SrseBb2xz-UUhVSYNMTKNxLwxb0Dg-UtOq5sgIbaE7Fz4Gd8sjJP3sChJWQ2ZYub7weTHQuPDI8WC-e4QLBwwAM=s1600
20200731_143019.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81pOeP60gD0DI7NumagFlOa6sjRA6UjIsbPAzIWC1yJfwogWVLY2N3Vpulwh9Mhkd_3hX8omJf6P2zz6ABTdCy6SZTubrw=s1600
20200731_143036.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81rQiUrMdZzjtiKReBABW64yfmYvRUCvkEzh7_3m01D_HE_H8ndX3aI402USi3z2C87_-weR02-bryV7cShOMUHNBHOPaA=s1600
20200731_143124.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81rSxKKjclf6vrjczF2bGww4GQsneeQa5vJp4DdGxmA_qLCX6zCLJ1kcGaruQ3-d3a95YlDDpm5IINzDjfusQbHa7NHw6A=s1600
20200731_143131.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81o5kizlFIaAZh9BZtrYQcB--d4j3_Gc9cvmSfLU3U0DVdKuDTD9BfSKdznuttbe5iZ-9sI9Jvk0q14i_ODMbPjgcvFP7A=s1600
20200731_143230.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qGPvdoGyjjs-j8wSSjpq84YJIbDp7LayeKsWD5OZSXuPKSgJ52UPjYHhEktXjF2ZY3kv0zVj3BsTZ4rThSPniM9twZgg=s1600
20200731_143237.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qwJ5paTQHwXwJa3xEzznHFixJydJdiIbqWwA-17V0943tSbL5rhz58UorhdUBI7MB1T7h-2Zp2sk6Rm42-dtUXjLCYvA=s1600
20200731_143241.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81pv0VPmZaJJB5Sj28qFoIiEg1DtMDJInfbCtJBJ2k_TpdHKedoUtsVPd57CpPzcz5ocFSY-I1Sb5kYZ3_E63bPVDzWgmg=s1600
20200731_143246.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81pDExFeYfZ558uUoZTdMH58IRk9_21IQA3wE3_XhDOWO5M55-woeuI3Ho2MU20xakKaIlykCVxcgTQI72RT9K1nF4VG=s1600
20200731_143248.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qy6BnltaFLrieccgEANVcOKb8JxJruxng3--KPJlvtbijqcRcPE60aw5uaDdpzvDp3jju42r2wIHCLZ9bmy8NKfQamRw=s1600
20200731_143313.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81r7MeL_l6k0kEltn1kIzt8iUzSJ4XCDSqRlQPEHYr4222N8csZFmfGg0qOExMtYLJkpR5FGP0-osIOL4E8FR_X1trJZ=s1600
20200731_143314.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qKvbbCq9edK6x5HsgZPk-LSr2g_kl51CK8V82crsOLLMFuQoNk7pTkx4jxSTzLyOSpzn6Y8CkMPnYBRAKsTisNR5_zHQ=s1600
20200731_143315.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81r2UE3qC1vUhdbw5_RCGkSuaFh9bmxATdlx6XhFrJyUxHryWL5GieVdtV2y7Ru1ykoe5I9kLV_DAopVmWDrQCTBwO-VfA=s1600
20200731_143321.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qJiWjDjngIsqmP_v-iB1kiDt23uzhfhHbQxcvwIjFPtlY32N0ETDr57kenwjLO3_tPxayhj7sUfonOW-hO1q1w87P8=s1600
20200731_143322.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81q9yoW_V-m5TiDg-43tz_HWrMpp85v1KARKGRE3AAIHAuehZjMI3BQ-hGXU4Rv5omhLQW1PXdN12uu-Lu8fQmjJxH4M0A=s1600
20200731_143323.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81q-kQDHwVIduGz2zB8uFHhn9iZA2NuvbgOarqDGGpyXpUSHOmXRChww2UGsH3pqPrj2-sB1zZjLWQ5-2raBwddfpdxV8w=s1600
20200731_143325.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81ojb5JhaUd10hdGIMrE23gMxRuoJ6lRz1OtQfHUHFgV_e-ZageUZiE_32j2lItPBFO1CESvsCaopDYV7pGvB5OeGv1E8Q=s1600
20200731_143338.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81rGuNWlPEO3bzq40-DpfV7ELr_A8BLwrPv_DaY528gowLO7fdy5V-wn_luYp6v3iAxAfg4Naks0SV1_3bWU9oQAYmjS=s1600
20200731_143348.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81rTE4VBFPHPSNLNSLGkOjphAAdiHk8lASKmj49IcSGUq6B9yEATM9RhixLRtlmjyFBXW7Ar-jx-_NnGiYFPc-B0kXa0xQ=s1600
20200731_143353.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81pfhbfnKQcmpC_mRgg66k6fVHpAsoVGhWmVh5bGx8YAIpfqkIDYcZGw6dzz6Wz0Nrtwro5z1Vu3jHPEfFThnh_Za_wBOA=s1600
20200731_143440.jpg : https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qVO5jv0zFfz6qvslRGc0JnTMKp1j7UiSrR7FEw0PyLWLXlbFAeuLTvlfDrmAPgRe8vCa4C7tzrv3ISKeudaH5jkHSL=s1600
```
將單一公開Google雲端硬碟圖片轉成網址:<br>
示範: https://drive.google.com/file/d/1P2_3Vsi_HDe4tKTvNax3A1bzV6283RjD/view?usp=drive_link
```cmd
C:\> python google_drive_folder_image_to_url.py -s https://drive.google.com/file/d/1P2_3Vsi_HDe4tKTvNax3A1bzV6283RjD/view?usp=drive_link
轉成的網頁圖片連結，最高提供1600畫素乘以1200畫素。
https://lh3.googleusercontent.com/u/0/drive-viewer/AFGJ81qKvbbCq9edK6x5HsgZPk-LSr2g_kl51CK8V82crsOLLMFuQoNk7pTkx4jxSTzLyOSpzn6Y8CkMPnYBRAKsTisNR5_zHQ=s1600
```
