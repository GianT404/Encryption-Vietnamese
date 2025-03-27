# model/transposition.py

def rail_fence_encrypt(text, rails):
    """
    Mã hóa Rail Fence Cipher.
    :param text: Văn bản gốc
    :param rails: Số dòng (rail) sử dụng (>= 2)
    :return: Văn bản đã được mã hóa
    """
    if rails <= 1:
        return text

    # Tạo danh sách cho từng hàng
    fence = [[] for _ in range(rails)]
    rail = 0
    step = 1
    for char in text:
        fence[rail].append(char)
        rail += step
        if rail == 0 or rail == rails - 1:
            step *= -1  # Đảo chiều khi chạm biên
    encrypted = "".join("".join(row) for row in fence)
    return encrypted

def rail_fence_decrypt(text, rails):
    """
    Giải mã Rail Fence Cipher.
    :param text: Văn bản đã mã hóa
    :param rails: Số dòng (rail) đã dùng để mã hóa
    :return: Văn bản gốc
    """
    if rails <= 1:
        return text

    # Xây dựng pattern vị trí từng ký tự theo từng hàng
    pattern = []
    rail = 0
    step = 1
    for i in range(len(text)):
        pattern.append(rail)
        rail += step
        if rail == 0 or rail == rails - 1:
            step *= -1

    # Tính số ký tự của mỗi hàng
    rail_counts = [pattern.count(r) for r in range(rails)]
    fence = []
    index = 0
    for count in rail_counts:
        fence.append(list(text[index:index+count]))
        index += count

    # Dùng pattern để sắp xếp lại các ký tự theo thứ tự ban đầu
    result = []
    rail_positions = [0] * rails
    for r in pattern:
        result.append(fence[r][rail_positions[r]])
        rail_positions[r] += 1
    return "".join(result)
