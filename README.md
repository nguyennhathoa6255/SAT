## Bài tập nhóm môn: Artificial Intelligence
**Ứng dụng cuối: [Deploy](https://nhom1-trituetunhien.streamlit.app/)**

![Home](src\home.png)

**Làm cách nào chúng tôi có thể triển khai PL-Resolution, DPLL và WalkSAT một cách hiệu quả bằng một ngôn ngữ lập trình cụ thể?**
- Hiểu các khái niệm cốt lõi của từng thuật toán.
- Lựa chọn ngôn ngữ lập trình phù hợp để thực hiện.
- Đánh giá các chỉ số hiệu suất để so sánh.

### 1. Lý thuyết:
**Thuật toán PL-Resolution**:
Thuật toán PL-Resolution là một thuật toán sử dụng trong lĩnh vực Logic Học định lý (Logic theorem proving) để kiểm tra tính hợp lệ của một tập hợp các mệnh đề dựa trên quy tắc phân giải (resolution rule).

**Thuật toán DPLL**:
 Thuật toán Davis - Putnam - Logemann - Loveland (DPLL) là một phương pháp tìm kiếm đệ quy để xác định sự thỏa mãn (satisfiability - SAT) của công thức CNF. Thuật toán DPLL có nền tảng từ tìm kiếm quay lui (backtrack search) để có được giá trị thỏa mãn.

**Thuật toán WalkSAT**:
 WalkSAT là một thuật toán tìm kiếm có thứ tự (stochastic local search algorithm) được sử dụng để giải quyết bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP)
### 2. Dataset
Tạo ngẫu nhiên 2 bộ dataset:

**Uniform-Random3**: 
- Đây là một loại dữ liệu được tạo ngẫu nhiên để nghiên cứu bài toán SAT.
- Mỗi biểu thức logic được biểu diễn dưới dạng 3-CNF (Conjunctive Normal Form) với mỗi mệnh đề chứa đúng 3 biến.
- Các giá trị của biến và các mệnh đề được chọn ngẫu nhiên.
- Dữ liệu này giúp nắm bắt tính phức tạp của bài toán SAT và thử nghiệm các thuật toán giải quyết.
```
def generate_uniform_random_3sat(num_vars, num_clauses):
        clauses = []
        for _ in range(num_clauses):
            # Chọn ngẫu nhiên 3 biến khác nhau
            clause = np.random.choice(num_vars, 3, replace=False)
            # Phủ định mỗi biến với xác suất 1/2
            clause = [var if np.random.rand() > 0.5 else -var for var in clause]
            clauses.append(clause)
        return clauses
```

**Random -3SAT-backbone**:
- Dữ liệu này cũng liên quan đến bài toán SAT và được sử dụng để nghiên cứu hiệu suất của các thuật toán.
- Mỗi biểu thức logic được tạo dưới dạng 3-CNF với mỗi mệnh đề chứa đúng 3 biến.
- Tuy nhiên, dữ liệu này được tạo ra theo một cách khác, có thể dựa trên cấu trúc ngẫu nhiên hoặc backbone (một phần của biểu thức được xác định trước).
- Dữ liệu này giúp nghiên cứu sự ảnh hưởng của cấu trúc ngẫu nhiên hoặc backbone đối với khả năng giải quyết của các thuật toán.
```
def generate_random_3sat_instance(num_vars, num_clauses, backbone_size):
        # Khởi tạo ví dụ với một danh sách rỗng các mệnh đề
        instance = []

        # Xác định tập backbone bằng cách chọn backbone_size biểu thức ngẫu nhiên
        backbone = set(random.sample(range(1, num_vars + 1), backbone_size))

        # Thêm phủ định vào tập backbone với xác suất 50%
        backbone = {lit if random.choice([True, False]) else -lit for lit in backbone}

        while len(instance) < num_clauses:
            # Tạo một mệnh đề với 3 biểu thức duy nhất
            clause = set()
            while len(clause) < 3:
                var = random.randint(1, num_vars)
                lit = var if random.choice([True, False]) else -var
                clause.add(lit)

            # Chuyển đổi mệnh đề thành tuple và thêm vào ví dụ
            instance.append(tuple(clause))

        # Đảm bảo các biểu thức trong backbone có mặt trong ví dụ
        for lit in backbone:
            if not any(lit in clause or -lit in clause for clause in instance):
                # Thêm một mệnh đề mới chứa biểu thức trong backbone
                clause = {lit, random.randint(1, num_vars), random.randint(1, num_vars)}
                instance.append(tuple(clause))
        return instance
```
### 3. Triển khai Streamlit:
Tổ chức dự án:
```
├── main/                             : Chứa mã triển khai
├── src/                              : Tài nguyên
│   └── build.py                      : Tạo dataset và các thuật toán
│   └── search.py                     : Tìm hiểu bài
├── README.md                         : Báo cáo
├── .gitignore                        
└── requirements.txt                  : Package cần thiết 
```

Ứng dụng khi triển khai lên streamlit: [Deploy](https://nhom1-trituetunhien.streamlit.app/)


### 4. Kết luận
Từ các kết quả khi chạy thuật toán có thể kết luận được các trường hợp khi sử dụng:
- Kiểm tra tính hợp lệ: Chọn PL-resolution.
- Tìm phép gán thỏa mãn, cấu trúc rõ ràng: Chọn DPLL.
- Giải quyết nhanh, cấu trúc ngẫu nhiên hoặc ít bị ràng buộc: Chọn WalkSAT.
- Bài toán lớn, nhiều biến và ràng buộc, cần đảm bảo tìm kiếm phép gán thỏa mãn: Chọn DPLL.
