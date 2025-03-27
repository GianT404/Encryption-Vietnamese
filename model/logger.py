import logging
import os

# Xác định thư mục lưu log, ví dụ: ../logs nằm cùng cấp với thư mục model
LOG_FOLDER = os.path.join(os.path.dirname(__file__), "..", "logs")
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)
LOG_FILE = os.path.join(LOG_FOLDER, "activity.log")

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)