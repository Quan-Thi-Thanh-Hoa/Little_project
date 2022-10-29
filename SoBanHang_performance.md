# Report SoBanHang's Analyst Performance

## SoBanHang'S Traffic Trend

Trực quan hóa dữ liệu bằng [Power BI]

<img src="https://github.com/Quan-Thi-Thanh-Hoa/Funda_Python/blob/20ed60b1896ee9a43106a6e2d0e5850a6f5d3de8/Screenshot%202022-10-29%20152547.png">

Có thể thấy được 6 tệp khách hàng chủ yếu ở khu vực miền nam và miền trung, đối với miền bắc hiện mới có thủ đô ở hà nội có số lượng khách hàng quan tâm lớn. Các tỉnh phát triển mạnh về kinh tế hiện nay như Việt trì, Vĩnh phúc, Bắc ninh cũng có thể nghiên cứu kế hoạch để làm chiến dịch marketing thu hút lượng khách hàng ở thị trường này.

#### Theo khu vực: 

Ở đây chúng ta sẽ có thể thấy các khu vực hiện đang hoạt động khá là đồng đều và ổn định với nhau về số liệu qua từng tháng, vậy nghĩa là công ty đã làm rất tốt về sản phẩm cốt lõi để khách tin tưởng sử dụng dịch vụ. 

Như đã nêu bên trên ở quá trình phân tích dữ liệu, ta có thể tìm kiếm dữ liệu để phân tích và lập chiến lược đầu tư, marketing để phát triển sản phẩm ở các tỉnh thành khác. 

Về khách hàng: Chúng ta thấy được thời lượng trung bình của các phiên đăng nhập tại các khu vực tìm ra 1,000 khách hàng quan tâm nhất đối với SoBanHang ở các khu vực trên tổng 30,000 user_id để mình hành động cho những chiến dịch chăm sóc, tri ân khách hàng của SoBanHang. 1,000 khách hàng và tỉnh thành em sẽ để ở file đính kèm với báo cáo.

Các chỉ số về impression tại line and stacked column chart cho ta thấy được luôn giữ vị trí cao nhất ở screen_name là: report_management, sau đó là promotion_management và thất nhất là kênh chat_management. Vậy ta sẽ lên kế hoạch tạo trải nghiệm khách hàng tập trung tại các kênh có lưu lượng truy cập cao, và hành động để tìm hiểu lý do kênh chat và kênh community lại có lượng truy cập thấp hơn các kênh còn lại, và trả lời câu hỏi cần thiết “Phải làm sao để cải tăng lưu lượng click tại các kênh này của khách hàng?”

## SoBanHang's demongraphics

<img src="https://github.com/Quan-Thi-Thanh-Hoa/Funda_Python/blob/20ed60b1896ee9a43106a6e2d0e5850a6f5d3de8/Screenshot%202022-10-29%20152829.png">

Đầu tiên chúng ta hiểu nhân khẩu học là gì?
Nhân khẩu học được hiểu là quá trình thu thập và nghiên cứu các dữ liệu liên quan tới đặc điểm về tuổi tác, giới tính và chủng tộc của con người.
Phân tích nhân khẩu học dựa theo các yếu tố trên có thể được áp dụng cho một nhóm đối tượng/ nhóm người nào đó hoặc toàn bộ xã hội.
Theo như dữ liệu em sẽ hiểu về:
mức độ quan tâm của các user_id về các nhóm ngành hàng (thực phẩm, tạp hóa,…) qua thuộc tính active_days; 
mức độ doanh thu của các nhóm hàng ra sao qua thuộc tính transaction_value;

-> Từ đó ta sẽ thấy được nhóm hàng nào sẽ có mức độ quan tâm, mức độ doanh thu phụ thuộc vào khoảng thời gian trong năm.

Sau khi sử dụng mysql để kiểm tra dữ liệu em thấy được values thu được cao nhất cho cả hai loại ngành hàng mà khách hàng sử dụng sổ bán hàng đều ở HCM, trong khi đó đối với ngành hàng chính thấp nhất là thực phẩm tại Long An và thời trang tại Đồng Nai. 
Tuy nhiên các chỉ số ở cả hai ngành hàng cho thấy số lượng giao dịch không quá chênh lệch. Cụ thể ở ngành hàng chính trong khoảng thời gian 6 tháng cuối năm 2020 và trước tết này, lưu lượng giao dịch là 1720 chỉ cao hơn mỹ phẩm là 120 lượt đặt hàng. 

Từ đây, ta cũng thấy được đối với nhóm hàng F&B, lượng khách hàng quan tâm chính sẽ ở khu vực Hà Nội và tương tự như thế, tại Long An, nhóm khách hàng quan tâm chính ở đây là thực phẩm.


## Personal Marketing Brand

<img src="https://media-exp1.licdn.com/dms/image/C561BAQEWcBOxrvwIqA/company-background_10000/0/1650336590949?e=2147483647&v=beta&t=ODhLo7XemuwDF6BmG0d-r2OZRMo0vU56Eybgfrxll8k">

SoBanHang đều đặn chăm sóc fanpage để marketing thương hiệu và tiếp cận khách hàng, tuy nhiên lượt tiếp cận và lượng tương tác chưa được cao.
Cần giải quyết bài toán thuật toán của Facebook, lượng người share bài viết sẽ rất quan trọng nhưng bài viết chưa đạt tới được emotion của khách hàng để khiến họ sẵn sàng share.

Một số bài đăng có phạm vi tiếp cận và mức độ tương tác thấp vì mảng marketing chưa hiệu quả. Để cải thiện CTR cần những yếu tố về cá nhân em đưa ra 6 quan điểm cần:

1. Thông tin để tám: SoBanHang có thông tin gì để khách hàng thấy mình dùng sản phẩm tối ưu được cho dịch vụ bán hàng quán mình. Quản lý khách hàng, tiết kiệm chi phí vận hành như thế nào nhờ có sổ bán hàng. Vấn đề làm sao để người ta có câu chuyện để tám. SoBanHang có gì thú vị để khách có thể tám?
Ví dụ content:
+ Bạn là chủ cửa hàng, bạn thường lưu trữ dữ liệu đơn đặt hàng, bán hàng, doanh số bán hàng và nhân viên theo cách nào?
           * files excel, app tính lương, trích xuất bảng tính lương vân tay, viết hàm trên excel để tính doanh thu tháng.
           * Tại sao phải dùng nhiều bước trong thời đại số hóa như vậy nhỉ khi đã có SoBanHang rồi. Chỉ cần một lần đăng ký, có ngay hệ thống tự động cho bạn vận hành cửa hàng mình một cách trơn chu từ khách hàng đến nhân viên.
==> Khi có thông tin để tám thì sản phẩm sẽ được nhiều người biết đến mà không phải tốn tiền quảng cáo. Phải cung cấp Contagious để họ trao đổi, để khách hàng thấy được họ có đặc quyền ít nhất là về mặt thông tin. Hoặc tạo chú ý, quan tâm ví dụ mỗi lần mở app khách hàng có thể sẽ thấy được một thông tin về xu hướng thị trường, về thời tiết trong ngày, về những điều thú vị trong cuộc sống để khách hàng có câu chuyện để nói với nhau.
2. Trigger (Liên tưởng): Bối cảnh thông điệp ý tưởng liên quan. 

- Bối cảnh thời đại số hóa, các cửa hàng lớn nhỏ trên thị trường đều trên đà chuyển đổi số để tối ưu chi phí, tăng độ tiếp cận tới khách hàng tìm kiếm khách hàng tiềm năng tạo doanh thu. SoBanHang làm sao để khách hàng chưa sử dụng app thấy được điều này? Trong các chiến dịch Marketing chưa thực sự thấy đẩy mạnh cách khách hàng tiếp cận được khách hàng mục tiêu dễ dàng như thế nào để tăng độ liên tưởng -> thúc đẩy cảm xúc.

- Sologan thực sự của SoBanHang là gì? Buôn có bạn, bán có SoBanHang? Sổ Bán Hàng bán là nhàn? Nếu là slogan trong thời điểm tạo dựng branding vững mạnh, cá nhân em thấy cần luôn marketing slogan đi kèm sản phẩm để nhắc đi nhắc lại trong tâm trí khách hàng liên tưởng đến việc dùng sổ bán hàng, bán là sẽ nhàn. Điều này không thấy được lặp lại thường xuyên.

- Ví dụ chiến dịch whassup tạo viral toàn thế giới tạm dịch: Ê có gì mới không của thanh niên, ví dụ sologan: kitkat - take a break - take a kitkat, kinh đô đc liên tưởng nhiều nhất đến tết mặc dù rất nhiều, hoặc heniken sở hữu trigger giáng sinh, năm mới, cũng dễ liên tưởng màu xanh lá cây.
3. Cảm xúc: emotion: chia sẻ nội dung cũng ít nhiều chia sẻ về cảm xúc của mình, cảm xúc về một giấc mơ cho điều gì?

- Giấc mơ của SoBanHang là gì? Giấc mơ của nhóm đối tượng khách hàng của mình là gì? Khi khách hàng chia sẻ clip marketing của SoBanHang, cũng là chia sẻ về một giấc mơ không những vươn xa hơn mà còn mang đến những trải nghiệm khách hàng tốt cho người dùng cuối cùng trên một thị trường đầy biến động hiện nay.

Rằng không chỉ SoBanHang mà những khách hàng của SoBanHang cũng có những giấc mơ như vậy.

Cảm xúc có hai thái cực: Vui và buồn. Nếu không dùng SoBanHang, trong thời đại số hóa khách hàng vẫn phải loay hoay làm những công việc thủ công như thế nào? Điều đó khiến họ trăn trở và buồn phiền như thế nào? 

Cảm xúc thông tin mà SoBanHang mang lại cho khách hàng là gì vì chính cảm xúc mới dẫn dắt khách hàng hành động, cụ thể là chia sẻ.
4. Public (Công chúng): Các ý tưởng cần lan truyền phải làm sao để khách hàng dễ thấy, khi đó họ mới thấy dễ bị thuyết phục. 

Ví dụ: Thử thách xô nước đá, người chơi chấp nhận bị dội xô nước đá và phải chi $10 để quyên góp nếu không phải bỏ $100 cho quỹ phòng chống teo cơ, sau khi hoàn thành thử thách bạn có quyền thách thức người kế tiếp. Và tất nhiên ai cũng muốn có một tấm hình trên FB để cho mọi người đều thấy và sau đó lại thách thức người kế tiếp. 

Vấn đề của doanh nghiệp là: làm sao biến những người tham gia có hoạt động riêng lẻ cho nhiều người cùng biết như vậy và khi đó nhiều người sẽ tham gia và bắt chước. Hoặc làm sao để thương hiệu tự quảng cáo: khách hàng sẵn lòng khoe với người khác.
5. Practical values (Giá trị thực tế): Chia sẻ thông tin vì chính giá trị và lợi ích của thông tin của nó đem lại cho người dùng. 

Hai loại thông tin: Mang giải trí hoặc phải có ý nghĩa. Cần chiến lược đầu tư thương hiệu của công ty là gì? 

Nếu mang tính giải trí thì tạo những video đơn giản, gần gũi nhất như về trải nghiệm khách hàng, vui khi dùng Sổ Bán Hàng hay buồn nếu không có Sổ bán hàng, tiết kiệm chi phí nhất có thể. 

- Hoặc đối với nhóm ngành hàng thời trang, Sổ bán hàng làm thế nào để cạnh tranh với Shoppe, Lazada, ..
6. Stories (Câu chuyện): Cuối cùng cần có một câu chuyện: Đơn giản, bất ngờ, thuyết phục, tạo cảm xúc. Ý tưởng hay, câu chuyện hay tạo ra phải gắn kết thương hiệu hơn và việc chỉ để nhiều người chia sẻ. 

=> Hiểu lý do tại so ý tưởng của SoBanHang lại được lan truyền: Đơn giản để mọi nhà bán hàng đều có thể trở nên nhàn hơn. Quan trọng hơn, thương hiệu cần 6 điều này để có thể viral.

Không nhất thiết phải bỏ tiền vào TVC để phát sóng, muốn viral để đánh bại họ phải tạo ra một câu chuyện hay, một ý tưởng độc đáo rồi giúp cho nó phát tán.
Ý tưởng đề xuất từ dữ liệu: Ở trang blog có thể tạo thêm một trang chuyên về hướng dẫn xây dựng branding, trading, nắm bắt tâm lý khách hàng và tạo những bài viết cụ thể của ngành marketing vì đối với bán hàng, xây dựng thương hiệu, dấu ấn trên thị trường là điều tiên quyết trong suốt vòng đời của nhãn hàng để cạnh tranh.

Đến với Sổ Bán Hàng, khách hàng không chỉ hòa chung nhịp đập chuyển đổi số mà vẫn tiết kiệm chi phí đầu tư, mang đến những giao diện, trải nghiệm khách hàng tốt nhất cho khách hàng. Bên cạnh đó còn là một cộng đồng cùng nhau xây dựng brand, dấu ấn cá nhân của thương hiệu mình.

Đối với những cửa hàng có chỉ số giao dịch thấp trên sổ, cần có nghĩ ra giải pháp để tăng doanh số, ví dụ tạo hệ thống recommendation về các bài viết xây dựng thương hiệu trên blog để họ có thể tham khảo, nghiên cứu cách xây dựng brand. 

[Dữ liệu phân tích](https://github.com/Quan-Thi-Thanh-Hoa/Little_project/blob/70f86234867cfc2f5c942b38de44b0e93b44fb74/Business-performance.xlsx)
