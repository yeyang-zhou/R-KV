from .compression import H2O, R1KV, AnalysisKV, SnapKV, StreamingLLM


def build_r1kv_serving_algorithm(config):
    """LMCache token-drop plugin entry point for R-KV."""
    return R1KV.from_serving_config(config)


__all__ = [
    "H2O",
    "R1KV",
    "AnalysisKV",
    "SnapKV",
    "StreamingLLM",
    "build_r1kv_serving_algorithm",
]
