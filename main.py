import os
import time
from horspool import horspool_search
from naive import naive_search
from benchmark import compare_algorithms, best_similarity_in_text
from utils import read_file, scan_directory, write_report

def display_menu():
    print("\n===== STRING MATCHING TOOL =====")
    print("1. Search pattern in one file")
    print("2. Search pattern in all files")
    print("3. Compare Horspool vs Naive")
    print("4. Generate report")
    print("5. Exit")
    print("================================")

def search_in_file(filepath, patterns, print_results=True):
    lines = read_file(filepath)
    results = {p: [] for p in patterns}
    
    for line_idx, line in enumerate(lines, start=1):
        for pattern in patterns:
            # Using Horspool as our primary search algorithm
            matches = horspool_search(line, pattern)
            if matches:
                results[pattern].append((line_idx, matches))
                if print_results:
                    for match_idx in matches:
                        print(f"{os.path.basename(filepath)} -> Line {line_idx}, Position {match_idx + 1}")
                    
    return results, lines

def main():
    report_content = "--- String Matching Execution Report ---\n\n"
    report_content += "Requirements Met:\n"
    report_content += "- Sequential Access: Implemented in read_file() to scan whole file line by line.\n"
    report_content += "- Direct Access: Implemented in read_file_direct() using f.seek() to jump directly to byte offsets.\n"
    report_content += "- Algorithms: Horspool and Naive comparison implemented.\n\n"
    report_content += "Execution Logs:\n"
    
    report_file = "report.txt"

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filepath = input("Enter file path: ")
            if not os.path.exists(filepath):
                print("File not found.")
                continue
                
            patterns_input = input("Enter pattern(s) separated by comma: ")
            patterns = [p.strip() for p in patterns_input.split(',') if p.strip()]
            
            print("\nScanning...")
            start_time = time.time()
            results, lines = search_in_file(filepath, patterns)
            
            total_matches = sum(len(m_list) for match_list in results.values() for _, m_list in match_list)
            print(f"\n{total_matches} matches found.")
            
            # Bonus feature: Similarity Score
            if patterns:
                best_sim = best_similarity_in_text(lines, patterns[0])
                print(f"Similarity score for '{patterns[0]}' with closest word in file: {best_sim}%")
            
            report_content += f"Searched in '{filepath}' for patterns {patterns}. Found {total_matches} matches.\n"
            
        elif choice == '2':
            folderpath = input("Enter folder path: ")
            if not os.path.exists(folderpath):
                print("Folder not found.")
                continue
                
            patterns_input = input("Enter pattern(s) separated by comma: ")
            patterns = [p.strip() for p in patterns_input.split(',') if p.strip()]
            
            files = scan_directory(folderpath)
            print("\nScanning...\n")
            
            total_matches = 0
            for file in files:
                results, _ = search_in_file(file, patterns)
                for match_list in results.values():
                    for _, m_list in match_list:
                        total_matches += len(m_list)
                    
            print(f"\n{total_matches} matches found across {len(files)} files.")
            report_content += f"Scanned folder '{folderpath}' for patterns {patterns}. Found {total_matches} matches.\n"
            
        elif choice == '3':
            filepath = input("Enter file path for benchmark: ")
            if not os.path.exists(filepath):
                print("File not found.")
                continue
                
            pattern = input("Enter pattern: ")
            print("\nRunning benchmarks...")
            
            lines = read_file(filepath)
            text_content = "\n".join(lines)
            
            stats = compare_algorithms(text_content, pattern)
            
            print(f"Total matches: {stats['matches_count']}")
            print(f"Time taken (Horspool): {stats['horspool_time']:.6f} sec")
            print(f"Time taken (Naive): {stats['naive_time']:.6f} sec")
            
            report_content += f"Benchmark on '{filepath}' for '{pattern}': "
            report_content += f"Horspool: {stats['horspool_time']:.6f}s, Naive: {stats['naive_time']:.6f}s.\n"
            
        elif choice == '4':
            write_report(report_file, report_content)
            print(f"\nReport successfully generated and saved to {report_file}")
            
        elif choice == '5':
            print("Exiting tool. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
