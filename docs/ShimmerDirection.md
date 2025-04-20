# ShimmerDirection

An enumeration class that defines the direction options for the shimmer effect.

## Values

- `RIGHT_TO_LEFT`: The shimmer effect moves from right to left.
- `LEFT_TO_RIGHT`: The shimmer effect moves from left to right.
- `TOP_TO_BOTTOM`: The shimmer effect moves from top to bottom.
- `BOTTOM_TO_TOP`: The shimmer effect moves from bottom to top.

## Usage Example

```python
from flet_shimmer import ShimmerDirection

# Using in Shimmer initialization
direction = ShimmerDirection.RIGHT_TO_LEFT

# Random selection example
import random
random_direction = random.choice([
    ShimmerDirection.RIGHT_TO_LEFT,
    ShimmerDirection.LEFT_TO_RIGHT,
    ShimmerDirection.TOP_TO_BOTTOM,
    ShimmerDirection.BOTTOM_TO_TOP
])
```