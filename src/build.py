import numpy as np
import random

class Dataset():

    def generate_uniform_random_3sat(num_vars, num_clauses):
        clauses = []
        for _ in range(num_clauses):
            # Chọn ngẫu nhiên 3 biến khác nhau
            clause = np.random.choice(num_vars, 3, replace=False)
            # Phủ định mỗi biến với xác suất 1/2
            clause = [var if np.random.rand() > 0.5 else -var for var in clause]
            clauses.append(clause)
        return clauses

    
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
    
    def generate_alpha(num_vars):
        # Chọn ngẫu nhiên 3 biến khác nhau
        alpha_clause = np.random.choice(range(1, num_vars+1), 3, replace=False)
        # Phủ định mỗi biến với xác suất 1/2
        alpha_clause = [var if np.random.rand() > 0.5 else -var for var in alpha_clause]
        return alpha_clause
    

class Algorithm():
    # Hàm kiểm tra xem một mệnh đề có phải là mệnh đề trống không
    def is_empty_clause(clause):
        return len(clause) == 0

    # Hàm kiểm tra xem hai mệnh đề có phải là mệnh đề đối nhau không
    def is_complementary(clause1, clause2):
        for literal in clause1:
            if -literal in clause2:
                return True
        return False

    # Hàm PL_Resolve để tạo ra các mệnh đề mới từ hai mệnh đề đầu vào
    def PL_Resolve(clause1, clause2):
        resolved_clause = []
        for literal in clause1:
            if -literal not in clause2:
                resolved_clause.append(literal)
        return resolved_clause

    # Hàm kiểm tra xem mệnh đề mới đã tồn tại trong tập mệnh đề hay chưa
    def is_clause_in_set(clause, clause_set):
        for c in clause_set:
            if set(c) == set(clause):
                return True
        return False

    # Thuật toán PL_Resolution
    def PL_Resolution(clauses, alpha):
        # Thêm phủ định của alpha vào KB
        clauses_with_alpha = clauses + [[-lit for lit in alpha]]
        new_clauses = set(tuple(clause) for clause in clauses_with_alpha)
        while True:
            n = len(new_clauses)
            pairs = [(clause1, clause2) for clause1 in new_clauses for clause2 
                    in new_clauses if clause1 != clause2]
            for (clause1, clause2) in pairs:
                if Algorithm.is_complementary(clause1, clause2):
                    resolved_clause = Algorithm.PL_Resolve(clause1, clause2)
                    if Algorithm.is_empty_clause(resolved_clause):
                        return True
                    if not Algorithm.is_clause_in_set(resolved_clause, new_clauses):
                        new_clauses.add(tuple(resolved_clause))
            if len(new_clauses) == n:
                return False
    # Thuật toán DPLL       
    def dpll(clauses, assignment=[]):
        # Kiểm tra xem có mệnh đề rỗng nào không
        if [] in clauses:
            return False
        # Kiểm tra xem tất cả mệnh đề đã được thỏa mãn chưa
        if not clauses:
            return assignment
        # Chọn một biến ngẫu nhiên từ mệnh đề đầu tiên
        for clause in clauses:
            if clause:
                var = random.choice(clause)
                break
        # Tạo danh sách các mệnh đề mới sau khi gán giá trị cho biến
        def new_clauses(clauses, var):
            # Loại bỏ mệnh đề nếu chứa biến với giá trị đúng
            # Loại bỏ biến đối lập nếu mệnh đề chứa biến đối lập
            new_clauses = []
            for clause in clauses:
                if var in clause:
                    continue
                new_clause = [x for x in clause if x != -var]
                new_clauses.append(new_clause)
            return new_clauses
        # Thử gán True cho biến và gọi đệ quy DPLL
        if Algorithm.dpll(new_clauses(clauses, var), assignment + [var]):
            return assignment + [var]
        # Thử gán False cho biến và gọi đệ quy DPLL
        if Algorithm.dpll(new_clauses(clauses, -var), assignment + [-var]):
            return assignment + [-var]
        # Nếu cả hai trường hợp đều không thỏa mãn, trả về False
        return False
    # Thuật toán WalkSAT
    def walksat(clauses, alpha, max_flips=10000, p=0.5):
        # Thêm phủ định của alpha vào KB
        clauses_with_alpha = clauses + [[-lit for lit in alpha]]

        # Khởi tạo một lời giải ngẫu nhiên
        n_vars = max(abs(var) for clause in clauses_with_alpha for var in clause)
        assignment = [random.choice([-1, 1]) for _ in range(n_vars)]
        for _ in range(max_flips):
            # Tìm mệnh đề không thỏa mãn
            unsatisfied = [clause for clause in clauses_with_alpha if not any(assignment[abs(var) - 1] == var // abs(var) for var in clause)]

            # Nếu không còn mệnh đề không thỏa mãn, trả về lời giải
            if not unsatisfied:
                return assignment

            # Chọn một mệnh đề không thỏa mãn
            clause = random.choice(unsatisfied)

            # Với xác suất p, chọn một biến ngẫu nhiên trong mệnh đề để đảo giá trị
            # Với xác suất 1-p, chọn biến làm giảm nhiều nhất số mệnh đề không thỏa mãn
            if random.random() < p:
                var = random.choice(clause)
            else:
                # Tạo danh sách các cặp (bool, var) cho mỗi biến trong mệnh đề
                bool_var_pairs = [(assignment[abs(var) - 1] != var // abs(var), var) for var in clause]

                # Sắp xếp danh sách theo thứ tự tăng dần của giá trị bool
                bool_var_pairs.sort()

                # Chọn biến đầu tiên (làm giảm nhiều nhất số mệnh đề không thỏa mãn)
                var = bool_var_pairs[0][1]

            # Đảo giá trị của biến đã chọn
            assignment[abs(var) - 1] *= -1

        # Nếu không tìm được lời giải sau số lần đảo giá trị tối đa, trả về None
        return None