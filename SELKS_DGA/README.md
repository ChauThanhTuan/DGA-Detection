# Kết hợp SELKS, DGA và TheHive
***Lưu ý: để mô hình hoạt động bình thường, cần khởi động SELKS và TheHive lên trước, 
sau đó chỉnh sửa giá trị của "SELKS_IP" trong config.py thành IP tương ứng với máy đang chạy SELKS và TheHive***

## Mô tả
Hệ thống sẽ giám sát các DNS, phân tích việc truy cập Inernet của các người dùng trong mạng. Qua đó, trích xuất được các domain mà người dùng truy cập và phân loại domain đó. Kết quả phân loại sẽ được gửi trả lên lại cho SELKS và TheHive

## Cách thức hoạt động
Hệ thống sẽ truy xuất đến `http://<SELKS_IP>:9200/logstash-dns-<current_date>/_search` để trích xuất thông tin domain. 
Khi vừa khởi động (khởi chạy file `selks_dga.py`) thì nó sẽ trích xuất các domains từ 10 logs mới nhất và lặp lại sau mỗi 15'. 
Lúc này, nó sẽ không lấy 10 logs mới nhất nữa mà nó sẽ trích xuất các domains từ các logs trong vòng 15' vừa qua 
(Vì elasticsearch không hỗ trợ trích xuất logs theo thời gian thông qua API nên chúng tôi thay thế bằng cách trích xuất 100 logs mới nhất 
và kiểm tra id tuần tự từng log. Nếu id trùng với id của log cuối cùng của 15' trước thì quá trình kiểm tra sẽ dừng lại.)
Các domains trích xuất được sẽ được phân loại và gửi trả kết quả lên elasticsearch_index `classifyDomain`. 
Nếu Hệ thống phát hiện được DGA domain, nó cũng sẽ gửi thêm cảnh báo lên TheHive.

## Cách dùng:
- Trước hết cần chỉnh sửa giá trị của "SELKS_IP" trong config.py thành IP tương ứng với máy đang chạy SELKS và TheHive
- Nếu đây là lần đầu khởi động mô hình, cần phải thực thi file entrypoint.sh để thêm index "classifyDomain" vào kibana:</br>
```
./entrypoint
```
- Sử dụng
