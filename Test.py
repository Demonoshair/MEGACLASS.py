import logging

logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="w",
    format="we have next logging message:%(asctime)s:%(levelname)s - %(message)s"
)
numbers=[1, 2, 3, 4, 5]
iterable_num=iter(numbers)

while True:
    try:
        current_num = next(iterable_num)
        logging.info(f"Мы взяли из корзинки мыблочко под номером {current_num}")
    except StopIteration:
        logging.error("Мыблочки закончились(")
        break