### Chứng minh các bài toán Independent Set, K-Clique, và Vertex Cover là NP-Complete

#### 1. Independent Set (Tập độc lập)

**Định nghĩa**: Một tập độc lập trong một đồ thị là một tập các đỉnh sao cho không có cạnh nào nối giữa bất kỳ hai đỉnh nào trong tập đó.

**Chứng minh Independent Set là NP-Complete**:
- **Independent Set thuộc NP**: Cho một tập các đỉnh \( S \) của đồ thị \( G \), ta có thể kiểm tra trong thời gian đa thức liệu \( S \) có phải là một tập độc lập hay không bằng cách kiểm tra tất cả các cặp đỉnh trong \( S \) xem có cạnh nào nối giữa chúng không.
  
- **Giảm từ SAT về Independent Set**:
  - Cho một công thức logic mệnh đề dưới dạng CNF với \( m \) mệnh đề và \( n \) biến: \( \phi = C_1 \wedge C_2 \wedge ... \wedge C_m \).
  - Xây dựng đồ thị \( G \) như sau:
    - Với mỗi mệnh đề \( C_i \), tạo một đỉnh cho mỗi biến hoặc phủ định của biến trong mệnh đề đó.
    - Nối các đỉnh trong cùng một mệnh đề với nhau.
    - Nối các đỉnh đại diện cho biến \( x_j \) và \( \neg x_j \) (phủ định của \( x_j \)) trong các mệnh đề khác nhau.
  - Tìm một tập độc lập kích thước \( m \) trong đồ thị \( G \) tương đương với việc tìm một phép gán thỏa mãn cho công thức \( \phi \).

#### 2. K-Clique

**Định nghĩa**: Một K-Clique trong một đồ thị là một tập các đỉnh mà mỗi cặp đỉnh trong tập đó đều có một cạnh nối trực tiếp. Nói cách khác, một K-Clique là một đồ thị con đầy đủ với \( K \) đỉnh.

**Chứng minh K-Clique là NP-Complete**:
- **K-Clique thuộc NP**: Cho một tập các đỉnh \( S \) của đồ thị \( G \), ta có thể kiểm tra trong thời gian đa thức liệu \( S \) có phải là một K-Clique hay không bằng cách kiểm tra tất cả các cặp đỉnh trong \( S \) xem có cạnh nối giữa chúng hay không.

- **Giảm từ Independent Set về K-Clique**:
  - Cho một đồ thị \( G \) và một số \( k \), tạo đồ thị bù \( G' \) bằng cách đổi tất cả các cạnh thành không cạnh và ngược lại.
  - Một tập độc lập kích thước \( k \) trong \( G \) tương đương với một K-Clique kích thước \( k \) trong \( G' \).

#### 3. Vertex Cover (Tập đỉnh phủ)

**Định nghĩa**: Một tập đỉnh phủ trong một đồ thị là một tập các đỉnh sao cho mỗi cạnh trong đồ thị đều có ít nhất một đỉnh thuộc tập đó.

**Chứng minh Vertex Cover là NP-Complete**:
- **Vertex Cover thuộc NP**: Cho một tập các đỉnh \( S \) của đồ thị \( G \), ta có thể kiểm tra trong thời gian đa thức liệu \( S \) có phải là một tập đỉnh phủ hay không bằng cách kiểm tra tất cả các cạnh trong \( G \) xem có đỉnh nào thuộc \( S \) hay không.

- **Giảm từ Independent Set về Vertex Cover**:
  - Cho một đồ thị \( G \) và một số \( k \), \( S \) là một tập độc lập kích thước \( k \) trong \( G \) nếu và chỉ nếu tập các đỉnh còn lại \( V - S \) là một tập đỉnh phủ kích thước \( |V| - k \) trong \( G \).

#### Quan hệ giữa các bài toán

1. **K-Clique và Vertex Cover**:
   - **K-Clique sang Vertex Cover**: Trong một đồ thị \( G \), nếu tồn tại một K-Clique, thì tập các đỉnh không thuộc K-Clique sẽ là một tập đỉnh phủ của đồ thị bù \( G' \).
   - **Vertex Cover sang K-Clique**: Trong đồ thị bù \( G' \), nếu tồn tại một tập đỉnh phủ kích thước \( k \), thì tập các đỉnh còn lại sẽ là một K-Clique kích thước \( |V| - k \) trong đồ thị ban đầu \( G \).

2. **Vertex Cover và Independent Set**:
   - **Vertex Cover sang Independent Set**: Trong một đồ thị \( G \), nếu tồn tại một tập đỉnh phủ kích thước \( k \), thì các đỉnh không thuộc tập đỉnh phủ sẽ tạo thành một tập độc lập kích thước \( |V| - k \).
   - **Independent Set sang Vertex Cover**: Trong một đồ thị \( G \), nếu tồn tại một tập độc lập kích thước \( k \), thì các đỉnh còn lại sẽ tạo thành một tập đỉnh phủ kích thước \( |V| - k \).

3. **Independent Set và K-Clique**:
   - **Independent Set sang K-Clique**: Một tập độc lập kích thước \( k \) trong đồ thị \( G \) sẽ tương ứng với một K-Clique kích thước \( k \) trong đồ thị bù \( G' \).
   - **K-Clique sang Independent Set**: Một K-Clique kích thước \( k \) trong đồ thị \( G \) sẽ tương ứng với một tập độc lập kích thước \( k \) trong đồ thị bù \( G' \).

### Kết luận

Chứng minh rằng Independent Set, K-Clique, và Vertex Cover là NP-Complete có thể được thực hiện bằng cách:

- Chứng minh mỗi bài toán thuộc NP.
- Giảm từ SAT (một bài toán NP-Complete đã biết) về các bài toán này.
- Chuyển đổi giữa các bài toán với nhau để chứng minh tính NP-Completeness của chúng.

Việc này khẳng định rằng các bài toán này đều là NP-Complete, và nếu có một thuật toán giải quyết hiệu quả một trong các bài toán này, thì nó cũng có thể giải quyết hiệu quả tất cả các bài toán khác trong lớp NP.