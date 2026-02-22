"""
Solutions for Exercise Set 4: Performance Optimization & ML Pipelines
"""

import logging
import time
from functools import lru_cache

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# ===== INTERMEDIATE SOLUTIONS =====

def profile_implementations():
    """Compare performance of different approaches"""
    n = 10000
    
    # List comprehension
    start = time.time()
    result1 = [x**2 for x in range(n)]
    time1 = time.time() - start
    
    # Map
    start = time.time()
    result2 = list(map(lambda x: x**2, range(n)))
    time2 = time.time() - start
    
    # Generator
    start = time.time()
    result3 = list(x**2 for x in range(n))
    time3 = time.time() - start
    
    print(f"List comp: {time1:.6f}s, Map: {time2:.6f}s, Generator: {time3:.6f}s")

def process_large_dataset(max_size=1000000):
    """Process large dataset efficiently using generators"""
    def data_generator():
        for i in range(max_size):
            yield {"id": i, "value": i ** 2}
    
    count = 0
    for batch in data_generator():
        count += 1
    
    return count

# ===== ADVANCED SOLUTIONS =====

class Pipeline:
    """Full ML pipeline with error handling and logging"""
    def __init__(self, name):
        self.name = name
        self.data = None
    
    def load_data(self, data):
        logger.info(f"Loading data for {self.name}")
        if not data:
            raise ValueError("Data cannot be empty")
        self.data = data
        logger.info(f"Loaded {len(data)} samples")
    
    def preprocess(self):
        logger.info("Preprocessing data")
        self.data = [x * 2 for x in self.data]
    
    def evaluate(self):
        logger.info("Evaluating pipeline")
        return sum(self.data) / len(self.data)

class TextClassifier:
    """Optimized text classifier with caching"""
    def __init__(self):
        self.cache = {}
    
    @lru_cache(maxsize=128)
    def extract_features(self, text):
        features = len(text.split())
        return features
    
    def predict(self, text):
        features = self.extract_features(text)
        return "positive" if features > 5 else "negative"

if __name__ == "__main__":
    profile_implementations()
    pipeline = Pipeline("ML Pipeline")
    pipeline.load_data([1, 2, 3, 4, 5])
    pipeline.preprocess()
    print(f"Mean: {pipeline.evaluate()}")
