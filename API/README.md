# Dự đoán DGA thông qua API
## Mô tả
Khi chạy file `API.py`, nó sẽ lắng nghe kết nối ở port 5000 và dự đoán xem domain từ người dùng gửi lên có phải là DGA hay không
thông qua mô hình được train từ https://github.com/Tuan164/DGA.</br>
Kết quả được trả về dưới dạng json với format:</br>
"domain": "isDGA"</br>

## Cách dùng
### *Server*
- Cách 1: Clone from github
```
git clone https://github.com/Tuan164/SELKS_DGA.git
cd SELKS_DGA/API
python3 API.py
```
    
![image](https://user-images.githubusercontent.com/54493212/186891045-fc799837-a732-47f2-87d4-e35d7e1a4d0e.png)

- Cách 2: Pull from dockerhub
```
docker pull 1642001/dga_detect
docker run -d -p 0.0.0.0:5000:5000 1642001/dga_detect
```

![image](https://user-images.githubusercontent.com/54493212/186911262-a8966e19-cd5b-4d70-a0ba-46ae644557fe.png)

### *Client*
    curl http://<Server_IP>:5000/<Domain_name>
  
Kết quả khi truy cập với domain hợp lệ</br>
![image](https://user-images.githubusercontent.com/54493212/186892970-2ae63ca0-7574-4052-8e42-c51d61c86fed.png)

Kết quả khi truy cập với DGA domain</br>
![image](https://user-images.githubusercontent.com/54493212/186893004-98951134-e792-4bb8-8551-8125e28b3c0b.png)
