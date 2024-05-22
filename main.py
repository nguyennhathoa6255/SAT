import time
import streamlit as st
import build as bd


# Thiết lập page
st.set_page_config(     
    page_title="Nhóm 1 - Trí tuệ tự nhiên",      
    page_icon="🧊"  
)

# Thiết lập tiêu đề
st.subheader('Triển khai các thuật toán cho bài toán SAT')

with st.sidebar:
    # Số lượng biến và mệnh đề cho Uniform Random-3-SAT
    num_vars = st.number_input('Số lượng biến:', value=10)
    num_clauses = st.number_input('Số lượng mệnh đề:', value=40)
    backbone_size = st.number_input('Kích thước backbone:', value=10)
# Tạo input cho Uniform Random-3-SAT
ur_3sat_instance = bd.Dataset.generate_uniform_random_3sat(num_vars, num_clauses)

# Số lượng biến và mệnh đề cho Random-3-SAT
# backbone_size = 10  # Kích thước backbone

sat_instance = bd.Dataset.generate_random_3sat_instance(num_vars, num_clauses, backbone_size)

# Sử dụng hàm generate_alpha để tạo alpha
alpha = bd.Dataset.generate_alpha(num_vars)

# In ra một số thông tin về input
start_time = time.time()

with st.sidebar:
    dataset_type = st.selectbox('Chọn bộ dữ liệu:', ['ur_3sat_instance', 'sat_instance'])
    algorithm_type = st.selectbox('Chọn thuật toán:', ['PL_Resolution', 'dpll', 'walksat'])

def data_type(dataset_type):
    if dataset_type == 'ur_3sat_instance':
        dataset_type = ur_3sat_instance
    elif dataset_type == 'sat_instance':
        dataset_type = sat_instance
    return dataset_type
    
st.write(f'Knowledge Base: {data_type(dataset_type)}')
st.write(f'Alpha: {alpha}')

def algo_type(algorithm_type):
    return algorithm_type

if algorithm_type == 'PL_Resolution':
    start_time = time.time()
    # Kiểm tra tìm kiếm phép phân giải với KB và alpha
    result = bd.Algorithm.PL_Resolution(ur_3sat_instance, alpha)

    end_time = time.time()
    execution_time = end_time - start_time

    if result:
        st.write("Có phân giải hợp lý với KB và alpha.")
    else:
        st.write("Không có phân giải hợp lý với KB và alpha.")

    st.write(f"Thời gian thực thi: {execution_time} giây.")

elif algorithm_type == 'dpll':
    start_time = time.time()
    # Kiểm tra xem alpha có thể được suy ra từ ur_3sat_instance không
    dpll_solution = bd.Algorithm.dpll(ur_3sat_instance + [alpha])
    end_time = time.time()
    execution_time = end_time - start_time

    if dpll_solution:
        st.write("Tìm được lời giải thỏa mãn KB và alpha:")
        st.table(dpll_solution)
    else:
        st.write("Không tìm được lời giải thỏa mãn KB và alpha.")
    st.write(f"Thời gian thực thi: {execution_time} giây.")

else:
    start_time = time.time()
    # Giải bài toán Uniform Random-3-SAT bằng WalkSAT với alpha
    solution = bd.Algorithm.walksat(ur_3sat_instance, alpha)

    end_time = time.time()
    execution_time = end_time - start_time

    if solution:
        st.write("\nTìm được lời giải thỏa mãn KB và alpha:")
        solution_str = ['Yes' if value == 1 else 'No' for value in solution]
        st.write(solution_str)
    else:
        st.write("\nKhông tìm được lời giải thỏa mãn KB và alpha.")
        
    st.write(f"Thời gian thực thi: {execution_time} giây.")
