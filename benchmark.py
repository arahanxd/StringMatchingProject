import time
import difflib
from horspool import horspool_search
from naive import naive_search

def compare_algorithms(text, pattern):
    """Measures execution time for both algorithms."""
    
    # Horspool benchmark
    start_time = time.perf_counter()
    horspool_matches = horspool_search(text, pattern)
    horspool_time = time.perf_counter() - start_time
    
    # Naive benchmark
    start_time = time.perf_counter()
    naive_matches = naive_search(text, pattern)
    naive_time = time.perf_counter() - start_time
    
    return {
        'horspool_time': horspool_time,
        'naive_time': naive_time,
        'matches_count': len(horspool_matches),
        'results_match': horspool_matches == naive_matches
    }

def calculate_similarity(text1, text2):
    """Bonus feature: calculate similarity score between two strings."""
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return round(matcher.ratio() * 100, 2)

def best_similarity_in_text(lines, pattern):
    """Finds the highest similarity score for words in the text against the pattern."""
    best_score = 0.0
    for line in lines:
        for word in line.split():
            # Stripping punctuation for better comparison
            clean_word = "".join(c for c in word if c.isalnum())
            if clean_word:
                score = calculate_similarity(clean_word.lower(), pattern.lower())
                if score > best_score:
                    best_score = score
    return best_score
