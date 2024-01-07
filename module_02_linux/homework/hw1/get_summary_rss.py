import os.path

PATH_TO_OUTPUT_FILE = os.path.abspath("output_file.txt")


def get_summary_rss(ps_output_file_path: str) -> str:
    memory_sum = 0
    with open(ps_output_file_path, "r") as file:
        for line in file:
            try:
                mem_chunk: int = int(line.split()[5:6][0])
                memory_sum += mem_chunk
            except ValueError:
                pass
    result: str = str(memory_sum // 1024) + ' Kb'
    return result


get_summary_rss(PATH_TO_OUTPUT_FILE)

if __name__ == '__main__':
    path: str = PATH_TO_OUTPUT_FILE
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
