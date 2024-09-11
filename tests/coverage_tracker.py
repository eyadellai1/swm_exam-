
def print_coverage_report(coverage_tracker):
    print("\nManual Coverage Report:")
    total_lines = len(coverage_tracker)
    executed_lines = sum(1 for count in coverage_tracker.values() if count > 0)
    print(f"Executed {executed_lines} out of {total_lines} lines.")
    print(f"Coverage: {(executed_lines / total_lines) * 100:.2f}%")
    print("\nDetailed Coverage:")
    for line, count in coverage_tracker.items():
        print(f"{line}: Executed {count} times")
